print("All done") 
print ("select an operation")
print ("1 add")
print ("2 subtract")
print ("3 Multiplication")
print ("4 division")
operation = int(input())
if operation == 1:
    num1 = int(input("first number"))
    num2 = int(input("second number"))
    answer = num1 + num2
    print (answer)
elif operation == 2:
    num1 = int(input("first number"))
    num2 = int(input("second number"))
    answer1 = num1 - num2
    print (answer1)
elif operation == 3:
    num1 = int(input("first number"))
    num2 = int(input("second number"))
    answer2 = num1 * num2
    print (answer2)
elif operation == 4:
    num1 = int(input("first number"))
    num2 = int(input("second number"))
    answer3 = num1 / num2
    print (answer3)
else:
    print ("invalid user input")

            
