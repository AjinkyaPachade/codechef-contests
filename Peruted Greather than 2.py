T = int(input())
for _ in range(T):
    X, Y, Z = map(int, input().split())
    if X > 0 and Y > 0 and Z == 0:
        print("No")
    else:
        print("Yes")
