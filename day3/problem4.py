def first_negative(l):
    i = 0

    while i < len(l):
        if l[i] < 0:
            return l[i]

        i += 1

    return None

fun1 = first_negative([4, 0, -3, -8])   # -3
fun2 = first_negative([1, 2])

print(fun1)
print(fun2)

#ree