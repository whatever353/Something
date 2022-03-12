
## Basic Calc ##


calc = input("Operator  + , - , x , /")



if calc <= "+" and not (calc == "*"):
    number1 = input("Number 1")
    number2 = input("Number 2")
    answer = float(number1) + float(number2)
    
elif calc <= "-":
    number1 = input("Number 1")
    number2 = input("Number 2")
    answer = float(number1) - float(number2)
    
elif calc == "x" and not (calc == "+"):
    num1 = float(input("number 1"))
    num2 = float(input("Number 2"))
    answer = float(num1) * float(num2)
        
elif calc <= "/":
    number1 = input("Number 1")
    number2 = input("Number 2")
    answer = float(number1) / float(number2)
    



print("The answer is")
print(answer) 


