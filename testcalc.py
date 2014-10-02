"""
calculator.py

Using our morearithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""
import morearithmetic


def main():
    # Your code goes here

    while True:
        #uncomment the following three lines when not testing
        user_input = raw_input("enter your function and numbers RPN style ")
        token = user_input.split()

        command = token[0]

        operations = {'+': morearithmetic.add, '-': morearithmetic.subtract, 
        '*': morearithmetic.multiply, '/': morearithmetic.divide, 
        'square': morearithmetic.square, 'cube': morearithmetic.cube,
        'pow': morearithmetic.power, 'mod': morearithmetic.mod,
        'root': morearithmetic.root}

        if command == "q" or command == "quit" or command == "Q":
            break
        elif command in operations:
            print(operations[command](token))
        else:
            print "I don't understand. Here are some legit commands:"
            print "+ addition \t - subtraction \t * multiplication"
            print "/ division \t square n*n \t cube n*n*n"
            print "pow exponents \t mod modulo \t root nth root"


if __name__ == '__main__':
    main()