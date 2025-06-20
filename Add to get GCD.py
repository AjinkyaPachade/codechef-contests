import math

T = int(input())

for _ in range(T):
    X, Y = map(int, input().split())
    if math.gcd(X,Y)>1:
        print(0)
        
    elif math.gcd(X+1, Y)>1 or  math.gcd(X, Y+1)>1:
        print(1)
        
    else:
        print(2)