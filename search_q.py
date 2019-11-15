arr_len = int(input())
arr = [int(num) for num in input().split()]
q_len = int(input())
# arr_len = 6
# arr = [1, 1, 12, 0, 9, 5]
# q_len = 1
print(arr[1])

for i in range(q_len):
    count = 0
    q = int(input())
    for elem in arr:
        if elem == q:
            count += 1
    if count != 0:
        print(count)
    else:
        print("NOT PRESENT")

