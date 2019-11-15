N = int(input())
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]
for i in range(N):
    C = A[i] + B[i]
    print(C, end = " ")