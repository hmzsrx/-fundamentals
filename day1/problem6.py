def sum_num(nums):

    count = 0
    for i in nums:
        count += i
    return count


def average(nums):

    counter = 0
    add = 0
    if nums == []:
        raise ValueError ("empty string")
    for i in nums:
        add += i 
        counter += 1

    return add / counter 


fun = sum_num([2, 4, 6])   
fun2 = sum_num([])              
fun3 = average([2, 4, 6])

print(fun)
print(fun2)
print(fun3)