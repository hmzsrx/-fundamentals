
def word_lengths(text):
    words = text.split(" ")

    result = {}

    for word in words:
        result[word] = len(word)

    return result


fun = word_lengths("learn python daily")   
print(fun)