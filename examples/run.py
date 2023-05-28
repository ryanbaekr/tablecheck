import os
import sys

_DIR = os.path.dirname(os.path.realpath(__file__))
_DIR = os.path.normpath(os.path.join(_DIR, ".."))

sys.path.insert(0, _DIR)

import example_multitablecheck

example_multitablecheck
