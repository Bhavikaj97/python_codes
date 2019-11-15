n = int(input())
st = input()
st_length = int(len(st))
temp = []
temp_length = len(temp)
st2 = ""

for i in range(int(st_length)-1, int(st_length/2)-1, -1):
    temp.append(st[i])
st2 = st2.join(temp)
m = len(st2)
for j in range(int(m)):
    if st2[j] == ']':
        st2 = '['
    elif st2[j] == ')':
        st2[j] = '('
    else:
        st2[j] = '{'


if st == st2:
    print("yes")
else:
    print("no")