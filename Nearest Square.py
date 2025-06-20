import math 

T=int(input())

for _ in range(T):
    N = int(input())
    A = int(math.floor(N**0.5))
    print(A*A)

