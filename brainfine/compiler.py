from .ast import AssignNode, InputNode, OutputNode, PasteNode, ProgramNode, ReplaceNode, TaskCallNode, TaskDefNode, WhileNode


class BrainfuckCompiler:
    def __init__(self):
        self.tasks: dict[str, TaskDefNode] = {}

    def compile(self, ast: ProgramNode) -> str:
        return "".join(self.generate(node) for node in ast.statements)

    def generate(self, node):
        match node:
            case AssignNode():
                return "{AssignNode}"
            case ReplaceNode():
                return "{ReplaceNode}"
            case OutputNode():
                return "{OutputNode}."
            case InputNode():
                return "{InputNode},"
            case TaskDefNode(name, _, _):
                self.tasks[name] = node
                return ""
            case TaskCallNode():
                return ""
            case WhileNode(_, body):
                #body_code = "".join(self.generate(stmt) for stmt in body)
                #return "[" + body_code + "]"
                return "{WhileNode}"
            case PasteNode():
                return ""
            case _:
                return ""
