def is_sorted(*lst):
    for w in lst[:]:
        words = list(w)
        word = sorted(words)
        if word == words:
            return True
        else:
            return False


print(is_sorted('gin'))

