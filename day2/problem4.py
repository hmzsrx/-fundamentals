def count_items(l):

    result = {}
    

    for i in l:
        if i not in result:
            result[i] = 0
        result[i] += 1
    return result



fun1 = count_items(["a", "b", "a", "c", "a"])   # {"a": 3, "b": 1, "c": 1}
fun2 = count_items([]) 

print(fun1)
print(fun2)