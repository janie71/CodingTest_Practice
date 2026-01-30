import sys

T = int(sys.stdin.readline().strip())
for _ in range(T):
    a, b = map(int, sys.stdin.readline().split())
    mod1 = max(a,b)
    mod2 = min(a,b)
        
    while (mod1%mod2!=0):
        tmp = mod1%mod2
        mod1 = mod2
        mod2 = tmp

    gcd = mod2
    lcm = (a*b)//gcd
    print(lcm)