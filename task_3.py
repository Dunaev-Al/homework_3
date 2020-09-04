def my_func(x, y, z):
    sum = 0
    arr = [x, y, z]
    arr.remove(min(arr))
    for i in arr:
        sum = sum + i
    return sum


result = my_func(1, 2, 3)
print(result)