N = int(input())
a = [int(x) for x in input().split()]

def max_sum(i):
    sum = 0
    k = 3
    prev_index = i
    next_index = prev_index + 3
    while next_index <= N:
        for i in range(prev_index,next_index):
            sum = sum + a[i]
        prev_index = next_index
        next_index = prev_index + k
        k += 1
    arr.append(sum)

arr = []
arr.append(a[0])
for i in range(N-2):
    max_sum(i)
arr.append(a[N-2])
arr.append(a[N-1])
print(max(arr))


