def max2(x, y):
    """
    return maximum value
    of x and y.
    if equal return "equal".
    """
    if x>y:
        return x
    elif y>x:
        return y
    return "equal"


def test_max2():
    x, y = 1, 2
    m = max2(x, y)
    if m == 2:
        print("test1-ok")
    else:
        print("test1-fail")


test_max2()
