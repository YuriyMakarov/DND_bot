class NegativeNumberError(Exception):
    def __init__(self, number):
        self.number = number
        super().__init__(f"Отрицательное число {number} не допустимо")
