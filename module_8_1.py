def add_everything_up(a, b):
    # Проверяем, являются ли оба аргумента числами
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        result = a + b
        # Округляем результат до 3 знаков после запятой, если это число с плавающей точкой
        if isinstance(result, float):
            return round(result, 3)
        return result
    # Если хотя бы один из аргументов не является числом, возвращаем их строковое представление
    else:
        return f"{a}{b}"

# Примеры использования функции
print(add_everything_up(123.456, 'строка'))  # 123.456строка
print(add_everything_up('яблоко', 4215))    # яблоко4215
print(add_everything_up(123.456, 7))        # 130.456