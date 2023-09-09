from colorama import Fore
from typing import Union


def get_number(question: str) -> Union[int, float]:
    number: Union[float, None] = None

    while number is None:
        try:
            number = float(input(question))
        except ValueError:
            print(Fore.RED + '\nYou need to type the number!')
    
    if number.is_integer():
        number = int(number)
    return number


def get_sign() -> str:
    signes = ['+', '-', '*', '/', '**']
    sign: Union[str, None] = None

    while sign is None:
        sign = input('Type the sign (+, -, *, /, ^): ')
        if sign.replace('^', '**') not in signes:
            sign = None
            print(Fore.RED + '\nYou typed the incorrect sign, try again!')
    return sign


def main():
    loop = True

    while loop:
        number_1: Union[int, float] = get_number(Fore.CYAN + 'Enter the first number: ')
        number_2: Union[int, float] = get_number(Fore.CYAN + 'Enter the second number: ')

        sign: str = get_sign()
        try:
            result: Union[float, int] = float(eval(f'{number_1} {sign} {number_2}'))
            if result.is_integer():
                result = int(result)
        except ZeroDivisionError:
            print('\n' * 100 + Fore.RED + 'You cannot divide by zero!')
        else:
            print('\n' * 100 + Fore.GREEN + f'{number_1} {sign} {number_2} = {result}')


if __name__ == '__main__':
    main()
