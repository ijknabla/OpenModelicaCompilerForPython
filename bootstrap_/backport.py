__all__ = ("unparse",)

import sys

if sys.version_info < (3, 9):
    from astunparse import unparse
else:
    from ast import unparse
