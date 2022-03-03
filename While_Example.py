a = 10
b = 5
index = 0
while True:
    index = int(input("what example do you want to run? (0 ends the program)\n"))
    print("\n")

# Normal while loop
    if index == 1:
        while a > b:
            print("the first one is greater")
            b += 1

# While True Loop
    elif index == 2:
        add = 0

        while True:
            number = int(input("give me a number(0 to stop)"))
            add += number
            if number == 0:
                print("the sum is ",add)
                break

# for loop
    elif index == 3:
        greeting = "hello, how are you?"

        for letter in greeting:
            print(letter*2, end="")
        print()
        print(2*greeting)

# splitting strings
# 1 through 6
        print(greeting[1:6])
# 1 through end of string
        print(greeting[1:])
#
        print(greeting[2::2])

        print(greeting[::-1])
#
    elif index == 4:
        text = input("Type a palindrome without punctuation")
        text = text.replace(" ", "")
        print(text)

        reversed = text[::-1]
        print(reversed)
        if text == reversed:
            print("this is a palindrome")
        else:
            print("this is not a palindrome")

# end of examples
    elif index == 0:
        print("see you later")
        break
