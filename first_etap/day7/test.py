# names = {'dastan', 'danila', 'sonun', 'roman'}
# print(names)

# names = {'dastan', 'danila', 'sonun', 'roman'}
# names2 = {'Abdymazhit', 'Natalia', 'Dastan', 'Nuriza'}
# print(names.difference(names2))
#
# names = {'dastan', 'danila', 'sonun', 'roman'}
# names2 = {'Abdymazhit', 'Natalia', 'dastan', 'Nuriza'}
# names.discard('dastan')
# print(names)

# names = {'dastan', 'danila', 'sonun', 'roman'}
# names2 = {'Abdymazhit', 'Natalia', 'dastan', 'Nuriza'}
# names.intersection_update(names2)
# print(names)

# names = {'dastan', 'danila', 'sonun', 'roman'}
# names2 = {'Abdymazhit', 'Natalia', 'dastan', 'Nuriza'}
# print(names.pop())

# S L O V A R Y

# food = {}
# data = {
#     "name": 'Abdymazhit',
#     "last_name": 'Abdybekov',
#     "age": 28,
#     "stacks": 'Python',
#     "laptop": {
#         'name': 'macbook',
#         'year': 2021
#     }
# }
# data['name'] = input()
# print(data)

# data = {
#     "name": 'Abdymazhit',
#     "last_name": 'Abdybekov',
#     "age": 28,
#     "stacks": 'Python',
#     "laptop": {
#         'name': 'macbook',
#         'year': 2021
#     }
# }
# print(data['laptop'])

# data = {
#     "name": 'Abdymazhit',
#     "last_name": 'Abdybekov',
#     "age": 28,
#     "stacks": 'Python',
#     "laptop": {
#         'name': 'macbook',
#         'year': 2021
#     }
# }
# print(data['laptop']['name'][1])

# data = {
#     "name": 'Abdymazhit',
#     "last_name": 'Abdybekov',
#     "age": 28,
#     "stacks": 'Python',
#     "laptop": {
#         'name': 'macbook',
#         'year': 2021,
#         'cost': 50000
#     }
# }
# print(data.get('name'))

# data = {
#     "name": 'Abdymazhit',
#     "last_name": 'Abdybekov',
#     "age": 28,
#     "stacks": 'Python',
#     "laptop": {
#         'name': 'macbook',
#         'year': 2021,
#         'cost': 50000
#     }
# }
# print(data.values())
#
# data = {
#     "name": 'Abdymazhit',
#     "last_name": 'Abdybekov',
#     "age": 28,
#     "stacks": 'Python',
#     "laptop": {
#         'name': 'macbook',
#         'year': 2021,
#         'cost': 50000
#     }
# }
# print(data.items())


# data = {
#     "name": 'Abdymazhit',
#     "last_name": 'Abdybekov',
#     "age": 28,
#     "stacks": 'Python',
#     "laptop": {
#         'name': 'macbook',
#         'year': 2021,
#         'cost': 50000
#     }
# }
# for i, j in data.items():
#     print(i)

# data = {
#     "name": 'Abdymazhit',
#     "last_name": 'Abdybekov',
#     "age": 28,
#     "stacks": 'Python',
#     "laptop": {
#         'name': 'macbook',
#         'year': 2021,
#         'cost': 50000
#     }
# }
# for i, j in data.items():
#     print(f'{i} - {j}')

# a = [('Abdymazhit', 'Danila'), ('Erkinbek', 'Natalia'), ('Nuriza', 'Roman'), ('Vladislav', 'Dastan')]
# for i, j in a:
#     print(a)

# data = {
#     "name": 'Abdymazhit',
#     "last_name": 'Abdybekov',
#     "age": 28,
#     "stacks": 'Python',
#     "laptop": {
#         'name': 'macbook',
#         'year': 2021,
#         'cost': 50000
#     }
# }
# data.update({'national': 'Kyrgyz'})
# print(data)
#
# data = {
#     "name": 'Abdymazhit',
#     "last_name": 'Abdybekov',
#     "age": 28,
#     "stacks": 'Python',
#     "laptop": {
#         'name': 'macbook',
#         'year': 2021,
#         'cost': 50000
#     }
# }
# data['national'] = 'Kyrgyz'
# print(data)

# menu = {'lagman': 120, 'plov': '120', 'borsh': 100}
# menu['drinks'] = ['Coca-Cola', 'Sprite', 'Fanta']
# print(menu)

# a = ['234', 'qwerty', '234', '543', 'qwerty']
# b = set(a)
# a = list(b)
# print(a)

a = ['234', 'qwerty', '234', '543', 'qwerty']
b = set(a)
a = list(b)
print(a)