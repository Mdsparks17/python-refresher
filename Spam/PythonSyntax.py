class Chapter1:
    # Terminal Interaction
    # Printing
    print("hello, world!")
    # Input
    # myName = input("What is your name? ")

    # Primitives
    # Booleans: must be capitalized
    myBoolean = True
    myBoolean = False
    # Integers
    myInteger = 17
    # Float
    myFloat = 17.21

    # Composites
    # Strings: same data type for strings, chars, etc, strings are treated as arrays
    myString = "Michael Sparks"
    # List: python's implementation of arrays
    myArray = [1, 2, 3, 4]
    # Range: is an object that has numbers 0 to 4
    myRange = range(5)

    # Immutable Objects
    # Tuple
    myTuple = (1, 2, 3)
    
    # Operators
    # Arithmatic
    x = 1 + 2 - 3 * 4 / 5 % 6 ** 7
    # Assignment
    x = 1
    x += 2
    x -= 3
    # Comparison
    y = 1 > 2 < 3
    z = 3 <= 4 >= 5
    y = y == z != y
    # Logical Operators
    y = z and y
    y = not(z or y)
    # Identity Operator: checks if the object referenced is the same object, rather than content
    y = y is y
    y = y is not z
    # Membership Operator
    y = 2 in myArray

    # Type Conversion
    int()
    float()
    bool()
    str()

    # if statements
    if 21 > 17:
        print("21 is greater than 17")
    elif 21 < 17:
        print("21 is less than 21?")
    else:
        print("21 is equal to 21?")

    # while loop
    i = 0
    while i < 5:
        i += 1
    print(i)
    
    # for loop
    numbers = [1, 2, 3, 4, 5]
    for num in numbers:
        print(num)

    # List/Array tricks and quirks
    names = ["John", "Mary", "Joe", "Susan", "Sam"]
    print(names[0])
    print(names[-1])
    print(names[0:3])
    names.append("Sally")
    print(names)
    names.insert(0, "Fred")
    print(names)
    names.remove("Mary")
    print(names)
    # names.clear()
    print("Joe" in names)
    print(len(names))

    # Abstract data types
    # List
    # Map
    # Set
    # Stack
    # Queue
    # Graph 
