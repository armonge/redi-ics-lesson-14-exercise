"""
ICS Lesson 14: Recap
Exercise 4: Loops, Files, Operators, Modules, Functions, etc

Write a function that takes one argument
    - filepath: string
        the path to a CSV file, where each line contains 2
        columns separated by commas like the like the following:
            `OPERATION_NAME,NUMBER`

        Where `OPERATION_NAME` can be any of the following:
            - `SUM`
            - `MULTIPLY`
            - `DIVIDE`
            - `SUBTRACT`

Assuming an initial value of 0, apply the operations in each of the file lines to 
this initial value and return the final result

Hint: You will need to open a file using the `open` function
Hint: In python, files are **iterable**
Hint: You can use your previous functions here too!

Bonus! Instead of opning a hardcoded file open one that's given as an argument to the script
Eg:
    python exercise_4.py csvs/file1.csv

Documentation:
https://docs.python.org/3/library/functions.html#open
https://www.pythontutorial.net/python-basics/python-read-text-file/
"""


def process_file(filepath):
    pass


def test_process_file():
    assert process_file("csvs/file1.csv") == 1


if __name__ == "__main__":
    import pytest
    pytest.main([__file__])
