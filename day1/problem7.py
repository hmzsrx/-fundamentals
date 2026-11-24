def count_vowels(s:str):
    vowels = ['a','e','i','o','u']
    counter = 0
    for i in s:
      if i.lower() in vowels:
         counter += 1
    return counter

fun1 = count_vowels("Hamza")         
fun2 = count_vowels("PYTHON")        
fun3 = count_vowels("")  

print(fun1)
print(fun2)
print(fun3)