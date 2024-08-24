class InvalidArgumentError(Exception):
    """
    Пользовательское исключение, которое вызывается, когда один или оба аргумента не являются числами.
    """
    def __init__(self, message="Один или оба аргумента не являются числами"):
        self.message = message
        super().__init__(self.message)

def add_everything_up(a, b):
    """
    Функция для сложения двух аргументов.
    Если оба аргумента являются числами, возвращает их сумму, округленную до 3 знаков после запятой, если это необходимо.
    Если хотя бы один из аргументов не является числом, возвращает их строковое представление.
    """
    try:
        # Проверяем, являются ли оба аргумента числами
        if not all(isinstance(x, (int, float)) for x in (a, b)):
            raise InvalidArgumentError
        
        # Складываем аргументы
        result = a + b
        
        # Округляем результат до 3 знаков после запятой, если это число с плавающей точкой
        return round(result, 3) if isinstance(result, float) else result
    
    except InvalidArgumentError:
        # Если хотя бы один из аргументов не является числом, возвращаем их строковое представление
        return f"{a}{b}"

# Примеры использования функции
print(add_everything_up(123.456, 'строка'))  # 123.456строка
print(add_everything_up('яблоко', 4215))    # яблоко4215
print(add_everything_up(123.456, 7))        # 130.456
