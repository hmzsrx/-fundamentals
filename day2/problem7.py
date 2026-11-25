def invert(d):

    result = {}

    for i in d:
        if d[i] in result:
            raise ValueError("duplicate value")

        result[d[i]] = i

    return result


fun = invert({"a": 1, "b": 2})   # {1: "a", 2: "b"}
fun1 = invert({"a": 1, "b": 1})


print(fun)
print(fun1)