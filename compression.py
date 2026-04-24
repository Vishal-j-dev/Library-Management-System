s='aaabbcc'
result=''
count=1
for i in range(1,len(s)):
    if s[i]==s[i-1] and i-1>=0:
        count+=1
    else:
        result+=s[i-1]+str(count)
        count=1
result+=s[i-1]+str(count)
print(result)
