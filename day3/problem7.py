def transpose(m):
    if not m:
        return []

    result = []

    for col_index, _ in enumerate(m[0]):
        new_row = []

        for row_index, row in enumerate(m):
            new_row.append(row[col_index])

        result.append(new_row)

    return result

fun = transpose([[1, 2, 3], [4, 5, 6]])   # [[1, 4], [2, 5], [3, 6]]
print(fun)