# Составить список простых множителей натурального числа N

n = int(input())
list = []
def f(n, d):
    while d <= n:
        if n % d == 0:
            list.append(d)
            n //= d
        elif n % d != 0:
            d += 1
f(n, 2)
print(list)
