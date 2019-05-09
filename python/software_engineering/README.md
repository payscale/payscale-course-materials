# Software Engineering with Python

## Introduction to Object-Oriented Programming - Animal class in `oop.py`
- Class syntax
- The `self` parameter
- Method syntax
- Instance Variables
- Inheritance
- Class Variables
- [DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself) (Don't Repeat Yourself)
- The [diamond](https://en.wikipedia.org/wiki/Multiple_inheritance#The_diamond_problem) problem

## "Build a Library" `lib.py`, `user.py`, `test_lib.py`
- [Data Structures](https://en.wikipedia.org/wiki/Data_structure)
- "What is an [API](https://en.wikipedia.org/wiki/Application_programming_interface)?"
- Implement a data structure
- Import and use the data structure in a cient module
- Defensive programming
    - Raising [Exceptions](https://docs.python.org/3/library/exceptions.html)
    - Catching Exceptions
    - Custom Exceptions
- The [Python Data Model](https://docs.python.org/3/reference/datamodel.html)
    - "Dunder" protocol methods
        - `__len__`
        - `__repr__`
- Writing tests
    - The `unnittest` [module](https://docs.python.org/3/library/unittest.html)
        - As an alternative to `unnittest`, [pytest](https://docs.pytest.org/en/latest/) is a popular third party library
    - Write tests for `lib.py` in `test_lib.py`
- Code Documentation
    - We'll document our new libarary
    - Module docs
    - Class docs
    - Method docs
    - Code comments
- Refactor
    - Add a base `Sequence` to factor out common functionality
    - Show the value of tests

## Contribute to a shared code base
- Git and version control
- Maker sure tests pass
- Branching
- Pull requests and code review
