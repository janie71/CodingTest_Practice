import itertools, sys
n,m=map(int, sys.stdin.readline().split())
nlist=list(map(int, sys.stdin.readline().split()))
nlist=list(set(nlist))
nlist.sort()
clist=list(itertools.combinations_with_replacement(nlist, m))
#clist 오름차순만들기
clist.sort()

for i in clist:
    print(' '.join(list(map(str,i))))