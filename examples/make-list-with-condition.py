def make_list_with_condition(A:list):
    """
    Makes a list B from A
    with the elements which can be divided by 7
    """
    B = [x for x in A if x % 7 == 0]
    return B

def test_make_list_with_condition():
    A=list(range(1,16,1))           # one way to make a list
    A=[x for x in range(1,16)]      # another way to make a list
    A=(x for x in range(1,16))      # make a tuple - immutable
    C=[7,14]
    print(A)
    B=make_list_with_condition(A)
    print(C)
    print("test-OK" if C==B else "test-fail")


test_make_list_with_condition()

