SI = int(input())
SI1 = SI // 1000
SI2 = SI // 100 % 10
SI3 = SI % 100 // 10
SI4 = SI % 10
if SI1 + SI4 == SI2 - SI3:
    print('Да')
else:
    print('Нет')
