def second_largest(n):

        try:
            if len(n) <= 1:
                raise ValueError("incorrect value") 

        
            result = [] 

            for i in range(len(n)):
                for j in range(i+1 , len(n)):
                    if n[i] > n[j]:
                        n[i],n[j] = n[j],n[i]

            for i in n:
                if i not in result:
                    result.append(i)
                        
            
            return result[-2]
        except ValueError as e:
            print("error:" , e)



fun1 = second_largest([4, 9, 2, 7])   # 7
fun2 = second_largest([5, 5, 3,4])      
fun3 = second_largest([8]) 
print(fun1)
print(fun2)
print(fun3)