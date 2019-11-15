def bubblesort(arr):
    n = len(arr)
    for i in range(n):

        for j in range(0,(n-i-1)):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]


arr=[6 ,2 ,8 ,8 ,9 ,3]
bubblesort(arr)
for i in range (len(arr)):
    print ("%d" % arr[i], end=" ")

