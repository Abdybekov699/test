
s = int(input('Сколько вы хотите накопить ?'))
m = int(input('Сколько у вас есть :'))

while m < 100:
    s = int(input('Взнос: '))
    m += s
print('Поздравляю вы накопили', m)