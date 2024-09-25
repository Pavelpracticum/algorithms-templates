# def fibo(n):
#     a = 0
#     b = 1
#     for _ in range(n):
#         a, b = b, a + b
#         print(a, b)
#     return a

# print(fibo(8))

def fibo_recurs(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fibo_recurs(n-1) + fibo_recurs(n-2)

n = int(input())
print(fibo_recurs(n))
