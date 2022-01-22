# deque objects are like double-ended queues
# can append or remove from left or right sides and rotate

import collections
import string


def main():
    
    # TODO: initialize a deque with lowercase letters
    d = collections.deque(string.ascii_lowercase)

    # TODO: deques support the len() function
    print("Item count: ", str(len(d)))

    # TODO: deques can be iterated over
    #for elem in d:
        #print(elem.upper(), end=",")

    # TODO: manipulate items from either end
    d.pop()
    d.popleft()
    d.append(2)
    d.appendleft(1)
    #print(d)

    # TODO: rotate the deque
    print(d)
    d.rotate(10)                # takes the last 10 values and puts them in the front
    print(d)

    # to operate on both ends of a list, or move items in a list, USE A DEQUE!



if __name__ == "__main__":
    main()
