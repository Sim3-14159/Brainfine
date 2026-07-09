import re


def strip_comments(source: str) -> str:
    source = re.sub(r"--[^\n]*", "", source)
    source = re.sub(r"PS.*?END", "", source, flags=re.DOTALL)
    return source
