"""
ICS Lesson 14: Recap
Exercise 4: Bonus!

Think of the edgecases
    Eg:
        - What happens when you get an operation like `DIVIDE,0` ?
        - What if we get a line with more than 1 comma or more columns?
        

Implement some extra operations:
    Square Root? Power?

    Can you handle a CSV with swapped columns and headers?
    Eg: csvs/with-headers.csv

    hint: use csv.DictReader
        https://docs.python.org/3/library/csv.html#csv.DictReader
        https://python-adv-web-apps.readthedocs.io/en/latest/csv.html#reading-into-a-dictionary

"""


def process_file(filepath):
    pass


def test_process_file():
    assert process_file("csvs/file1.csv") == 1


if __name__ == "__main__":
    import pytest
    pytest.main([__file__])
