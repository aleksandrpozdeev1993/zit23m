# Даны два целых числла A и B, A > B. 
# Выведите все нечётные числа от A до B включительно, в порядке убывания

def printOddNumbers(a,b):
    i = b
    res = []
    while i >= a:
        if i % 2 != 0:
            res.append(i)
        i -= 1
    print(res)
    return res

a = int(input("Введите A: "))
b = int(input("Введите B: "))

printOddNumbers(a,b)