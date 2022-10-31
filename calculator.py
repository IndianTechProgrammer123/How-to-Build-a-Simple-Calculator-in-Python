Num1 = int(input("Enter First Number : "))
Num2 = int(input("Enter Second Number : "))
op = input("Enter Operator [+ - * / %] : ")
result = 0

if op == '+':
    result = Num1 + Num2
elif op == '-':
    result = Num1 - Num2
elif op == '*':
    result = Num1 * Num2
elif op == '/':
    result = Num1 / Num2
elif op == '%':
    result = Num1 % Num2
else:
    print("InValid operator")
    
print(Num1,op,Num2,"=",result)