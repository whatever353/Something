
## Basic Calc ##

calc = input("Operator  + , - , * , /")


if calc <= "+":
    number1 = input("Number 1")
    number2 = input("Number 2")
    answer = float(number1) + float(number2)
    
elif calc <= "-":
    number1 = input("Number 1")
    number2 = input("Number 2")
    answer = float(number1) - float(number2)
    
elif calc == "*":
    op = "*"
    if op == "*":
        num1 = float(input("Number 1"))
        num2 = float(input("Number 2"))
        answer = float(num1) * float(num2)
        
elif calc <= "/":
    number1 = input("Number 1")
    number2 = input("Number 2")
    answer = float(number1) / float(number2)
    



print("The answer is")
print(answer) 




