"""
ICS Lesson 14: Recap
Exercise 1: Types

Write a function that takes 1 argument
    - operation: string

This `operation` argument has the form: 
    `OPERATION_NAME,NUMBER`

The function should return a `tuple` with 2 values, 
    - OPERATION_NAME as a string variable 
    - NUMBER as a python number variable

Hint! Here's the python documentation for the builtin string methods
    https://docs.python.org/3/library/stdtypes.html#string-methods

    You will need to use one of those to `split` the string

Hint! Here's the python documentation for tuples
    https://docs.python.org/3/library/stdtypes.html#tuples

Standard Python types
    https://docs.python.org/3/library/functions.html#int
    https://docs.python.org/3/library/functions.html#float
"""


def split_operation(operation):
    pass


def test_split_operation():
    assert split_operation("SUM,5") == ("SUM", 5)
    assert split_operation("MULTIPLY,5") == ("MULTIPLY", 5)
    assert split_operation("DIVIDE,2") == ("DIVIDE", 2)
    assert split_operation("SUBTRACT,10") == ("SUBTRACT", 10)


if __name__ == "__main__":
    import pytest
    pytest.main([__file__])
