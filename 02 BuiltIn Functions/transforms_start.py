# use transform functions like sorted, filter, map


def filterFunc(x):
    if x % 2 == 0:
        return False    # even number
    return True         # odd number


def filterFunc2(x):
    if x.isupper():
        return False    # false for uppercase letters
    return True         # true for lowercase letters


def squareFunc(x):
    return x**2


def toGrade(x):
    if (x >= 90):
        return "A"
    elif (x >= 80 and x < 90):
        return "B"
    elif (x >= 70 and x < 80):
        return "C"
    elif (x >= 65 and x < 70):
        return "D"
    return "F"


def main():
    # define some sample sequences to operate on
    nums = (1, 8, 4, 5, 13, 26, 381, 410, 58, 47)
    chars = "abcDeFGHiJklmnoP"
    grades = (81, 89, 94, 78, 61, 66, 99, 74)

    # TODO: use filter to remove items from a list
    odds = list(filter(filterFunc, nums))       # filterFunc returns True for odd #'s, filtering gets rid of even number in odds
    #print(odds)

    # TODO: use filter on non-numeric sequence
    lowers = list(filter(filterFunc2, chars))
    #print(lowers)                               # filters out uppercase letters

    # TODO: use map to create a new sequence of values
    squares = list(map(squareFunc, nums))
    print(squares)

    # TODO: use sorted and map to change numbers to grades
    #grades = sorted(grades)    
    # use sorted() to sort grades from lowest to greatest, if exact order is wanted dont sort them
    letters = list(map(toGrade, grades))
    print(letters)


if __name__ == "__main__":
    main()
