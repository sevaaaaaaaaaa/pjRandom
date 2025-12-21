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
            return UNDER  
        elif guess > self.secret_number:
            return OVER   
        else:
            return SUCCESS  

    def start(self):
        """Основной игровой цикл"""
        self.generate_number()
        print(INTRO)  

        prompt_text = PROMPT.format(MIN_NUMBER=MIN_NUMBER, MAX_NUMBER=MAX_NUMBER)

        while self.attempts < MAX_ATTEMPTS:
            try:
                user_input = int(input(prompt_text)) 
            except ValueError:
                print(ERROR) 
                continue

            result = self.check_guess(user_input)
            print(result)

            if result == SUCCESS: 
                return
        
        print(FAILURE.format(number=self.secret_number))
