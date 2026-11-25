def merge_stock(a, b):
    new_dic = {}
    for i in a:
      for j in b:
        if i == j:
          new_dic[i] =  a[i] + b[j] 
    new_dic[i] = a[i]
    new_dic[j] = b[j]
    print(new_dic)
          
          



fun = merge_stock({"mouse": 5, "keyboard": 2}, {"mouse": 3, "webcam": 1})
print(fun)