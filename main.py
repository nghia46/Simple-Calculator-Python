from calculator import Calculator

num1 = float(input("Enter num 1:"))
num2 = float(input("Enter num 2:"))
sign = input("Enter caculate type(+,-,*,/): ")

calculator = Calculator(num1, num2)

try:
    if sign == '+':
        result = calculator.add(num1,num2)
    elif sign == '-':
        result = calculator.subtract(num1,num2)
    elif sign == '*':
        result = calculator.multiply(num1,num2)
    elif sign == '/':
        result = calculator.divide(num1,num2)
    # Display result
    print(f"Result of {num1} {sign} {num2} = {result}")

except ValueError:
    print("Error")
except ZeroDivisionError:
    print("You can't devide for zero!")
