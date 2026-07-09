from pathlib import Path
import sys

from .compiler import BrainfuckCompiler
from .preprocessor import BrainfinePreprocessor


def main(argv: list[str] | None = None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    if not args:
        args = [str(Path(__file__).resolve().parent / "sample.bfn")]

    for path_str in args:
        path = Path(path_str).resolve()
        preprocessor = BrainfinePreprocessor()
        ast = preprocessor.preprocess_file(path)
        compiler = BrainfuckCompiler()
        print(f"Compiling {path}")
        print(compiler.compile(ast))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
