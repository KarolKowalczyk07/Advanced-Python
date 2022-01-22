# Demonstrate the use of function docstrings


def myFunction(arg1, arg2=None):
    # create a DOCUMENTATION STRING, use triple quotes
    # first line summarizes functionality
    # modules: list important classes, functions, exceptions
    # classes: list important methods
    # functions: list parameters and explain each, list return value, list raised exceptions

    """myFunction(arg1, arg2=None) --> doesn't do anything, just prints.

    Parameters:
    arg1: the first argument
    arg2: second argument. Defaults to None.

    """
    print(arg1, arg2)


# calls documentation string
def main():
    print(myFunction.__doc__)


if __name__ == "__main__":
    main()
