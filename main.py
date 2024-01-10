# function to add two numbers

def add_two_numbers(x, y):
    return x + y

while True:
    try:
        userInumputX = float(input("Enter the first number: "))
        userInumputY = float(input("Enter the second number: "))
    except ValueError:
        print("Enter a number")
    finally:
        print(add_two_numbers(userInumputX, userInumputY))

