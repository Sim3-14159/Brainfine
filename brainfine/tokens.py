from enum import Enum


class TokenType(str, Enum):
    IDENTIFIER = "IDENTIFIER"
    STRING = "STRING"
    NUMBER = "NUMBER"
    PLUS = "PLUS"
    TILDEEQ = "TILDEEQ"
    TASK = "TASK"
    END = "END"
    SET = "SET"
    RUN = "RUN"
    OUTPUT = "OUTPUT"
    INPUT = "INPUT"
    WHILE = "WHILE"
    DO = "DO"
    DOES = "DOES"
    WITH = "WITH"
    TYPE = "TYPE"
    TO = "TO"
    REPLACE = "REPLACE"
    PASTE = "PASTE"


KEYWORDS = {
    name.upper(): TokenType[name].value for name in (
        "TASK",
        "END",
        "SET",
        "RUN",
        "OUTPUT",
        "INPUT",
        "WHILE",
        "DO",
        "DOES",
        "WITH",
        "TYPE",
        "TO",
        "REPLACE",
        "PASTE",
    )
}


TOKEN_NAMES = [member.value for member in TokenType]
