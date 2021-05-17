# This function contains a bug, please fix it
def lone_sum(a, b, c):
    if a >= b:
        return c
    elif a == c:
        return b
    elif b == c:
        return a
    elif a == b and a == c and b == c:
        return 0
    else:
        return a+b+c


if __name__ == '__main__':
    result = lone_sum(1, 3, 5)
    print("The result: " + str(result))
