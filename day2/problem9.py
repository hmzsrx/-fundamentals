
def passed(students, cutoff):

   for i in students:
    
    if i["score"] > cutoff:
      return i['name']

    


fun = passed([{"name": "Ali", "score": 72}, {"name": "Sara", "score": 55}], 
60)   # ["Ali"]

print(fun)