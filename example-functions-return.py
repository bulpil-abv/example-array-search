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


def test1_max2():
    x, y = 1, 2
    m = max2(x, y)
    if m == 2:
        print("test1-ok")
    else:
        print("test1-fail")


def test2_max2():
    x,y = 1,1
    m = max2(x,y)
    #TODO

def test3_max2():
    x,y=2,1
    #TODO

test1_max2()
test2_max2()
test3_max2()
