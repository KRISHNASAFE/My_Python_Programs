'''
#Addition Program

x = input("Enter a number: ")
y = input("Enter another number: ")

z = int(x) + int(y)

print("Sum of", x, "and", y, "is:", z)


# Subtraction Program

x = input("Enter a number: ")
y = input("Enter another number: ")

z = int(x) - int(y)

print("Subtraction of", x, "and", y, "is:", z)


# Multiplication Program
x = input("Enter a number: ")
y = input("Enter another number: ")

z = int(x) * int(y)

print("Multiplication of", x, "and", y, "is:", z)


# Division Program

x = input("Enter a number: ")
y = input("Enter another number: ")

z = int(x) / int(y)

print("Division of", x, "and", y, "is:", z)
'''

'''
# Calculator Program using switch

print("Enter your choice: 1.Addition 2.Subtraction 3.Multiplication 4.Division ")
ch = input("Enter your choice:")
# print(ch)

x = input("Enter a number:")
y = input("Enter another number:")


def switch(ch):
    if ch == 1:
        return int(x) + int(y)
    if ch == 2:
        return int(x) - int(y)


print(switch(ch))
'''

'''
Calculator using function :


def add(num1, num2):
    print("Sum of entered numbers is:", int(num1) + int(num2))


def sub(num1, num2):
    return print("Subtraction of entered numbers is:", int(num1) - int(num2))


def multi(num1, num2):
    return print("Multiplication of entered numers is:", int(num1) * int(num2))


def div(num1, num2):
    return print("Division of entered numbers is:", int(num1) / int(num2))


print("Enter your choice: 1.Addition 2.Subtraction 3.Multiplication 4.Division")
ch = input("Enter your choice:")
print(ch)
x = input("Enter a number: ")
y = input("Enter another number: ")

if ch == '1':
    add(x, y)
elif ch == '2':
    sub(x, y)
elif ch == '3':
    multi(x, y)
elif ch == '4':
    div(x, y)
    
'''
