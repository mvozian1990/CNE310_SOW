def lone_sum(a, b, c):
    if a == b and b == c:
        return 0
    elif a == c:
        return b
    elif b == c:
        return a
    elif a == b:
        return c
    else:
        return a + b + c


if __name__ == '__main__':

    x = int(input())
    y = int(input())
    z = int(input())

    result = lone_sum(x, y, z)
    print("Input: " + str(x) + ", " + str(y) + ", " + str(z))
    print("Result: " + str(result))
