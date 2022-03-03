try:
    age = input("How old are you? ")
    print("in 2032 you will be ", int(age)+10)
    print(100/int(age))

except ValueError:
    print("Hey, that is not a number")
except ZeroDivisionError:
    print("Hey, you are dividing by zero")
finally:
    print("This is what we do after all this is done")
    print("This will print no matter what the code above is")
