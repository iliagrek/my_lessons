def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(2)
print_params([1, 2, 3])
print_params(b=25)
print_params(c=[1, 2, 3])
values_list = [13, 'тип1', False]
values_dict = {'a': 5, 'b': 'тип2', 'c': [6, 7]}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)
