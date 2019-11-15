N = int(input())
dic = {}
for i in range(N):
    r,p = input().split()
    if int(p) in dic:
        dic[int(p)].append(r)
        continue
    dic[int(p)] = [r]

lst =[]
for x in dic:
    lst.append(int(x))
max_point = max(lst)
lst_2 = (dic[max_point])
lst_2.sort()
print(lst_2[0])



