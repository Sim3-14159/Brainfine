from pathlib import Path

from .ast import AssignNode, InputNode, OutputNode, PasteNode, ProgramNode, ReplaceNode, TaskCallNode, TaskDefNode, WhileNode
from .parser import parse_source
from .utils import strip_comments


class BrainfinePreprocessor:
    def __init__(self):
        self.tasks: dict[str, TaskDefNode] = {}
        self.visited_files: set[Path] = set()

    def preprocess_file(self, path: str | Path):
        resolved_path = Path(path).resolve()
        self.visited_files.clear()
        self.tasks.clear()
        return self._preprocess_file(resolved_path)

    def _preprocess_file(self, path: Path):
        path = path.resolve()
        if path in self.visited_files or not path.exists():
            return ProgramNode([])

        self.visited_files.add(path)
        source = path.read_text(encoding="utf-8")
        ast = parse_source(strip_comments(source))
        self._collect_tasks(ast)

        expanded_statements = []
        for stmt in ast.statements:
            expanded_statements.extend(self._expand_statement(stmt, path))

        return ProgramNode(expanded_statements)

    def _collect_tasks(self, ast: ProgramNode):
        for node in ast.statements:
            self._collect_from_node(node)

    def _collect_from_node(self, node):
        match node:
            case TaskDefNode(name, _, _):
                self.tasks[name] = node
            case WhileNode(_, body):
                for stmt in body:
                    self._collect_from_node(stmt)
            case PasteNode(target):
                child_path = self._resolve_path(Path.cwd(), target)
                if child_path.exists():
                    child_ast = parse_source(strip_comments(child_path.read_text(encoding="utf-8")))
                    self._collect_tasks(child_ast)

    def _expand_statement(self, node, current_file: Path):
        match node:
            case TaskDefNode():
                return []
            case TaskCallNode(name, args):
                task = self.tasks.get(name)
                if task is None:
                    raise ValueError(f"Task '{name}' is not defined")
                return self._expand_statement_list(task.body, current_file)
            case PasteNode(target):
                child_path = self._resolve_path(current_file, target)
                if child_path.exists():
                    return self._preprocess_file(child_path).statements
                return []
            case WhileNode(condition, body):
                expanded_body = self._expand_statement_list(body, current_file)
                return [WhileNode(condition=condition, body=expanded_body)]
            case AssignNode() | ReplaceNode() | OutputNode() | InputNode():
                return [node]
            case _:
                return []

    def _expand_statement_list(self, statements, current_file: Path):
        expanded = []
        for statement in statements:
            expanded.extend(self._expand_statement(statement, current_file))
        return expanded

    def _resolve_path(self, current_file: Path, target: str):
        path = Path(target)
        if not path.suffix:
            path = path.with_suffix(".bfn")
        if not path.is_absolute():
            path = current_file.parent / path
        return path.resolve()
