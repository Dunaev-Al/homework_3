def int_func(string):
    new_str = ''
    array = string.split()
    for i in array:
        i = str(i)
        i = i.capitalize()
        new_str += str(i)
    return new_str


word = int_func(input('Введите слово из маленьких букв с пробелами'))


print(word)