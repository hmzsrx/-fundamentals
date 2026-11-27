def row_sums(n):
        new = []
        # for i in n:
        #     a = sum(i)
        #     new.append(a)
        # return new   
        return [sum(i)for i in n]          
def col_sums(n):
    a = n[0]
    b = n[1]

    # new_list = []

    # for i in range(len(a)):
    #       new_list.append(a[i] + b[i]) 
    # return new_list   

    return [a[i] + b[i] for i in range(len(a))]

    

      
fun1 = row_sums([[1, 2], [3, 4]])   # [3, 7]
fun2 = col_sums([[1, 2], [3, 4]])   # [4, 6]


print(fun1)
print(fun2)