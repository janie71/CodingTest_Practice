def check_sudoku(sudoku):
    #가로
    for row in sudoku:
        if len(set(row)) != 9:
            return 0

    #세로
    for i in range(9):
        temp=[]
        for j in range(9):
            temp.append(sudoku[j][i])
        if len(set(temp)) !=9:
            return 0
	#3*3
    for i in range(0,9,3):
        for j in range(0,9,3):
            temp=[]
            for k in range(i, i+3):
                for l in range(j, j+3):
	                temp.append(sudoku[k][l])
            if len(set(temp)) !=9:
                return 0
    return 1
            
T = int(input())

for tc in range(1, T + 1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    print(f'#{tc} {check_sudoku(sudoku)}')