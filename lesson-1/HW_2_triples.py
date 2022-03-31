list_1 = []
for num_1 in range(1, 1001, 2):
    list_1.append(num_1 ** 3)

list_2 = []
for num in list_1:
    sum_1 = 0
    for num_1 in str(num):
        sum_1 += int(num_1)
    if sum_1 % 7 == 0:
        list_2.append(num)
print('Числа, чья сумма цифр делится на 7 без остатка: ', list_2)

list_3 = []
for num_3 in list_1:
    num_3 += 17
    sum_2 = 0
    for num_2 in str(num_3):
        sum_2 += int(num_2)
    if sum_2 % 7 == 0:
        list_3.append(num_3)
print('Числа, к которым прибавили 17, чья сумма цифр делится на 7 без остатка: ', list_3)
