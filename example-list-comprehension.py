def make_list_comprehension(y):
    """
    list demo 1
    2 power y by comprehension
    """
    A = [2 ** x for x in range(y)]
    print(A)


def make_list_append(y):
    """
    list demo 2
    2 power y by append
    pop() demo
    """
    A = []
    for x in range(y):
        A.append(2**x)
    print(A)
    print(A.pop())
    print(A.pop())
    print(A)


make_list_comprehension(4)
make_list_append(4)
