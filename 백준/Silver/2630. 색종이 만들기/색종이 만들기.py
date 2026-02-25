import sys

N = int(input())
List = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

blue = 0
white = 0


def paper(C, l1, l2):
    global blue, white
    for i in range(C):
        for j in range(C):
            if List[l1][l2] != List[l1 + i][l2 + j]:
                paper(C // 2, l1, l2)
                paper(C // 2, l1 + C // 2, l2)
                paper(C // 2, l1, l2 + C // 2)
                paper(C // 2, l1 + C // 2, l2 + C // 2)
                return 0

    if List[l1][l2] == 0:
        white += 1
    elif List[l1][l2] == 1:
        blue += 1
    return 0


paper(N, 0, 0)
print(white)
print(blue)