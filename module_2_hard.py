import random
number = random.randint(3, 20)
def password_generation(number):
    result = ""
    for i in range(1, number):
        for j in range(i + 1, number):
            if number % (i + j) == 0:
                result += str(i) + str(j)
    return result
password = password_generation(number)
print(f"Число {number} - пароль: {password}")
