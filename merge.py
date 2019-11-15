def mergesort(arr):
    if len(arr) > 1:
        mid = int(len(arr) / 2)
        arr1 = mergesort(arr[0:mid])
        arr2 = mergesort(arr[mid:])
        i = 0
        j = 0
        result = []
        while i <= len(arr1) or j <= len(arr2):
            if arr1[i] <= arr2[j]:
                result.append(arr1[i])
                i += 1
            else:
                result.append(arr2[j])
                j += 1

            if i >= len(arr1):
                result.extend(arr2[j:])
                return result
            elif j >= len(arr2):
                result.extend(arr1[i:])
                return result
    else:
        return arr

arr = [6,2,5,12,1,4]
n = len(arr)
result = mergesort(arr)
for i in result:
    print(i, end=", ")

