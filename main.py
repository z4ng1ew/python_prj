# user, admin, number = 'Anna', 'Bob', 9
# print(user, admin, number)
#
#
# *users, age = 'Anna', 'Kate', 'Bob', 9
# print(users)
#
# print(age)
#
#
# *char, num = 'Ivan', 'Тимур', 'Ростислав', 'gogi', 4, 5, 5, 7
# print(char)
# print(num)
#
#
# var_1 = var_2 = var_3 = 5
# print(var_1, var_2, var_3)
#
#
# var_num, var_str = 'gogi', 4
# print(var_num, var_str)
# var_num, var_str = var_str, var_num
#
#
# print(var_num, var_str)
#
#
# a = 2
# a = a + 5
#
#
# b = 0
# b += 7
#
# print(b)
#
# x = 34
# x = x % 6
#
# c = 5
# x = x % 2
#
# h = 11 % 3
#
# print(h, 'tr')
#
# y = 14 % 5
# print(y, 'gg')
#
#
# print(x, "pro cent")
#
#
# n = 10
# if n % 2 == 0:
#     print(f"{n} - чётное число")
# else:
#     print(f"{n} - не чётное число")
#
#
#
#
# index = 5 % 3
# print(index)
#
# day_n = 10
# day_of_week = day_n % 7
# print(day_of_week, 'gg')
#
#
# name = 'Марина'
#
# age = 25
# print("Привет, %s! Тебе %d лет." %(name, age))
#
#
# x1 = -10 % 3
# y1 = 10% -3
# print(x1, y1)
#
#
#
# x3 = 10
# x3 %= 3
# print(x3)
#
#
#
#
#
# colors = ['red', 'green', 'blue']
# ind = 4
# color = colors[ind % len(colors)]
# print(color)
#
# print(len(colors))
#
#
#
#
# h_24 = 15
#
# h_12 = h_24 % 12
# print(h_12, "h_12,")


# # Пример использования оператора **=
# x = 2
# y = 3

# # Возведение x в степень y и присваивание результата переменной x
# x **= y

# print(x)  # Результат будет 8, потому что 2 ** 3 = 8



# a = 5
# a **= 2
# print(a)  # 25, потому что 5 ** 2 = 25

# b = 3
# b **= 3
# print(b)  # 27, потому что 3 ** 3 = 27


# x = 10
# x **= 3 #возводит в степень левый операнд в степень правого и присваивает результат
# print(x)

# r = 4
# r **= 2
# print(r)


# c1 = 3

# c1 **= 0.3
# print(c1)

# c = 9
# c **= 0.5
# print(c)  # Результат будет 3.0, потому что 9 ** 0.5 = 3.0 (это вычисление квадратного корня)


# t = 10

# t **= -1
# print(t, 't')


# d = 2
# d **= -1
# print(d)  # Результат будет 0.5, потому что 2 ** -1 = 1 / 2



# # w = 3

# # for r in range(5):
# #     x **= 2
# #     print(f'после возведения в степень {r+1}: {x}')



# x = 2
# for i in range(3):
#     x **= 2
#     print(f'После возведения в степень {i+1}: {x}')





# def schet (f = 2):
#     for d in range(3):
#         f **= 2
#     print(f'счёт {d + 1}: {f}')
#     return f


# res = schet()

# print(f'Результат: {res}')




# def schet(f=2):
#     for d in range(2):
#         f **= 2
#         print(f'счёт {d + 1}: {f}')  # Выводим результат на каждой итерации

# schet()





# x = 20

# y = 2

# x //= y
# print(x)
# print(x)

# t = 22//3
# print(t)

# y1 = 3**2

# print(y1, 's')






# Создаем обычное множество
# my_set = {1, 2, 3}

# # Создаем замороженное множество
# my_frozenset = frozenset([4, 5, 6])

# # Множества можно использовать в операциях
# union_result = my_set | my_frozenset  # Объединение множеств
# print(union_result)  # Выведет: {1, 2, 3, 4, 5, 6}

# # Попытка изменить замороженное множество вызовет ошибку
# #my_frozenset.add(7)  # Ошибка, нельзя изменять замороженное множество




# set1 = frozenset([1, 2, 3])
# set2 = frozenset([2, 3, 4])

# # Пересечение
# print(set1 & set2)  # Выведет frozenset({2, 3})

# # Объединение
# print(set1 | set2)  # Выведет frozenset({1, 2, 3, 4})

