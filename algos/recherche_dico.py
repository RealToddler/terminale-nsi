def foo(elem, l): # version récursive
    if len(l)==1 :
        return 0
    m = len(l)//2
    if l[m] == elem :
        return m
    elif l[m] > elem :
        return foo(elem, l[:m])
    else :
        return m + foo(elem, l[m:])