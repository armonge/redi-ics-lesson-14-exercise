"""
ICS Lesson 14: Recap
Exercise 3: Modules

Write a function  that prints the arguments given to the python script

Hint: In order to solve this function you will need to `import` the module `sys` 
from the python standard library and use one of the variables it provides

https://docs.python.org/3/library/sys.html

Example:
    python exercises/exercise_3.py  csvs/file1.csv 
    ['exercises/exercise_3.py', 'csvs/file1.csv']


Question:
    - What type are the arguments?
    - Can you have multiple arguments?
    - What can you use these arguments for?
"""


def print_script_arguments():
    pass


def test_print_script_arguments(capsys):
    print_script_arguments()
    captured = capsys.readouterr()
    assert 'exercises/exercise_3.py' in captured.out


if __name__ == "__main__":
    import pytest
    pytest.main([__file__])
