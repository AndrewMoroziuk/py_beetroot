def persistence(n):
    """
    Звичайна класична функція.
    """
    res = 0
    while len(str(n)) > 1:
        d = 1
        for i in str(n):
            d *= int(i)
        n = d
        res += 1
    return res


def my_persistence_of_recursion(n, counter=0):
    """
    Рекурсивна функція.
    """
    if len(str(n)) >= 1:
        counter += 1
        res = 1
        for i in str(n):
            res *= int(i)
        return my_persistence_of_recursion(res, counter)
    return counter


print(persistence(999))
print(my_persistence_of_recursion(999))