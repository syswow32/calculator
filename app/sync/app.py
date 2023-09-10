from colorama import Fore, init
from typing import Union


class Calculator:
    def __init__(self):
        self.number_1: Union[int, float, None] = None
        self.number_2: Union[int, float, None] = None
        self.sign: Union[str, None] = None
        
        self.result: Union[int, float, None] = None

    def get_number(self, question: str) -> Union[int, float]:
        '''This method need the question and returns the valid number, that user typed
        '''
        number: Union[float, None] = None

        while number is None:
            try:
                number = float(input(question))
            except ValueError:
                print(Fore.RED + '\nYou need to type the number!')
        
        if number.is_integer():
            number = int(number)
        return number

    def get_sign(self) -> str:
        '''This method returns valid sign
        '''
        signes = ['+', '-', '*', '/', '**']
        sign: Union[str, None] = None

        while sign is None:
            sign = input('Type the sign (+, -, *, /, ^): ')
            if sign.replace('^', '**') not in signes:
                sign = None
                print(Fore.RED + '\nYou typed the incorrect sign, try again!')
        return sign
    
    def solve(self):
        '''This method solves the conversion
        '''
        try:
            self.result = float(eval(f'{self.number_1} {self.sign.replace("^", "**")} {self.number_2}'))
            if self.result.is_integer():
                self.result = int(self.result)
        except ZeroDivisionError:
            print('\n' * 100 + Fore.RED + 'You cannot divide by zero!')
        else:
            print('\n' * 100 + Fore.GREEN + f'{self.number_1} {self.sign} {self.number_2} = {self.result}')


def main():
    init()
    
    calc = Calculator()
    while calc:
        calc.number_1 = calc.get_number(Fore.CYAN + 'Enter the first number: ')
        calc.number_2 = calc.get_number(Fore.CYAN + 'Enter the second number: ')

        calc.sign = calc.get_sign()
        calc.solve()


if __name__ == '__main__':
    main()
