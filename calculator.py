def calculate(expression):
    # Удаляем пробелы
    expression = expression.replace(' ', '')

    n = len(expression)
    if n == 0:
        return 0

    current_number = 0
    last_operator = '+'
    stack = []

    for i in range(n):
        char = expression[i]

        if char.isdigit():
            current_number = current_number * 10 + int(char)  # Собираем число

        # Если текущий символ не число или мы достигли конца строки
        if not char.isdigit() or i == n - 1:
            if last_operator == '+':
                stack.append(current_number)
            elif last_operator == '-':
                stack.append(-current_number)
            elif last_operator == '*':
                stack[-1] *= current_number
            elif last_operator == '/':
                # Используем целочисленное деление с округлением
                stack[-1] = int(stack[-1] / current_number)

            last_operator = char
            current_number = 0  # Сбрасываем текущее число

    return sum(stack)  # Возвращаем сумму всех элементов в стеке


# Пример использования
expression = "3 + 5 * 2 - 8 / 4"
result = calculate(expression)
print("Результат:", result)
