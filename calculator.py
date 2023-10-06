import math
def Addition (num1, num2):
    value = float(num1) + float(num2)
    return str(value)
def Subtraction (num1, num2):
    value1 = float(num1) - float(num2)
    return str(value1)
def Multiplication (num1, num2):
    value2 = float(num1) * float(num2)
    return str(value2)
def Division (num1, num2):
    value3 = float(num1) / float(num2)
    return str(value3)
def Exponent (num1, num2):
    value4 = float(num1) ** float(num2)
    return str(value4)
def Mod (num1, num2):
    value5 = float(num1) % float(num2)
    return str(int(value5))
whileVariable = True
while whileVariable == True:
    outputWanted = input("What function would you like to preform? ")
    outputWanted = outputWanted.lower()
    if (outputWanted.capitalize() == "Addition" ):
        num1 = input("What is the first number (of the two) you would like to add? ")
        num2 = input("What is the second number (of the two) you would like to add? ")
        print(num1 + " + " + num2 + " = " + Addition(num1, num2))

    elif (outputWanted.capitalize() == "Subtraction" ):
        num1 = input("What is the first number (of the two) you would like to subtract? ")
        num2 = input("What is the second number (of the two) you would like to subtract? ")
        print(num1 + " - " + num2 + " = " + Subtraction(num1, num2))

    elif (outputWanted.capitalize() == "Multiplication" ):
        num1 = input("What is the first number (of the two) you would like to multiply? ")
        num2 = input("What is the second number (of the two) you would like to multiply? ")
        print(num1 + " x " + num2 + " = " + Multiplication(num1, num2))

    elif (outputWanted.capitalize() == "Exponent" ):
        num1 = input("What is the base? ")
        num2 = input("What is the exponent? ")
        print(num1 + " ^ " + num2 + " = " + Exponent(num1, num2))

    elif (outputWanted.capitalize() == "Modulus" ):
        num1 = input("What is the first number (of the two) you would like to find the remainder of? ")
        num2 = input("What is the second number (of the two) you would like to find the remainder of? ")
        print(num1 + " % " + num2 + " = " + Mod(num1, num2) + "R") 

    elif (outputWanted.capitalize() == "Square root" ):
        num1 = input("What is number would you like to find the sqaure root of? ")
        num1 = int(num1)
        print("√" + str(num1) + " = " + str(math.sqrt(num1))) 
    elif (outputWanted.capitalize() == "Log" ):
        num1 = input("What is the number you would like to Log? ")
        num1 = int(num1)
        num2 = input("What is the base (optional)? ")
        if (str(num2) == ""):
            num2 = 10
        num2 = int(num2)
        print("log(" + str(num1) + ")" + " = " + str(math.log(num1, num2))) 

    elif (outputWanted.capitalize() == "Natural log"):
        num1 = input("What is the number you would like to find the natural log of? ")
        num1 = int(num1)
        print("ln(" + str(num1) + ")" + " = " + str(math.log(num1))) 
    
    elif (outputWanted.capitalize() == "Sin"):
        num1 = input("What number would you like to find the sin of? ")
        num1 = int(num1)
        print("sin(" + str(num1) + ")" + " = " + str(math.sin(num1)))

    elif (outputWanted.capitalize() == "Tan"):
        num1 = input("What number would you like to find the tan of ")
        num1 = int(num1)
        print("tan(" + str(num1) + ")" + " = " + str(math.tan(num1)))

    elif (outputWanted.capitalize() == "Cos"):
        num1 = input("What number would to find the cos of? ")
        num1 = int(num1)
        print("cos(" + str(num1) + ")" + " = " + str(math.cos(num1))) 
    
    #I do not need this because my variables reset every time the user preforms another function. I still added it though.
    elif (outputWanted.capitalize() == "Clear"):
        num1 = 0
        num2 = 0
        print("Cleared")

