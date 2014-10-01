def add(token):
    tot = 0
    for i in range(1,len(token)):
        tot = tot + float(token[i]) 
    return tot

def subtract(token):
    tot = float(token[1])
    for i in range(2,len(token)):
        print(tot)
        tot = tot - float(token[i]) 
    return tot

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return float(num1) / float(num2)

def square(num1):
    return num1*num1

def cube(num1):
    return num1 ** 3

def power(num1, num2):
    return num1**num2

def mod(num1, num2):
    return num1 % num2
