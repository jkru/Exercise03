"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""
import arithmetic

def main():
    # Your code goes here

    while True:
        user_input = raw_input("enter your function and numbers RPN style ")
        token = user_input.split()
        command = token[0]
        if command == "q":
            break
 
        if command == "+":
            print(arithmetic.add(float(token[1]), float(token[2])))
        elif command == "-":
            print(arithmetic.subtract(float(token[1]), float(token[2])))
        elif command == "*":
            print(arithmetic.multiply(float(token[1]), float(token[2])))
        elif command == "/":
            print(arithmetic.divide(float(token[1]), float(token[2])))
        elif command == "square":
            print(arithmetic.square(float(token[1])))
        elif command == "cube":
            print(arithmetic.cube(float(token[1])))
        elif command == "pow":
            print(arithmetic.power(float(token[1]), float(token[2])))
        elif command == "mod":
            print(arithmetic.mod(float(token[1]), float(token[2])))
        else:
            print "I don't understand."




if __name__ == '__main__':
    main()