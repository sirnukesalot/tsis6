def pal(s):
    rev = ''.join(reversed(s))
    if (s == rev):
        return True
    return False
  
s = "abba"
ans = pal(s)
  
if (ans):
    print("Yes")
else:
    print("No")