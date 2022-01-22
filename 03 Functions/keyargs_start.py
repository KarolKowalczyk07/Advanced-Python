# Demonstrate the use of keyword-only arguments


# use keyword-only arguments to help ensure code clarity (only call function if you know how to use it, hence keyword)
def myFunction(arg1, arg2, *, suppressExceptions=False):
    # the * is not an argument, its job is to separate positional arguments from keywords arguments
    # hence myFunction still takes 3 arguments, the 3rd being the keyword
    pass


def main():
    # try to call the function without the keyword
    myFunction(1, 2,suppressExceptions= True)


if __name__ == "__main__":
    main()
