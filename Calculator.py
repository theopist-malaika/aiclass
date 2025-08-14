def calculator(num1,num2,operator):
operator=input("Enter an operator (+,-,*,/):")
num1=float(input("Enter the first number:"))
num2=float(input("Enter the second number:"))
print("Error: Invalid.Please enter a number.")
return
        
    if operator=="+":
     result=num1+num2
    elif operator=="-":
     result=num1-num2
    elif operator=="*":
    result=num1*num2
    elif operator=="/":
     result=num1/num2


    
