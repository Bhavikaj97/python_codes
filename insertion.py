def insertion(arr):
    n = len(arr)
    for i in range(1,n):
        key = arr[i]
        j= i-1
        while j>=0 and arr[j]>key:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key
arr = [4, 3, 2, 10, 12, 1, 5, 6]
insertion(arr)
for i in range (len(arr)):
    print ("%d" % arr[i])

