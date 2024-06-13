# List comprehension
# Дан кусок прайс листа
# При помощи генераторов превратите этот текст в словарь
# Обратите внимание, что цены в словаре имеют тип int (они не в кавычках)

PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

list = list(PRICE_LIST.split())
list_key = [x for x in list[0::2]]
list_value = [int(x.replace('р', '')) for x in list[1::2]]
new_dict = dict(zip(list_key, list_value))

print(new_dict)
