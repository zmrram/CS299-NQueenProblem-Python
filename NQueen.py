solution = []
            
def solveNQueens(size):
    global solution
    if(placeQueens(0,size)):
        for i in range(0,size):
            for j in range(0,size):
                if solution[i][j] == 1:
                    print("[Q]", end = "")
                else:    
                    print("[ ]", end = "")
            print()
    else:
        print("No Solution")
    

def placeQueens(queen, size):
    global solution
    if queen == size:
        return True
    for row in range (0, size):
        if (checkRCD(solution,row, queen)):
            solution[row][queen] = 1
            if (placeQueens(queen + 1, size)):
                return True
            solution[row][queen] = 0
    return False

def checkRCD(matrix, row, col):
    
    for i in range (0,col):
        if matrix[row][i] == 1:
            return False
    x = row
    y = col
    while( x >= 0 and y >= 0):
        if (matrix[x][y] == 1):
            return False
        x = x - 1
        y = y - 1
    x = row
    y = col
    while (x < len(matrix) and y >= 0):
        if (matrix[x][y] == 1):
            return False
        x = x + 1
        y = y - 1
    return True
            
def main():
    print("Test size: 5")
    size = 8
    global soluion
    for i in range(0,size):
        solution.append([])
    for row in range(0,size):
        for column in range(0,size):
            solution[row].append(0)
    solveNQueens(size)
    
if  __name__ =='__main__':
    main()
