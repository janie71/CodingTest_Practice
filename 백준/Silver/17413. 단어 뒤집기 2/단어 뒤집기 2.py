import sys
S=sys.stdin.readline().strip()
check=0
res=''
temp=''
for i in S:
    if i=="<":
        check=1
        if temp!='':
            res+=temp[::-1]
            temp=''
        temp+=i
    elif i==">":
        check=0
        res+=temp+'>'
        temp=''
    elif i==' ' and check==0:
        res+=temp[::-1]+' '
        temp=''
    else:
        temp+=i
if temp!='':
    res+=temp[::-1]
print(res)