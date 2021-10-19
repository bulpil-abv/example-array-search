# Recursion, два условия
# 1.Рекурентный случай
# 2.Крайний случай

def matryoshka(n):
    if n == 1:
        print("Матрешечка")
    else:
        print("Верх матрешки n=", n)
        matryoshka(n - 1)
        print("Низ матрешки n=", n)


matryoshka(5)

import graphics as gr

window = gr.GraphWin("Russian game", 800, 800)
alpha=0.2


def fractal_rectangle(A, B, C, D, depth=5):
    if depth < 1:
        return
    for M, N in (A, B), (B, C), (C, D), (D, A):
        gr.Line(gr.Point(*A), gr.Point(*B)).draw(window)
        A1 = (A[0] * (1 - alpha) + B[0] * alpha, A[1] * (1 - alpha) + B[1] * alpha)
        B1 = (B[0] * (1 - alpha) + C[0] * alpha, B[1] * (1 - alpha) + C[1] * alpha)
        C1 = (C[0] * (1 - alpha) + D[0] * alpha, C[1] * (1 - alpha) + D[1] * alpha)
        D1 = (D[0] * (1 - alpha) + A[0] * alpha, D[1] * (1 - alpha) + A[1] * alpha)
    fractal_rectangle(A1, B1, C1, D1, depth - 1)


fractal_rectangle((100,100),(500,100),(500,500),(100,500),10)
print("End")

#my_rectangle = gr.Rectangle(gr.Point(2, 4), gr.Point(4, 8))
#my_rectangle.draw(window)

# Factorial
# f(0)=1
# f(n)=f(n-1)*n

def factorial(n):
    assert n>=0
    if n == 0:
        return 1
    return   factorial(n-1)*n

print(factorial(3))