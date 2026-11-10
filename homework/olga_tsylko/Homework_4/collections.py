my_dict = {
    'tuple': (100, 222, 333, 4, (1, 1000)),
    'list': ['test', 100, False, True, None],
    'dict': {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', (1, 2): {6: 'value'}},
    'set': {1, None, 'text', 1000, 'Test'}
}

print(my_dict['tuple'][-1])
my_dict['list'].append(200)
my_dict['list'].pop(1)
my_dict['dict'][('i am a tuple',)] = False
my_dict['dict'].pop(1)
my_dict['set'].add(10000)
my_dict['set'].remove(1)
print(my_dict)
