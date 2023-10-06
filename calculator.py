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
answer = ""
while whileVariable == True:
    outputWanted = input("What function would you like to preform? ")
    outputWanted = outputWanted.lower()
    if (outputWanted.capitalize() == "Addition" ):
        if (answer == ""):
            num1 = input("What is the first number (of the two) you would like to add? ")
        else:
            num1 = input("What is the first number (of the two) you would like to add (If you would like to use the previous answer, leave this blank)? ")
        if (num1 == ""):
            num1 = answer
        num2 = input("What is the second number (of the two) you would like to add? ")
        answer = Addition(num1, num2)
        print(str(num1) + " + " + str(num2) + " = " + Addition(num1, num2))

    elif (outputWanted.capitalize() == "Subtraction" ):
        if (answer == ""):
            num1 = input("What is the first number (of the two) you would like to subtract? ")
        else:
            num1 = input("What is the first number (of the two) you would like to subtract (If you would like to use the previous answer, leave this blank)? ")
        if (num1 == ""):
            num1 = answer
        num2 = input("What is the second number (of the two) you would like to subtract? ")
        answer = Subtraction(num1, num2)
        print(str(num1) + " - " + str(num2) + " = " + Subtraction(num1, num2))

    elif (outputWanted.capitalize() == "Multiplication" ):
        if (answer == ""):
            num1 = input("What is the first number (of the two) you would like to multiply? ")
        else:
            num1 = input("What is the first number (of the two) you would like to multiply (If you would like to use the previous answer, leave this blank)? ")
        if (num1 == ""):
            num1 = answer
        num2 = input("What is the second number (of the two) you would like to multiply? ")
        answer = Multiplication(num1, num2)
        print(str(num1) + " x " + str(num2) + " = " + Multiplication(num1, num2))
    
    elif (outputWanted.capitalize() == "Division" ):
        if (answer == ""):
            num1 = input("What is the first number (of the two) you would like to divide? ")
        else:
            num1 = input("What is the first number (of the two) you would like to divide (If you would like to use the previous answer, leave this blank)? ")
        if (num1 == ""):
            num1 = answer
        num2 = input("What is the second number (of the two) you would like to divide? ")
        answer = Division(num1, num2)
        print(str(num1) + " / " + str(num2) + " = " + Division(num1, num2))

    elif (outputWanted.capitalize() == "Exponent" ):
        if (answer == ""):
            num1 = input("What is the base? ")
        else:
            num1 = input("What is the base? (If you would like to use the previous answer, leave this blank)? ")
        if (num1 == ""):
            num1 = answer
        num2 = input("What is the exponent? ")
        answer = Exponent(num1, num2)
        print(str(num1) + " ^ " + str(num2) + " = " + Exponent(num1, num2))

    elif (outputWanted.capitalize() == "Modulus" ):
        if (answer == ""):
            num1 = input("What is the first number (of the two) you would like to find the remainder of?")
        else:
            num1 = input("What is the first number (of the two) you would like to find the remainder of? (If you would like to use the previous answer, leave this blank)? ")
        if (num1 == ""):
            num1 = answer
        num2 = input("What is the second number (of the two) you would like to find the remainder of? ")
        answer = Mod(num1, num2)
        print(str(num1) + " % " + str(num2) + " = " + Mod(num1, num2) + "R") 

    elif (outputWanted.capitalize() == "Square root" ):
        if (answer == ""):
            num1 = input("What number would you like to find the sqaure root of? ")
        else:
            num1 = input("What number would you like to find the sqaure root of? (If you would like to use the previous answer, leave this blank)? ")
        if (num1 == ""):
            num1 = float(answer)
        num1 = float(num1)
        answer = math.sqrt(num1)
        print("√" + str(num1) + " = " + str(math.sqrt(num1))) 
    elif (outputWanted.capitalize() == "Log" ):
        if (answer == ""):
            num1 = input("What number would you like to log? ")
        else:
            num1 = input("What number would you like to log? (If you would like to use the previous answer, leave this blank)? ")
        if (num1 == ""):
            num1 = float(answer)
        num1 = float(num1)
        num2 = input("What is the base (optional)? ")
        if (str(num2) == ""):
            num2 = 10
        num2 = float(num2)
        answer = math.log(num1, num2)
        print("log(" + str(num1) + ")" + " = " + str(math.log(num1, num2))) 

    elif (outputWanted.capitalize() == "Natural log"):
        if (answer == ""):
            num1 = input("What number would you like to find the natural log of? ")
        else:
            num1 = input("What number would you like to find the natural log of? (If you would like to use the previous answer, leave this blank)? ")
        if (num1 == ""):
            num1 = float(answer)
        num1 = float(num1)
        answer = math.log(num1)
        print("ln(" + str(num1) + ")" + " = " + str(math.log(num1))) 
    
    elif (outputWanted.capitalize() == "Sin"):
        if (answer == ""):
            num1 = input("What number would you like to find the sin? ")
        else:
            num1 = input("What number would you like to find the sin? (If you would like to use the previous answer, leave this blank)? ")
        if (num1 == ""):
            num1 = float(answer)
        num1 = float(num1)
        answer = math.sin(num1)
        print("sin(" + str(num1) + ")" + " = " + str(math.sin(num1)))

    elif (outputWanted.capitalize() == "Tan"):
        if (answer == ""):
            num1 = input("What number would you like to find the tan? ")
        else:
            num1 = input("What number would you like to find the tan? (If you would like to use the previous answer, leave this blank)? ")
        if (num1 == ""):
            num1 = float(answer)
        num1 = float(num1)
        answer = math.tan(num1)
        print("tan(" + str(num1) + ")" + " = " + str(math.tan(num1)))

    elif (outputWanted.capitalize() == "Cos"):
        if (answer == ""):
            num1 = input("What number would you like to find the cos? ")
        else:
            num1 = input("What number would you like to find the cos? (If you would like to use the previous answer, leave this blank)? ")
        if (num1 == ""):
            num1 = float(answer)
        num1 = float(num1)
        answer = math.cos(num1)
        print("cos(" + str(num1) + ")" + " = " + str(math.cos(num1))) 
    
    #I do not need this because my variables reset every time the user preforms another function. I still added it though.
    elif (outputWanted.capitalize() == "Clear"):
        num1 = 0
        num2 = 0
        print("Cleared")
    #Also, I did not add paranthesis cause I do not need it the way my calculator is set up :)
    elif (outputWanted.capitalize() == "Exit"):
        print("Thank you for using this calculator!")
        break

