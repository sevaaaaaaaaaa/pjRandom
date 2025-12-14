import random
from config import MIN_NUMBER, MAX_NUMBER, MAX_ATTEMPTS
from messages import *

class GuessNumberGame:
    def __init__(self):
        self.secret_number = 0
        self.attempts = 0

    def generate_number(self):
        """Генерация случайного числа"""
        self.secret_number = random.randint(MIN_NUMBER, MAX_NUMBER)

    def check_guess(self, guess):
        """Проверка числа пользователя"""
        self.attempts += 1
        if guess < self.secret_number:
            return TOO_LOW
        elif guess > self.secret_number:
            return TOO_HIGH
        else:
            return WIN

    def start(self):
        """Основной игровой цикл"""
        self.generate_number()
        print(WELCOME)

        while self.attempts < MAX_ATTEMPTS:
            try:
                user_input = int(input(INPUT_PROMPT))
            except ValueError:
                print(INVALID_INPUT)
                continue

            result = self.check_guess(user_input)
            print(result)

            if result == WIN:
                return