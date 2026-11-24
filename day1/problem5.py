def max_of_three(a,b,c):

    if a > b or a > c:
        return a
    elif b > a or b > c:
        return b
    else:
        return c

fun1 = max_of_three(3, 9, 4)    
print(fun1) 
# 9
fun2 = max_of_three(-1, -5, -2)  # -1
print(fun2)

fun3 = max_of_three(7, 7, 2)
print(fun3) 
