def isbalanced(word):
    s=[]
    for k in word:
        if k=='(':
            s.append(k)
        else:
            if len(s)==0:
                return False
            else:
                s.pop()

    if len(s)==0:
        return True
    return False

a='()())'
print(isbalanced(a))