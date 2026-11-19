PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

new_list = PRICE_LIST.split('\n')
my_tuple = map(lambda x: tuple(x.split()), new_list)
new_dict = {key: int(value[:-1]) for key, value in my_tuple}
print(new_dict)
