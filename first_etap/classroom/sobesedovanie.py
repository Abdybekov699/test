y = input('Язык программирования -')
v = int(input('Возраст -'))
o = int(input('Опыт -'))
z = int(input('Желаемая зарплата -'))
if y in ('java', 'python', 'javascript'):
    if v >= 18:
        if o > 3:
            if z < 60000:
                print('Вы приняты')


else:
    print('В следующий раз')