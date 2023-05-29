import os
from tablecheck import MultiTableCheck

_DIR = os.path.dirname(os.path.realpath(__file__))
_FILE = os.path.normpath(os.path.join(_DIR, "example.xlsx"))

my_checker = MultiTableCheck(
    _FILE,
    [
        "Sheet1",
        "Sheet2",
    ],
)

check = {
    "name": "check1",
    "sheet": "Sheet1",
    "columns": [
        {
            "name": "Column1",
            "eq": [],   # multiple act as `or ==`
            "ne": [],   # multiple act as `and !=`
            "lt": [7],  # multiple act as `and <`
            "gt": [1],  # multiple act as `and >`
            "le": [],   # multiple act as `and <=`
            "ge": [],   # multiple act as `and >=`
        },
        {
            "name": "Column2",
            "eq": [4],
            "ne": [],
            "lt": [],
            "gt": [],
            "le": [],
            "ge": [],
        },
    ],
}

my_checker.check(check)

check = {
    "name": "check2",
    "sheet": "Sheet2",
    "columns": [
        {
            "name": "Column3",
            "eq": [my_checker.fetch("check1", "Column1") * 3],
            "ne": [],
            "lt": [],
            "gt": [],
            "le": [],
            "ge": [],
        },
    ],
}

my_checker.check(check)

score = my_checker.score()
print(score)
