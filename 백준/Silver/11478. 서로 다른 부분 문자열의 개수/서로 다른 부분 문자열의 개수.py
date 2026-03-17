import sys
S=sys.stdin.readline().strip()
S_list=[]
for i in range(len(S)):
    for j in range(len(S)-i):
        S_list.append(S[j:j+i+1])
print(len(set(S_list)))
        