list_1 = []
for num_1 in range(1, 1001, 2):
    list_1.append(num_1 ** 3)
print("Список из кубов нечетных чисел от 1 до 1000: ", list_1)

list_2 = []
for num_2 in list_1:
    sum_1 = 0
    for num_3 in str(num_2):
        sum_1 += int(num_3)
    if sum_1 % 7 == 0:
        list_2.append(num_2 + 17)
print('Список чисел сумма цифр которых делится на 7 без остатка, к которым прибавили 17: ', list_2)

list_3 = []
for num_4 in list_2:
    sum_2 = 0
    for num_5 in str(num_4):
        sum_2 += int(num_5)
    if sum_2 % 7 == 0:
        list_3.append(num_4)
print('Список чисел из второго списка, сумма цифр которых делится на 7 без остатка : ', list_3)
