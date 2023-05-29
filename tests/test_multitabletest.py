import pandas as pd
from tablecheck import MultiTableCheck

def test_1(mocker):
    sheets = {
        "Sheet1": pd.DataFrame(data={'Column1': [1, 2], 'Column2': [3, 4]}),
        "Sheet2": pd.DataFrame(data={'Column3': [5, 6], 'Column4': [7, 8]}),
    }

    mocker.patch("pandas.read_excel", return_value=sheets)

    my_checker = MultiTableCheck(
        None,
        None,
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

    assert list(score.keys()) == ["check1", "check2"]
    assert score.get("check1").get("sheet") == "Sheet1"
    assert score.get("check1").get("result") == "success"
    assert score.get("check1").get("row").get("Column1") == 2
    assert score.get("check1").get("row").get("Column2") == 4
    assert score.get("check2").get("sheet") == "Sheet2"
    assert score.get("check2").get("result") == "success"
    assert score.get("check2").get("row").get("Column3") == 6
    assert score.get("check2").get("row").get("Column4") == 8
