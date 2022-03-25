list_1 = []
for num_1 in range(1, 1001, 2):
    list_1.append(num_1 ** 3)
# print("Список из кубов нечетных чисел от 1 до 1000: ", list_1)

list_2 = []
for num in list_1:
    sum_1 = 0
    for index in range(len(str(num))):
        sum_1 += int(str(num)[index])
    if sum_1 % 7 == 0:
        list_2.append(num)
print('Числа, чья сумма цифр делится на 7 без остатка: ', list_2)

list_3 = []
for num_1 in list_1:
    num_1 += 17
    sum_2 = 0
    for index in range(len(str(num_1))):
        sum_2 += int(str(num_1)[index])
    if sum_2 % 7 == 0:
        list_3.append(num_1)
print('Числа, к которым прибавили 17, чья сумма цифр делится на 7 без остатка: ', list_3)
