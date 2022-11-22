# users = ('kewa', 'kolya', 'yura', 'kojo')
# print(users[1][2])

# users = ('kewa', 'kolya', 'yura', 'kojo')
# print(users[1][::-1])

# users = ('kewa', 'kolya', 'yura', 'kojo')
# print(users[1][::-1])
#
# users = ('kewa', 'kolya', 'yura', 'kojo')
# print(users[::-1])

# names = ['kewa', 'kolya', 'yura', 'kojo']
# for i in names:
#     print(i)
#
# names = ['kewa', 'kolya', 'yura', 'kojo']
# for i in names:
#     print(f'Имя - {i}')
#
# names = ['kewa', 'kolya', 'yura', 'kojo']
# for i in range(len(names)):
#     print(f'{i} - {names[i]}')

# names = ['kewa', 'kolya', 'yura', 'kojo']
# a = input('Введите свое имя -')
# names.append(a)
# print(names)

# names = ['kewa', 'kolya', 'yura', 'kojo']
# names.append(input('Введите свое имя -'))
# print(names)
#
# names = ['kewa', 'kolya', 'yura', 'kojo']
# for i in range(3):
#     names.append(input('Введите свое имя -'))
# print(names)

# names = ['kewa', 'kolya', 'yura', 'kojo']
# new_names = []
# for i in range(3):
#     new_names.append(input('Введите свое имя -'))
# print(names)
# print(new_names)
# names.extend(new_names)
# print(names)

#
# names = ['kewa', 'kolya', 'yura', 'kojo', 'kojo']
# print(names.count('kojo'))


# names = ['kewa', 'kolya', 'yura', 'kojo', 'kojo']
# print(names.remove('kojo'))
# print(names)

# names = ['kewa', 'kolya', 'yura', 'kojo', 'kojo']
# print(names.remove('kojo'))
# a = names.count('kojo')
# print(names)

# names = ['kewa', 'kolya', 'yura', 'kojo', 'kojo']
# for i in range(names.count('kojo')):
#     names.remove('kojo')
# print(names)

# names = ['kewa', 'kolya', 'yura', 'kojo', 'kojo']
# names.pop(0)
# print(names)

# names = ['kewa', 'kolya', 'yura', 'kojo', 'kojo']
# a = names.index('kojo')
# print(a)
# print(names[a])

# names = ['kewa', 'kolya', 'yura', 'kojo', 'kojo']
# print(names[0:3])

# names = ['kewa', 'kolya', 'yura', 'kojo', 'kojo']
# print(names[0:3])

# names = ['kewa', 'kolya', 'yura', 'kojo', 'kojo']
# print(names[3:0:-1])

# a = [i for i in range(10)]
# print(a)

# a = [i for i in 'Python']
# print(a)

# names = ['JACK', 'JIMMY', 'JACKSON', 'JHON', 'JACKSON', 'JHON',  'JIMMY', 'JACKSON',
#          'JHON','JACK', 'JIMMY', 'JACK', 'JACKSON', 'JHON', 'JACKSON', 'JHON','JACK',
#          'JIMMY', 'JACK', 'JACKSON', 'JHON',]
# for i in range(len(names)):
#     print(i)

names = ['JACK', 'JIMMY', 'JACKSON', 'JHON', 'JACKSON', 'JHON',  'JIMMY', 'JACKSON',
         'JHON','JACK', 'JIMMY', 'JACK', 'JACKSON', 'JHON', 'JACKSON', 'JHON','JACK',
         'JIMMY', 'JACK', 'JACKSON', 'JHON',]
for i in range(len(names)):
    if i % 2 == 0:

print(names)
