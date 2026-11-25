def remove_duplicates(l):

    result = []

    for i in l:
        if i not in result:
            result.append(i)
    return result





fun1 = remove_duplicates([3, 1, 3, 2, 1])   # [3, 1, 2]
fun2 = remove_duplicates([])   

print(fun1)
print(fun2)