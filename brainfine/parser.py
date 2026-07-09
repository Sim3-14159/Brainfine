import ply.yacc as yacc

from .ast import (
    AssignNode,
    BinaryExprNode,
    InputNode,
    LiteralNode,
    NameNode,
    OutputNode,
    PasteNode,
    ProgramNode,
    ReplaceNode,
    TaskCallNode,
    TaskDefNode,
    WhileNode,
)
from .lexer import lexer
from .tokens import TOKEN_NAMES


tokens = TOKEN_NAMES


class BrainfineParser:
    def __init__(self):
        self.parser = yacc.yacc(write_tables=False, debug=False)

    def parse(self, source: str):
        return self.parser.parse(source, lexer=lexer)


def p_program(p):
    "program : statement_list"
    p[0] = ProgramNode(p[1])


def p_statement_list(p):
    """statement_list : statement_list statement
                      | statement"""
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = [p[1]]


def p_statement_assign(p):
    "statement : SET IDENTIFIER optional_type TO expr"
    p[0] = AssignNode(name=p[2], value=p[5])


def p_statement_replace(p):
    "statement : REPLACE IDENTIFIER optional_type WITH expr"
    p[0] = ReplaceNode(name=p[2], value=p[5])


def p_statement_output(p):
    "statement : OUTPUT expr"
    p[0] = OutputNode(p[2])


def p_statement_input(p):
    "statement : INPUT IDENTIFIER optional_type"
    p[0] = InputNode(p[2])


def p_statement_paste(p):
    "statement : PASTE IDENTIFIER"
    p[0] = PasteNode(p[2])


def p_statement_task_def(p):
    "statement : TASK IDENTIFIER task_params DOES statement_list END"
    p[0] = TaskDefNode(name=p[2], params=p[3], body=p[5])


def p_statement_task_call(p):
    "statement : RUN IDENTIFIER task_args"
    p[0] = TaskCallNode(name=p[2], args=p[3])


def p_statement_while(p):
    "statement : WHILE expr DO statement_list END"
    p[0] = WhileNode(condition=p[2], body=p[4])


def p_task_params_empty(p):
    "task_params :"
    p[0] = []


def p_task_params_with(p):
    "task_params : WITH IDENTIFIER"
    p[0] = [p[2]]


def p_task_args_empty(p):
    "task_args :"
    p[0] = []


def p_task_args_with(p):
    "task_args : WITH expr"
    p[0] = [p[2]]


def p_optional_type_empty(p):
    "optional_type :"
    p[0] = None


def p_optional_type(p):
    "optional_type : TYPE IDENTIFIER"
    p[0] = p[2]


def p_expr_name(p):
    "expr : IDENTIFIER"
    p[0] = NameNode(p[1])


def p_expr_string(p):
    "expr : STRING"
    p[0] = LiteralNode(p[1])


def p_expr_number(p):
    "expr : NUMBER"
    p[0] = LiteralNode(p[1])


def p_expr_plus(p):
    "expr : expr PLUS expr"
    p[0] = BinaryExprNode("+", p[1], p[3])


def p_expr_tildeeq(p):
    "expr : expr TILDEEQ expr"
    p[0] = BinaryExprNode("~=", p[1], p[3])


def p_error(p):
    if p:
        print(f"Parser Error: Syntax error at token '{p.value}' on line {p.lineno}")
    else:
        print("Parser Error: Unexpected End of File")


_parser = BrainfineParser()


def parse_source(source: str):
    return _parser.parse(source)
