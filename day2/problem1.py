def total_marks(marks):
    for m in marks: 
        total = total + m
    print(total)
# in this code have two main issue first is not delcare total varible and 2nd one is use print rather than
#using return 

# correct code is

def total_marks(marks):
    total = 0
    for m in marks: 
        total = total + m
    return total 

obj = total_marks([70, 80, 90])
print(obj)
 