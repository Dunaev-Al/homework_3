def my_func(x, y):
    return x**y

def my_func2(x, y):
    result = 1
    for i in range(abs(y)):
        result = result * x
    return 1 / result


x = my_func(5, -4)
print(x)
x = my_func2(5, -4)
print(x)