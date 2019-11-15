def selection(a):
    n = len(a)
    for i in range(n):
        min = i
        j= i+1
        for j in range (i+1, n):
            if a[j] < a[min]:
                min = j

        a[min], a[i] = a[i], a[min]

a = [64, 25, 12, 22, 11]
selection(a)
for i in range (len(a)):
    print ("%d" % a[i])