# # Разность
# print(set1 - set2)  # Выведет frozenset({1})



# Элементы, которые есть в set1, но нет в set2: это только 1, так как:
# 2 и 3 присутствуют в обоих множествах (поэтому они удаляются из результата),
# 4 есть только в set2, но эта операция разности вычитает из set1, поэтому 4 не учитывается.

# Симметрическая разность
# print(set1 ^ set2)  # Выведет frozenset({1, 4})























# Множества и массивы (в Python это списки) отличаются по нескольким важным характеристикам и функциональным возможностям. Вот основные различия между **множествами** и **списками** (массивами):

# ### 1. **Уникальность элементов**
#    - **Множества** (`set`): Все элементы должны быть уникальными. Если ты добавишь элемент, который уже присутствует в множестве, он не будет добавлен повторно.
#    - **Списки** (`list`): Могут содержать дубликаты, то есть одно и то же значение может встречаться несколько раз.

#    **Пример**:
#    ```python
#    my_set = {1, 2, 3, 3}
#    print(my_set)  # Выведет: {1, 2, 3}, так как повторяющийся элемент 3 удалится

#    my_list = [1, 2, 3, 3]
#    print(my_list)  # Выведет: [1, 2, 3, 3], дубликаты остаются
#    ```

# ### 2. **Порядок элементов**
#    - **Множества**: Неупорядоченные структуры данных. Это значит, что элементы не имеют фиксированной позиции, и их порядок не сохраняется.
#    - **Списки**: Упорядоченные структуры данных. Каждый элемент имеет свою позицию (индекс), и порядок элементов сохраняется.

#    **Пример**:
#    ```python
#    my_set = {3, 1, 2}
#    print(my_set)  # Выведет: {1, 2, 3}, порядок не гарантируется

#    my_list = [3, 1, 2]
#    print(my_list)  # Выведет: [3, 1, 2], порядок сохраняется
#    ```

# ### 3. **Изменяемость**
#    - **Множества**: Изменяемы, можно добавлять и удалять элементы, но они остаются неупорядоченными.
#      - Есть неизменяемая версия множества — **`frozenset`**, которая не допускает изменений после создания.
#    - **Списки**: Также изменяемы, можно добавлять, удалять, изменять элементы, и их порядок сохраняется.

# ### 4. **Хешируемость элементов**
#    - **Множества**: Элементы множества должны быть хешируемыми. Это значит, что ты не можешь включать в множество изменяемые объекты, такие как списки или другие множества. Например, ты не можешь добавить список в множество.
#    - **Списки**: Могут содержать любые типы данных, включая изменяемые объекты, такие как другие списки, словари и даже множества.

#    **Пример**:
#    ```python
#    my_set = {1, 2, [3, 4]}  # Ошибка, потому что списки не хешируемы
#    my_list = [1, 2, [3, 4]]  # Допустимо
#    ```

# ### 5. **Операции поиска**
#    - **Множества**: Операции проверки наличия элемента (`in`) происходят быстрее, так как множества используют хеширование. Поиск элемента в множестве выполняется за **O(1)** в среднем.
#    - **Списки**: Поиск элемента требует последовательного обхода всех элементов и имеет сложность **O(n)**.

#    **Пример**:
#    ```python
#    my_set = {1, 2, 3}
#    print(2 in my_set)  # True, поиск выполняется быстро

#    my_list = [1, 2, 3]
#    print(2 in my_list)  # True, но поиск медленнее, особенно на больших данных
#    ```

# ### 6. **Операции над коллекциями**
#    - **Множества**: Поддерживают множество математических операций, таких как **объединение** (`union`), **пересечение** (`intersection`), **разность** (`difference`) и **симметрическая разность** (`symmetric_difference`). Эти операции позволяют удобно работать с данными.
#    - **Списки**: Не поддерживают такие операции напрямую, но можно выполнить аналогичные действия, используя циклы и другие методы Python.

#    **Пример**:
#    ```python
#    set1 = {1, 2, 3}
#    set2 = {3, 4, 5}

#    # Объединение множеств
#    print(set1 | set2)  # {1, 2, 3, 4, 5}

#    list1 = [1, 2, 3]
#    list2 = [3, 4, 5]

#    # Для списков нужно использовать другие методы, например объединение через сложение
#    print(list1 + list2)  # [1, 2, 3, 3, 4, 5]
#    ```

