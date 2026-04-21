# pylint: disable=W0613:unused-argument
# pylint: disable= C0116:missing-function-docstring
# pylint: disable= C0114:missing-module-docstring

from .types.formatType import FileFormatType

def load_text(path: str) -> str:
    with open(path, encoding="utf-8") as f:
        return f.read()
