import time
import random as rd

start = time.time()
array_numbers = []
num = int(input('Введите кол-во элементов массива: '))
for _ in range(num):
    array_numbers.append(rd.randint(1, 50000))


def search(array_numbers, number):
    result = []
    for element in array_numbers:
        if element % 2 == 0:
            result.append(element - number)
    return result


n = int(input('Введите число: '))
print(search(array_numbers, n))
end = time.time() - start
print(f"Время выполнения функции: {end} млсек")
