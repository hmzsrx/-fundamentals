def multiply_matrices(a, b):
    if len(a[0]) != len(b):
        raise ValueError("Number of columns in a must equal number of rows in b")

    result = []

    for i in range(len(a)):
        row = []

        for j in range(len(b[0])):
            total = 0

            for k in range(len(b)):
                total += a[i][k] * b[k][j]

            row.append(total)

        result.append(row)

    return result

fun = multiply_matrices([[1, 2], [3, 4]], [[5, 6], [7, 8]])   # [[19, 22], [43, 50]]
fun1 = multiply_matrices([[1, 2, 3]], [[1], [0], [2]])         
# [[7]]
#fun3 = multiply_matrices([[1, 2]], [[1, 2]])     

print(fun)
print(fun1)
#print(fun3)