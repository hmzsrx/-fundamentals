def find_pair(num, target):

    for i in range(len(num)):
        for j in range(i + 1 , len(num)):
           if num[i] + num[j] == target:
               return i, j
        



fun = find_pair([500, 1200, 300, 700], 1000)  
print(fun)