def recursivePower(a:int, b:int) -> int:
    if a == 0 and b == 0:
        return 1
    elif a == 0:
        return 0
    elif b == 0: 
        return 1
    else:
        return a*recursivePower(a, b-1)
    
print(recursivePower(3, 4))