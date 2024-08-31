import time


def factorize(*numbers):
    result = []
    for number in numbers:
        div = []
        for i in range(1, number + 1):
            if number % i == 0:
                div.append(i)
        result.append(div)
    return result


numbers = [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 323563298]

start_time = time.time()
result = factorize(*numbers)
end_time = time.time()
ex_time = end_time - start_time

print(f"Результат: {result}")
print(f"Час виконання: {ex_time:.3f} секунд")