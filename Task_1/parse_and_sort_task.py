'''
# Задание № 1
# Входные данные: файл с тестовыми данными (генерируется при отсутствии)
# Выходные данные: вывод в консоль значений из распарсенного файла
# с тестовыми данными в порядке возрастания и убывания 
'''
import numpy as np

try: # если файл есть- открываем его
    f = open('data_for_test1.txt', 'r')
except: # файла нет - создаем его и наполняем данными
    numbers0_20 = np.arange(21) # генерим 20 чисел
    np.random.shuffle(numbers0_20) # перемешиваем числа
    shuffled_numbers = [str(a) for a in numbers0_20]
    f = open('data_for_test1.txt', 'w') # создание файла с тестовыми данными
    f.write(",".join(shuffled_numbers)) # пишем в файл числа через запятую
    f.close() # закрываем файл

incoming_data = f.read()
string_list = incoming_data.split(',') # переводим строку с данными в массив
numbers_list = [int(a) for a in string_list] # переводим массив строк в массив чисел

sortA_Z = sorted(numbers_list, reverse = False) # сортировка по возрастанию
sortZ_A = sorted(numbers_list, reverse = True) # сортировка по убыванию

# вывод в консоль
print("Значения, отсортированные по возрастанию: ")
print(sortA_Z)
print("Значения, отсортированные по убыванию: ")
print(sortZ_A)

# предотвращение закрытия консоли после выполнения кода
x = input()