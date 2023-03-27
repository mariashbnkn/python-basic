"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*numbers):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    """
    return [number * number for number in numbers]


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(number):
    if number != 0 and number != 1:
        k = 0
        for i in range(2, number // 2 + 1):
            if number % i == 0:
                k += 1
        if k <= 0:
            return True


def filter_numbers(numbers_list, filter_type):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)
    """
    if filter_type == ODD:
        return [number for number in numbers_list if number % 2 != 0]
    if filter_type == EVEN:
        return [number for number in numbers_list if number % 2 != 1]
    if filter_type == PRIME:
        return [number for number in numbers_list if is_prime(number) == True]