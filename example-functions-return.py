def max2(x, y):
    """
    return maximum value
    of x and y.
    if equal return "equal".
    """
    if x > y:
        return x
    elif y > x:
        return y
    return "equal"


def test1_max2():
    x, y = 1, 2
    m = max2(x, y)
    if m == 2:
        print("test1-ok")
    else:
        print("test1-fail")


def test2_max2():
    x, y = 1, 1
    m = max2(x, y)
    if m == "equal":
        print("test2-ok")
    else:
        print("test2-fail")


def test3_max2():
    x, y = 2, 1
    m = max2(x, y)
    if m == 2:
        print("test3-ok")
    else:
        print("test3-fail")


test1_max2()
test2_max2()
test3_max2()


def max3(x, y, z):
    """
    Compare three parameters
    :param x:
    :param y:
    :param z:
    :return: largest
    """
    m = max(y,z)
    if m != "equal":
        n = max2(x, m)
        if n != "equal":
            return n
        return m
    return max2(x,y)


def test1_max3():
    x, y, z = 1, 2, 3
    m = max3(x, y, z)
    if m == 3:
        print("test1-ok")
    else:
        print("test1-fail")


def test2_max3():
    x, y, z = 3, 3, 2
    m = max3(x,y,z)
    if m == 3:
        print("test2-ok")
    else:
        print("test2-fail")


def test3_max3():
    x,y,z=2,3,3
    m = max3(x,y,z)
    if m == 3:
        print("test3-ok")
    else:
        print("test3-fail")


test1_max3()
test2_max3()
test3_max3()