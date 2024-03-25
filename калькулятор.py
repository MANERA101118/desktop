num1 = float(input("Введите первое число: "))
operator = input("Введите оператор (+, -, *, /): ")
num2 = float(input("Введите второе число: "))

if operator == '+':
        result = num1 + num2
elif operator == '-':
        result = num1 - num2
elif operator == '*':
        result = num1 * num2
elif operator == '/':
        if num2 == 0:
            result = "Ошибка: деление на ноль"
        else:
            result = num1 / num2
else:
        result = "Ошибка: некорректный оператор"

print("Результат: ", result
