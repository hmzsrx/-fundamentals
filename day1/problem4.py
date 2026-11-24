def grade(score):
    try:
        if score > 100 or score <0:
             raise ValueError("value enter btween 0-100")     
        elif score >= 90:
            return "A"
        elif score >= 75 and score <= 89:
            return "B"
        elif score >= 60 and score <= 74:
            return "C"
        elif score < 60:
            return "F"  
    except ValueError as e:
        return e        
    
fun1 = grade(95)     
fun2 = grade(75)     
fun3 = grade(59)     
fun4 = grade(120) 

print(fun1)
print(fun2)
print(fun3)

print(fun4)

    
