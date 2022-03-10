a = 10
b = 5
index = 0
while True:
    index = int(input("what example do you want to run? (0 ends the program)\n"))

# Normal while loop
    if index == 1:
        while a > b:
            print("a is greater")
            print("b = ", b)
            b += 1

# While True Loop
    elif index == 2:

        add = 0
        while True:
            number = int(input("give me a number to add to the running sum (0 to stop)"))
            add += number
            if number == 0:
                print("the sum is ", add, "\n")
                break

# for loop
    elif index == 3:
        greeting = "Hello, how are you?"
        print("this is the string\n", greeting, "\n")

        print("Doubling each letter by multiplying each letter by 2")
        for letter in greeting:
            print(letter*2, end="")
        print("\n")

        print("multiply the string greeting by 2")
        print(2*greeting, "\n")

# string/list selection
        # 1 through 6
        print("1 through 6")
        # python is a base 0 language so the h in "hello" is 0 and the ending index will not be included
        print(greeting[1:6], "\n")

        # 1 through end of string
        print("1 through end of string")
        print(greeting[1:], "\n")

        # greeting [start : end : step]
        print("greeting [start : end : step]")
        print(greeting[2::2], "\n")
        # if [::-1] then the string is reversed
        print(greeting[::-1])

# String manipulation
    elif index == 4:
        text = input("Type a palindrome without punctuation")
        text = text.replace(" ", "")
        print(text)

        reverse = text[::-1]
        print(reverse)
        if text == reverse:
            print("this is a palindrome")
        else:
            print("this is not a palindrome")

# try, except and finally functions
    elif index == 5:
        print("Type anything to see how this code responds to errors, its expecting a non 0 integer \n")
        try:
            age = input("How old are you? ")
            print("in 2032 your age  will be ", int(age) + 10, "\n")
            print("this is your age divided by 100", 100 / int(age), "\n")

        except ValueError:
            print("Hey, that is not a number!! \n")
            print("type 5 to try again you typed a string!\n")
        except ZeroDivisionError:
            print("Hey, you are dividing by zero!! \n")
            print("type 5 to try again you divided by zero\n")
        finally:
            print("This will print no matter what the code above is, even if there is an error\n")

# list comprehension
    elif index == 6:
        # lists use brackets
        numbers = [2, 6, 7]

        my_squares = [i ** 2 for i in numbers]

        print(my_squares)

# sets
    elif index == 7:

        myset = {1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3}

        # the set only prints unique values
        print(myset)

        myset = {3.14, 2, "hello", (1, 2, 3)}

        print(myset)

        try:
            myset = {3.14, 2, "hello", [1, 2, 3]}
        except TypeError:
            print("in myset = {3.14, 2, ""hello"", [1, 2, 3]} dictionaries "
                  "cannot print hashable objects, so a tuple won't print\n")

        # dictionaries cannot print hashable objects, so a tuple won't print
        # print(myset_2)

        set_A = {1, 2, 3, 4, 5, 9, 3}
        print("set a", set_A, "\n")
        set_B = {1, 3, 6, 4, 2, 1, 3}
        print("set b", set_B, "\n")

        # union:or
        print("union:or")
        print(set_B | set_A)
        print(set_B.union(set_A), "\n")

        # intersection
        print("intersection")
        print(set_A & set_B)
        print(set_A.intersection(set_B), "\n")

        # difference
        print("difference")
        print(set_A - set_B)
        print(set_B - set_A)

        # symmetric difference
        print("symmetric difference")

        print(set_A ^ set_B)


# String methods
    elif index == 8:
        s = "hello world my name is john"
        print(s)
        print(s.capitalize())
        print(s.center(40))
        print(s.count(" "))
        print(s.replace(" ", "!!"))
        print(s.split())

    elif index == 9:
        s = "http://google.com and then there could be http://yahoo.com or even a website like http://bbc.co.uk"
        start = 0
        while True:
            start = s.find("http://", start)
            if start == -1:
                break
            end = s.find(" ", start)
            if end == -1:
                print(s[start:])
                break

            print(s[start:end])
            start = end

# f string
    elif index == 10:
        # old way/normal string
        print("1 + 2", 1+2)
        # New way
        print(f"1 + 2 = {1+2}")
        a = 3
        b = 7
        name = input("what is your name")
        print(f"Dear {name.capitalize()}, 1+2 = {b**a}")
    # Files
    elif index == 11:
        try:
            filename = "text.txt"
            fp = open(filename, "r")  # second argument default is open for reading
            print(fp.read())
            print()
            fp.close()
        except FileNotFoundError:
            print("No such file or directory: 'text.txt'")

            with open("filename", "a") as fp:
                for line in fp:
                    print(f"Line: {line}")
                    # at the end, the file will be closed automatically

    elif index == 12:
        filename = "example.txt"
        palindrome_file = "palindromes.txt"
        non_palindrome_file = "non_palindromes.txt"
        punctuation = " .,?!'"

        open(palindrome_file, "w")
        open(non_palindrome_file, "w")

        with open(filename) as fp:
            # 2 read line by line
            for line in fp:
                # save original line
                orig_line = line.rstrip()
                # need to sanitize the line by removing punctuation
                line = line.lower()
                for p in punctuation:
                    line = line.replace(p, "")
                print(line)
                line = line.rstrip()  # this removes the enter at the end
                # check if palindrome
                if line == line[::-1]:
                    print(f"{orig_line} is a palindrome")
                    with open(palindrome_file, "a") as palindrome_fp:
                        palindrome_fp.write(f"{orig_line}\n")
                else:

                    print(f"{line} is not a palindrome")
                    with open(non_palindrome_file, "a") as non_palindrome_fp:
                        non_palindrome_fp.write(f"{orig_line}\n")
                # line = line.replace([i for i in punctuation], "")

# end of examples
    elif index == 0:
        print("see you later")
        break
