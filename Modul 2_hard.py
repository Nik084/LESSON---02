start_number = int(input ('Введите целое число от 3 до 20: '))
def find_parol():
    deliteli_ = []
    for k in range(3, start_number): # цикл поиска делителей, по условию задачи берём делители > 2
            if start_number % k == 0:
                deliteli_.append(k)
    deliteli_.append(start_number)
    #print (f'требуемые делители для {start_number}: {deliteli_}') # список делителей больше 2, последний равен вводимому числу
    result = []
    for i in range (1, start_number):
        for j in deliteli_:
            if j - i  > i and j > i:
                result.append(i)
                result.append(j - i)
                #print (i, j - i)
    #print (result)
    result = str(result)
    print (f'Пароль для {start_number}:', (result.replace(', ', '')[1:-1]))
while start_number < 3: # ограничений на максимум нет, хоть задание было до 20
    start_number = int(input('Маловато будет))) Введите целое число от 3 до 20: '))
while start_number > 20:
    find_bigger = input(f'Введённое число > 20. Введите какую-л. комбинацию для выхода. Для поиска пароля чмсла {start_number} нажмите "Enter"')
    #break
    if find_bigger == '':
         find_parol()
         break
    else:
        print (f'Поиск пароля для числа {start_number} прерван, начните новый поиск.')
        break
else:
    find_parol()