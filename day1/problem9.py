def reverse_str(s:str):

    rev = ""

    for i in s:
        rev = i + rev

    return rev

fun = reverse_str("hdxpert")
print(fun) 