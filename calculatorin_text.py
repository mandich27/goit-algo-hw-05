from typing import Callable
import re


def generator_numbers(text: str):
    for match in re.findall(r'\s\d+\.\d+\s', text):                         # Шукаємо співпадіння через регулярний вираз числа розділені крапкою
        yield float(match)                                                  # Співпадіння переводимо в тип float


def sum_profit(text: str, func: Callable[[str], float])-> float:            # Приймаєм str і число float
    nums = 0
    for numbers in func(text):                                              # Циклом for перебираєм numbers і додаємо в nums
        nums += numbers                                                     # Сумуємо знайдені числа
    return nums                                                             # Повертаєм nums



text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."



total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
