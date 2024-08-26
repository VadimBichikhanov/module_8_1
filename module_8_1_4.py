def add_everything_up(a, b):
    try:
        # Пытаемся преобразовать аргументы в числа
        a_num = float(a)
        b_num = float(b)
        
        # Складываем числа
        result = a_num + b_num
        
        # Округляем результат до 3 знаков после запятой
        return round(result, 3)
    
    except (ValueError, TypeError):
        # Если хотя бы один из аргументов не является числом, возвращаем их строковое представление
        return f"{a}{b}"

# Примеры использования функции
print(add_everything_up(123.456, 'строка'))  # 123.456строка
print(add_everything_up('яблоко', 4215))    # яблоко4215
print(add_everything_up(123.456, 7))        # 130.456
