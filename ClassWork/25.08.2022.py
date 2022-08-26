
def fibo(a=10):
    if a == 1 or a == 2:
        return 1
    else:
        return fibo(a - 1) + fibo(a - 2)


print(fibo())
