def fizz_buzz(n):
    l = []
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            l.append("fizzbuzz")
        
        elif i % 3 == 0:
            l.append("fizz")
        elif i % 5 == 0:
            l.append("buzz")
        else:
            l.append(i)
    return l


    
obj = fizz_buzz(15)

print(obj)
        
