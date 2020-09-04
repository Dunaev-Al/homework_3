def info(name, age, email, city, number):
    stroke = name + str(age) + email + city + str(number)
    return stroke


x = info('vasya', 18, 'vasya@vasya.com', 'Moscow', 123321)
print(x)

