from tablecheck import MultiTableCheck

my_checker = MultiTableCheck(
    "example.xlsx",
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
