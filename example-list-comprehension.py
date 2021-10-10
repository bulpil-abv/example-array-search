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


def make_list_expression():
    """
    List demo
    Power 2 even numbers in list A.
    """
    A=[1,2,3,4,5,7,12,9,6]
    B=[]
    for x in A:
        if x%2 == 0:
            B.append(x**2)
    print(B)

    B=[x**2 for x in A if x%2==0]
    print(B)

make_list_comprehension(4)
make_list_append(4)
make_list_expression()