def fibonacci(num:int) -> int:
    if num == 0:
        return 0
    elif num < 0:
        return 0
    elif num == 1:
        return 1
    else:
        return int(fibonacci(num-1) + fibonacci(num-2))
    

print(fibonacci(46))