# advanced iteration functions in the itertools package
import itertools

def testFunction(x):
    return x < 40


def main():
    # TODO: cycle iterator can be used to cycle over a collection
    seq1 = ["Joe", "John", "Mike"]
    cycle1 = itertools.cycle(seq1)          # cycles through an array
    # print(next(cycle1))
    # print(next(cycle1))
    # print(next(cycle1))
    # print(next(cycle1))

    # TODO: use count to create a simple counter
    count = itertools.count(100,10)     # adds 10 to starting number (100)
    # print(next(count))
    # print(next(count))
    # print(next(count))

    # TODO: accumulate creates an iterator that accumulates values
    vals = [10,20,30,40,50,40,30]
    # acc = itertools.accumulate(vals,max)        # pins (stops) at max value
    # print(list(acc))
            
    # TODO: use chain to connect sequences together
    x = itertools.chain("ABCD", "1234")
    print(list(x))                              # puts two strings in a list, seperated by character
    
    # TODO: dropwhile and takewhile will return values until
    # a certain condition is met that stops them
    print("testFunction is true when x < 40")
    print("dropwhile: ", list(itertools.dropwhile(testFunction, vals)))    # drop values from sequence while testFunction returns true
    print("takewhile: ", list(itertools.takewhile(testFunction, vals)))    # returns values from sequence while testFunction returns true
    
    # testFunction is true when x < 40
    
if __name__ == "__main__":
    main()
    