var1 = 'qwq'
var2 = 'qwddq2'

my_dict = {
    'tuple': (1, 3, 6, 7, None, 'teccczxt', False, 2.42),
    'list': [1, 3, 6, 7, None, 'text-qwerty', True, 2.42, 'csasdcasd', 'last', 'last2'],
    'dict': {
        'one': '1',
        'two': '2',
        'three': var2,
        'four': '4',
        'five': None
    },
    'set': {'set1', False, 1, var1, None}
}

print("Последний элемент tuple ", my_dict['tuple'][-1], "\n")

# добавьте в конец списка еще один элемент
my_dict['list'].append('some_new')
# удалите второй элемент списка
my_dict['list'].pop(1)
# добавьте в конец списка еще один элемент
my_dict['dict'][('i am a tuple',)] = 'Alko-Tester'
# удалите какой-нибудь элемент
del my_dict['dict']['one']
# добавьте новый элемент в множество
my_dict['set'].add('cool lesson')
# удалите элемент из множества
my_dict['set'].pop()
# выведите на экран весь словарь
print(my_dict)
