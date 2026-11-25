def most_common_word(s:str):
    dic = {}
    s = s.lower()

    
    for i in s.split(" "):
        if i not in dic:
          dic[i] = 0
    dic[i] += 1

    print(dic)    



fun1 = most_common_word("The cat sat. The dog ran!")   # "the"
fun2 = most_common_word("Cat? cat, CAT. dog")          
fun3 = most_common_word("b a b a")


print(fun1)
print(fun2)
print(fun3)