import re
import pyinputplus as pyip
from pathlib import Path
import os
import shutil
import zipfile

class Chapter1to4:
    # # Terminal Interaction
    # # Printing
    print("Chapter 1-4")
    # # Input
    # # myName = input("What is your name? ")

    # # Primitives
    # # Booleans: must be capitalized
    # myBoolean = True
    # myBoolean = False
    # # Integers
    # myInteger = 17
    # # Float
    # myFloat = 17.21

    # # Composites
    # # Strings: same data type for strings, chars, etc, strings are treated as arrays
    # myString = "Michael Sparks"
    # # List: python's implementation of arrays
    # myArray = [1, 2, 3, 4]
    # # Range: is an object that has numbers 0 to 4
    # myRange = range(5)

    # # Immutable Objects
    # # Tuple
    # myTuple = (1, 2, 3)
    
    # # Operators
    # # Arithmatic
    # x = 1 + 2 - 3 * 4 / 5 % 6 ** 7
    # # Assignment
    # x = 1
    # x += 2
    # x -= 3
    # # Comparison
    # y = 1 > 2 < 3
    # z = 3 <= 4 >= 5
    # y = y == z != y
    # # Logical Operators
    # y = z and y
    # y = not(z or y)
    # # Identity Operator: checks if the object referenced is the same object, rather than content
    # y = y is y
    # y = y is not z
    # # Membership Operator
    # y = 2 in myArray

    # # Type Conversion
    # int()
    # float()
    # bool()
    # str()

    # # if statements
    # if 21 > 17:
    #     print("21 is greater than 17")
    # elif 21 < 17:
    #     print("21 is less than 21?")
    # else:
    #     print("21 is equal to 21?")

    # # while loop
    # i = 0
    # while i < 5:
    #     i += 1
    # print(i)
    
    # # for loop
    # numbers = [1, 2, 3, 4, 5]
    # for num in numbers:
    #     print(num)

    # for index, num in enumerate(numbers):
    #     print(str(index) + " : " + str(num))

    # # List/Array tricks and quirks
    # names = ["John", "Mary", "Joe", "Susan", "Sam"]
    # print(names[0])
    # print(names[-1])
    # print(names[0:3])
    # names.append("Sally")
    # print(names)
    # names.insert(0, "Fred")
    # print(names)
    # names.remove("Mary")
    # print(names)
    # # names.clear()
    # print("Joe" in names)
    # print(len(names))
    # # Multiple Assignments in 1 line
    # cat = ['fat', 'gray', 'loud']
    # size, color, disposition = cat

    # # Global
    # def spam():
    #     global eggs
    #     eggs = 'spam'
    # eggs = 'global'
    # spam()
    # print(eggs) # Expect 'spam' with no errors

    # # Exception Handling
    # def spam(divideBy):
    #     try:
    #         return 42 / divideBy
    #     except ZeroDivisionError:
    #         print('Error: Invalid argument.')

    # print(spam(2))
    # print(spam(12))
    # print(spam(0)) # Expect exception
    # print(spam(1)) # Continues to execute

    # # Random
    # import random
    # random.shuffle(numbers)
    # print(numbers)

    # # String editing
    # myName = "Michael Sparks"
    # myNewName = myName[0:7] + " Dillon" + myName[7:14]
    # print(myNewName)

    # # Handling list copies
    # import copy
    # colors = ['red', 'blue', 'yellow']
    # myColors = copy.copy(colors)
    # myColors[0] = 'purple'
    # print(colors)
    # print(myColors)

class Chapter5:
    # Dictionary
    print('Chapter 5')
    # myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
    # print(myCat['size'])
    # print(list(myCat))

    # # for k in myCat.keys():
    # #     print(k)
    
    # # for k in myCat.values():
    # #     print(k)

    # # for k in myCat.items():
    # #     print(k)

    # myLookup = 'color' in myCat
    # myLookup = 'color' in myCat.keys() # Same as previous line
    # myLookup = 'fat' in myCat.values()
    # myLookup = 'fat' not in myCat
    # # You can set a default response if it is not in the dictionary
    # print('my cat is ' + myCat.get('color', 'an unknown color') )

class Chapter6:
    # String Manipulation
    print('Chapter 6')
    # # Double quotes as the standard so you can use '
    # spam = "That is Michael's"
    # # Escape Characters
    # spam = 'That is Michael\'s'
    # # Print it raw with r
    # print(r'That is Carol\'s cat.') # That is Carol\'s cat.
    # # Multilines
    # print('''Dear Alice,

    # Eve's cat has been arrested for catnapping, cat burglary, and extortion.

    # Sincerely,
    # Bob''')
    # # useful methods
    # spam.upper()
    # spam.lower()
    # spam.islower()
    # spam.isupper()
    # spam.isalpha() # consists of letters and is not blank
    # spam.isalnum() # consists only of letters and numbers and is not blank
    # spam.isdecimal() # consists of numbers and is not blank
    # spam.isspace() # consists of only spaces, tabs, newlines, and is not empty
    # spam.istitle() # has a capital first letter and lower case for the rest
    # spam.startswith('That')
    # spam.endswith("Michael's")
    # ', '.join(['Michael', 'Sparks']) # Michael, Sparks
    # 'Michael, Sparks'.split(', ') #['Michael', 'Sparks']
    # 'Hello, world!'.partition('w') # ('Hello, ', 'w', 'orld!')
    # 'Hello'.rjust(10) # '     Hello'
    # 'Hello'.ljust(10) # 'Hello     '
    # spam.strip() # gets rid of leading and trailing white space

