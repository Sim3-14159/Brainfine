import ast

import ply.lex as lex

from .tokens import KEYWORDS, TOKEN_NAMES


tokens = TOKEN_NAMES

t_PLUS = r"\+"
t_TILDEEQ = r"~="
t_ignore = " \t\r"


def t_IDENTIFIER(t):
    r"[a-zA-Z_][a-zA-Z0-9_]*"
    upper_value = t.value.upper()
    t.type = KEYWORDS.get(upper_value, "IDENTIFIER")
    return t


def t_STRING(t):
    r'"([^"\\]|\\.)*"'
    try:
        t.value = ast.literal_eval(t.value)
    except Exception:
        t.value = t.value[1:-1]
    return t


def t_NUMBER(t):
    r"\d+"
    t.value = int(t.value)
    return t


def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)


def t_error(t):
    print(f"Lexer Error: Illegal character '{t.value[0]}' on line {t.lineno}")
    t.lexer.skip(1)


lexer = lex.lex()


def build_lexer():
    return lex.lex()
