def digit_sum(n):
    if n < 0:
        raise ValueError("invalid num")

    total = 0

    while n > 0:
        digit = n % 10
        total += digit
        n = n // 10

    return total


fun = digit_sum(4053)   # 12
fun1 = digit_sum(0)      
# 0
fun2 = digit_sum(-5)

print(fun)
print(fun1)
print(fun2)

#re