class Chapter7:
    # Regex
    print('Chapter 7')

    # # Identify a phone number with regex
    # def contains_phone_number(text):
    #     pattern = re.compile(r'(\+?\d{1,2})?[\s.-]?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}')
    #     return bool(pattern.search(text))

    # # Test cases
    # print(contains_phone_number("Call me at (123) 456-7890"))  # True
    # print(contains_phone_number("My number is 123-456-7890"))  # True
    # print(contains_phone_number("Reach me at 123.456.7890"))   # True
    # print(contains_phone_number("Here is the number: 1234567890"))  # True
    # print(contains_phone_number("Dial +31636363634"))          # True
    # print(contains_phone_number("My office number is 075-63546725"))  # True
    # print(contains_phone_number("No phone number here"))       # False

    # # Identify an email address with  regex
    # def contains_email(text):
    #     pattern = re.compile(
    #         r'[\w\.-]+@[\w\.-]+\.\w+'
    #     )
    #     return bool(pattern.search(text))

    # # Test cases
    # print(contains_email("Contact me at john.doe@example.com"))  # True
    # print(contains_email("My email is jane_doe123@domain.co.uk"))  # True
    # print(contains_email("Send an email to test.email@sub.domain.com"))  # True
    # print(contains_email("No email here"))  # False
    # print(contains_email("Invalid email @example.com"))  # False

class Chapter8:
    # Validating inputs
    print('Chapter 8')

    # response = pyip.inputEmail(prompt="Enter your email address: ")
    # print(f"Your email address is {response}")

class Chapter9:
    # Reading and writing to files
    print('Chapter 9')

    # # Pathing
    # myPath = Path('spam', 'bacon', 'eggs')
    # print(myPath) # spam\bacon\eggs
    # # making a full path
    # myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
    # for filename in myFiles:
    #     print(Path(r'C:\Users\Al', filename))
    # Path('spam') / 'bacon' / 'eggs' # WindowsPath('spam/bacon/eggs')
    # # Current working directory
    # Path.cwd()
    # # Change CWD
    # # >>> from pathlib import Path
    # # >>> import os
    # # >>> Path.cwd()
    # # WindowsPath('C:/Users/Al/AppData/Local/Programs/Python/Python37')'
    # # >>> os.chdir('C:\\Windows\\System32')
    # # >>> Path.cwd()
    # # WindowsPath('C:/Windows/System32')

    # # Home Directory
    # Path.home()
    # #  make new directory
    # # os.makedirs('C:\\delicious\\walnut\\waffles')

    # # >>> p = Path('C:/Users/Al/spam.txt')
    # # >>> p.anchor
    # # 'C:\\'
    # # >>> p.parent # This is a Path object, not a string.
    # # WindowsPath('C:/Users/Al')
    # # >>> p.name
    # # 'spam.txt'
    # # >>> p.stem
    # # 'spam'
    # # >>> p.suffix
    # # '.txt'
    # # >>> p.drive
    # # 'C:'

    # # Path Validation
    # myPath.exists()
    # myPath.is_file()
    # myPath.is_dir()

    # # p = Path('spam.txt')
    # # p.write_text('Hello, world!')
    # # print(p.read_text())

    # spamFile = open('spam.txt', 'w')
    # spamFile.write('Hello, world!\n')
    # spamFile.close()

    # spamFile = open('spam.txt', 'a')
    # spamFile.write('Hello again')
    # spamFile.close()

    # spamFile = open('spam.txt')
    # mySpamContent = spamFile.read()
    # spamFile.close()
    # print(mySpamContent)

class Chapter10: 
    # Organizing Files
    print('Chapter 10')

    p = Path.home()
    shutil.copytree(p / 'spam', p / 'spam_backup')
    shutil.move('C:\\bacon.txt', 'C:\\eggs\\new_bacon.txt')

    for filename in Path.home().glob('*.rxt'):
        #os.unlink(filename)
        print(filename)

    # Walking a directory
    for folderName, subfolders, filenames in os.walk('C:\\delicious'):
        print('The current folder is ' + folderName)

    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)

    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': '+ filename)

    print('')

    # Zip files
    # Extracting (not within python, into the target directory)
    p = Path.home()
    exampleZip = zipfile.ZipFile(p / 'example.zip')
    exampleZip.extract('spam.txt', 'C:\\some\\new\\folders')
    exampleZip.close()

    # Making a new zip file
    newZip = zipfile.ZipFile('new.zip', 'w')
    newZip.write('spam.txt', compress_type=zipfile.ZIP_DEFLATED)
    newZip.close()

