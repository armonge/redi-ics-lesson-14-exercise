"""
ICS Lesson 14: Recap
Exercise 2: Operators and Logic

Write a function  that takes 2 arguments. 
    - operand1: number
    - operation:  string
        Contains an instruction to applied with `operand1`
        the `operation` argument will always be of the form
            `OPERATION_NAME,NUMBER`

            Where `OPERATION_NAME` can be any of the following:
                - `SUM`
                - `MULTIPLY`
                - `DIVIDE`
                - `SUBTRACT`



The function should return the result of applying the operation on the operand1

Hint!: Remember you can use the function you wrote in the previous exercise
"""


def process_operation(operand1, operation):
    pass


if __name__ == "__main__":
    assert process_operation(5, "SUM,5") == 10
    assert process_operation(2, "MULTIPLY,5") == 10
    assert process_operation(20, "DIVIDE,2") == 10
    assert process_operation(20, "SUBTRACT,10") == 10
