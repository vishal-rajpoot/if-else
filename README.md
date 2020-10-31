THIS IS AN AGE CALACULATOR FOR THE DRIVING.



Welcome to the if-else wiki!

What is if...else statement in Python? Decision making is required when we want to execute a code only if a certain condition is satisfied.

The if…elif…else statement is used in Python for decision making.

Python if Statement Syntax if test expression: statement(s) Here, the program evaluates the test expression and will execute statement(s) only if the test expression is True.

If the test expression is False, the statement(s) is not executed.

In Python, the body of the if statement is indicated by the indentation. The body starts with an indentation and the first unindented line marks the end.

Python interprets non-zero values as True. None and 0 are interpreted as False.

Python if Statement Flowchart Flowchart of if statement in Python programming Flowchart of if statement in Python programming Example: Python if Statement

If the number is positive, we print an appropriate message
num = 3 if num > 0: print(num, "is a positive number.") print("This is always printed.")

num = -1 if num > 0: print(num, "is a positive number.") print("This is also always printed.") When you run the program, the output will be:

3 is a positive number This is always printed This is also always printed.

In the above example, num > 0 is the test expression.

The body of if is executed only if this evaluates to True.

When the variable num is equal to 3, test expression is true and statements inside the body of if are executed.

If the variable num is equal to -1, test expression is false and statements inside the body of if are skipped.

The print() statement falls outside of the if block (unindented). Hence, it is executed regardless of the test expression.

Python if...else Statement Syntax of if...else if test expression: Body of if else: Body of else

The if..else statement evaluates test expression and will execute the body of if only when the test condition is True.

If the condition is False, the body of else is executed. Indentation is used to separate the blocks.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://docs.github.com/categories/github-pages-basics/) or [contact support](https://github.com/contact) and we’ll help you sort it out.
