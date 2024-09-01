numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = [] # простые числа
not_primes = [] # составные числа
for i in range(len(numbers)):
    if numbers[i] == 1:
        continue
    if numbers[i] == 2:
        primes.append(numbers[i])
    else:
        for j in range(2, len(numbers)): # цикл поиска составных чисел
            while numbers[i] > j:
                if numbers[i] % j == 0:
                    not_primes.append(numbers[i])
                    numbers[i] = 0 # сост. число = 0 и выбывает из поиска простых чисел
                break
        for j in range(2, len(numbers)): # цикл поиска простых чисел
            while numbers[i] > j:
                if numbers[i] % j != 0:
                    primes.append(numbers[i])
                break
primes = set(primes) # тип "множество" исп. для удал. повторов, полученных при поиске
primes = list(primes)
print ('простые числа:', primes)
print ('составные числа:', not_primes)
