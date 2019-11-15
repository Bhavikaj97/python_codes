arr_length = int(input())
arr = [int(x) for x in input().split()]

for m in range(arr_length-1, -1, -1):
    print(arr[m])
