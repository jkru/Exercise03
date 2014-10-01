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

#temporary test code

#        listofcommands = ["+","-","*","/ ","square","cube","pow","mod"]
#        for com in listofcommands:
#            token = test_this_calc(listofcommands)


        if command == "q" or command == "quit" or command == "Q":
            break
        elif command == "+":
            print(morearithmetic.add(token))
        elif command == "-":
            print(morearithmetic.subtract(token))
        elif command == "*":
            print(morearithmetic.multiply(token))
        elif command == "/":
            print(morearithmetic.divide(token))
        elif command == "square":
            print(morearithmetic.square(float(token[1])))
        elif command == "cube":
            print(morearithmetic.cube(float(token[1])))
        elif command == "pow":
            print(morearithmetic.power(token))
        elif command == "mod":
            print(morearithmetic.mod(float(token[1]), float(token[2])))
        elif command == "root":
            print(morearithmetic.root(token))
        else:
            print "I don't understand. Here are some legit commands:"
            print "+ addition \t - subtraction \t * multiplication"
            print "/ division \t square n*n \t cube n*n*n"
            print "pow exponents \t mod modulo \t root nth root"



if __name__ == '__main__':
    main()