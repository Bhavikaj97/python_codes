def findsubstring(s, ss):
    if ss in s:
        return True
    else:
        return False


s = "learning python programming"
ss = "learning"
result = findsubstring(s, ss)
print("%s" %result)