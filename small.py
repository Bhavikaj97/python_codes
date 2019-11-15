def binary(arr, l, h, ele):
    if l <= h:
        mid = int((l+h) / 2)
        if arr[mid] == ele:
            return mid
        elif arr[mid] > ele:
            binary(arr, l, (mid - 1), ele)
        else:
            binary(arr, (mid + 1), h, ele)
    else:
        return -1

N = int(input())
power_s = [int(x) for x in input().split()]
Q = int(input())
count = 0
sum = 0
for i in range(Q):
    power_b = int(input())
    index = binary(power_s, 0, len(power_s), power_b)
    for j in range(index):
        while count < index:
            count += 1
            sum = sum + power_s[i]
    print(count, end=" ")
    print(sum)