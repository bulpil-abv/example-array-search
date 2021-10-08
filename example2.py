A = [0] * 1000
top = 0
x = int(input())
while x != 0:
    A[top] = x
    top += 1
    x = int(input())
print(A)
