def count_down(n):
    result = []
    i = n
    while i > 0:
        result.append(i)
    return result



fun = count_down(3)
print(fun)
#[3, 2, 1]

fun1 = count_down(0)
print(fun1)
#[]