# ### Когда использовать множества, а когда списки:

# - **Используй множества**, если:
#   - Тебе нужно хранить только уникальные элементы.
#   - Ты собираешься часто проверять наличие элемента (проверка на принадлежность быстрее).
#   - Тебе нужно выполнять математические операции над данными (объединение, пересечение, разность и т. д.).

# - **Используй списки**, если:
#   - Тебе нужно сохранить порядок элементов.
#   - Ты собираешься работать с дубликатами.
#   - Тебе нужны операции, связанные с индексами элементов (например, доступ по индексу или сортировка).

# ### Итог:

# | Характеристика                | Списки (list)            | Множества (set)            |
# |-------------------------------|--------------------------|----------------------------|
# | Уникальность элементов         | Нет                      | Да                         |
# | Порядок элементов              | Сохраняется              | Неупорядоченные             |
# | Изменяемость                   | Изменяемые               | Изменяемые                  |
# | Хешируемость элементов         | Любые объекты             | Только хешируемые объекты   |
# | Поиск элемента                 | Медленный (O(n))         | Быстрый (O(1))              |
# | Операции объединения/разности  | Не поддерживаются напрямую | Поддерживаются напрямую    |

# Таким образом, множества полезны, когда ты работаешь с уникальными элементами и хочешь быстрой проверки принадлежности, а списки более универсальны для последовательных данных, где важен порядок и допускаются повторения.





# a = 1

# print(dir(a))


# print(1, end = '*')
# print(44)
# print(12, end = '*')



# sub = "f"
# string = 'fgfg'

# count = string.count(sub, 0, len(string))

# print(count)






# d = 't'

# print(d.count('ttt'))


# s = "e"
# print(s.count(('exel')))




# r = 'ппривет'

# print(r.count('п', ), 'п')


# h = '111yy666666yy'
# print(h.find('y', 5, 7), 'y')





# word = '01234'
# # print(word.find('l',3, 4))
# # print(word.find('l'))
# print(word.find('3'), 'rtttttttttt')

# qq = 'goodbuy'
#
# print(qq.index('o'), 'o')
#
#
# print(qq.rindex('o'), 'o')


# str1 = '12345'
#
# print(str1.replace('2', '9'))
#
#
# str2 = 'нижний регистр'
#
# print(str2.upper())
#
#
# str2 = 'ВЕРХНИЙ верхний регистр'
#
# print(str2.lower())
#
#
# print(str2.replace('ВЕРХНИЙ', 'перевод'))
#
#
# S = 'Qwerty Qwerty'
#
# l = 'loweR loweR'
#
# print(S.capitalize())
#
# print(l.title())



#
# word = 'ssss'
#
# digit = '123'
#
# alnumber = '123aaa'
#
# print(word.isalpha())
# print(digit.isdigit())
#
# print(alnumber.isalnum())
#
#
#
# p = '   probel          f'
#
# print(p.strip(), 's', end = ' ')


#
# str3 = '123 456 789 10 .'
#
# print(str3.startswith('123'))
# print('123 456 789 10 .'.startswith('1'))
# print(str3.endswith(' .'))



# print(str3.removeprefix('123'))
# print('123 456 789 10 .'.startswith('1'))
# print(str3.removesuffix(' .'))



# bots_start_1000 = 1000
# lose_bots_2 = 2
# add_bots_3 = 3
# days_30 = 30
#
# bots_today  = bots_start_1000 + days_30 *(add_bots_3 - lose_bots_2)
#
# bots_today_2  = bots_start_1000 -  (days_30 * lose_bots_2)
#
#
# print(bots_today, 'bots_today')
# print(bots_today_2, 'bots_today_2')



# katet_dlinniy = 4
# katet_korotkiy = 3
#
#
# kk_2 = katet_korotkiy * katet_korotkiy
#
# kd_2 = katet_dlinniy * katet_dlinniy
#
#
# summa = kd_2 + kk_2
#
#
#
# gipotenuza = summa ** 0.5
#
# print(int(gipotenuza), 'gipo')
#
# g = summa //  5
#
# print(int(g), 'gipo')
#
# dop = 1.5  + 1.5
#
# dop1 = int(dop)  # Преобразование dop в int
#
# res = dop1 + g

# print(int(res), 'gipo')




S_yra = 7*9

radius_alex = 9 / 2

print(radius_alex)








