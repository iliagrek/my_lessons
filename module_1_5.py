immutable_var = (366,12,False,"name")
print(immutable_var)
# immutable_var [3][3] = 2
# print(immutable_var)
# выдает ошибку "TypeError: 'str' object does not support item assignment" - это значит что изменить нельзя так как кортеж не поддерживает обращение по элементам, это не зависит от типа будь то 'str', 'bool' или 'int'
mutable_list = [True,1,"name","age"]
print(mutable_list)
mutable_list[0] = 24
mutable_list[1] = "lemon"
mutable_list[2] = 25.3
mutable_list[3] = False
print(mutable_list)