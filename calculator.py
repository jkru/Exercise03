"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""
import arithmetic

def main():
    while True:
        user_input = raw_input("enter your function and numbers RPN style")
        tokens = user_input.split()
        print(user_input)


    # Your code goes here
    pass


if __name__ == '__main__':
    main()