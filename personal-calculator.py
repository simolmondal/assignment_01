#Personal Information & Simple Calculator.
Name = input("Please, enter your name:")
Age = int(input("Please , enter your age:"))
print(f"Hello, {Name}!")
print(f"Your age is {Age}")

num1 = int(input("Enter Your First number:"))
num2 = int(input("Enter Your Second number:"))
a = input("Input your operation:")

if a== "+" :
    print(f"Addition: {num1+num2}")
elif a== "-":
    print(f"Subtraction: {num1-num2}")
elif a== "*":
    print(f"Multiplication: {num1*num2}")
elif a== "/":
    if num2!=0:
        print(f"Division: {num1/num2}")
    else :
        print("Can not Divide by zero.")
else:
    print("Please , Input Your Correct Operetor! Like +, -, *, /.")





Student Grade Calculator

 