def times_table(n):
    result = []
    row = []
    for i in range(n):

        for j in range(n):
            row.append((i + 1) * (j + 1))

        result.append(row)

    return result


fun1 = times_table(3)   # [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
fun2 = times_table(0)   # []

print(fun1)
print(fun2)