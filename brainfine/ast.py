from dataclasses import dataclass
from typing import Any


@dataclass
class ProgramNode:
    statements: list[object]


@dataclass
class AssignNode:
    name: str
    value: Any


@dataclass
class ReplaceNode:
    name: str
    value: Any


@dataclass
class OutputNode:
    value: Any


@dataclass
class InputNode:
    name: str


@dataclass
class TaskDefNode:
    name: str
    params: list[str]
    body: list[object]


@dataclass
class TaskCallNode:
    name: str
    args: list[object]


@dataclass
class WhileNode:
    condition: Any
    body: list[object]


@dataclass
class PasteNode:
    target: str


@dataclass
class LiteralNode:
    value: Any


@dataclass
class NameNode:
    name: str


@dataclass
class BinaryExprNode:
    op: str
    left: Any
    right: Any
