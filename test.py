s = input()
T = int(input())
for _ in range(T):
    k = int(input())
    for i in range(len(s)-k+1):
        m = int(i+((k+1)/2))
        for j in range(i, m):
            n = i+k-1
            if s[j] != s[n]:
                break
        else:
            print(k)


#import argparse
# dirname
# query

