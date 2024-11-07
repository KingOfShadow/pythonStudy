import calculator

a = int(input("Введіть 1 число"))
b = int(input("Введіть 2 число"))
s = input("Введіть дію")

if s == 'add':
    calculator.add(a, b)
if s == 'subtract':
    calculator.subtract(a, b)
if s == 'multiply':
    calculator.multiply(a, b)
if s == 'divide':
    calculator.divide(a, b)


