perc = int(input('pls enter number from 1 to 100: '))
while perc in range(101):
    if perc != 11 and perc % 10 == 1:
        print(perc, 'процент')
    elif perc not in [12, 13, 14] and (perc % 10 == 2 or perc % 10 == 3 or perc % 10 == 4):
        print(perc, 'процента')
    else:
        print(perc, 'процентов')
    perc = int(input('pls enter number from 1 to 100 or print 000 to quite: '))
    if perc == 000:
        break
