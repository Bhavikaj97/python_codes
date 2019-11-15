N = 1
st = []
top = -1
for i in range(N):
    s = input()
    for j in range(len(s)):
        if (top == -1) and ((s[j] == ')') or (s[j] == '}') or (s[j] == ']')):
            top += 1
            break
        elif (s[j] == '(') or (s[j] == '{') or (s[j] == '['):
            top += 1
            st.append(s[j])
        elif (s[j] == ')') and (st[top] == '('):
            st.pop()
            top -= 1
        elif (s[j] == ']') and (st[top] == '['):
            st.pop()
            top -= 1
        elif (s[j] == '}') and (st[top] == '{'):
            st.pop()
            top -= 1
        else:
            break
    if top == -1:
        print("YES")
    else:
        st = []
        top = -1
        print("NO")
