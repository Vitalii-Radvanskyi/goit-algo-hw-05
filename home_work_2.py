from typing import Callable
import re


def generator_nambers(text: str):
    numbers = re.findall(r'(?<= )\d+(?= )', text)
    yield float(numbers)
    

def sum_profit(func : Callable):
    total = 0
    for number in generator_nambers(text):
         total += number
    return total
         
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(generator_nambers, text)
print(f"Загальний дохід: {total_income}")
        
