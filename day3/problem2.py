def index_of(l , target):
    for i, value in enumerate(l):
       
            
        if value == target:
            return(i)
    return -1
        
        

fun = index_of(["a", "b", "c", "b"], "b")   # 1
fun1 = index_of([], "x")  

print(fun)
print(fun1)