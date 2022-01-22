# Demonstrate the use of variable argument lists


# TODO: define a function that takes variable arguments
def addition(*args):        # * in front of arguments gives variable number of arguments
    result = 0
    for arg in args:
        result += arg
    return result


def main():
    # TODO: pass different arguments
    print(addition(5,10,15,20))
    print(addition(-1,0,20,195,-569,333))

    # TODO: pass an existing list
    myNums = [5, 10, 15, 20]
    print(addition(*myNums))


if __name__ == "__main__":
    main()
