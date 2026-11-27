def add_matrices(a, b):
    if len(a) != len(b):
        raise ValueError("Matrices must have the same dimensions")

    result = []

    for i in range(len(a)):
        if len(a[i]) != len(b[i]):
            raise ValueError("Matrices must have the same dimensions")

        row = []

        for j in range(len(a[i])):
            row.append(a[i][j] + b[i][j])

        result.append(row)

    return result

fun = add_matrices([[1, 2], [3, 4]], [[5, 6], [7, 8]])   # [[6, 8], [10, 12]]
#fun1 = add_matrices([[1, 2]], [[1], [2]]) 

print(fun)
#print(fun1)
