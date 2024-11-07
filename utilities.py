def calculate_average(numbers):
    t = 0
    s = 0
    for num in numbers:
        s += numbers[t]
        t += 1
    print(f'Середнє арифметичне{s / len(numbers)}')


def find_max(numbers):
    sorted(numbers)
    print(f'Максимальне значення {numbers[-1]}')