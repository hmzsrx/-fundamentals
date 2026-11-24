def fizz_buzz(n):
    L = []
    for i in range(1, n+1):
  

        if i / 3 == 0:
            print(i)
            
            L.append("Fizz")

        elif i / 5 == 0:
            L.append('buzz')
        

    return L

obj = fizz_buzz(5)

print(obj)
        
