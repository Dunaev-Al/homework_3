def user_sum(user_str):
    sum = 0
    array = user_str.split()
    for i in array:
        sum += int(i)
    return sum


user_str = input('Введите строку чисел, разделенных пробелом')
summa = user_sum(user_str)
print(f' Сумма чисел: {summa}')
user_str_new = input('Продолжите ввод разделенных пробелом или напишите q для выхода')
if user_str_new != 'q':
    new_sum = user_sum(user_str_new)
    new_sum += summa
    print(new_sum)

else:
    print('Конец')
