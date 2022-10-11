def matrixZeros(matrix):
    ROWS, COLS = len(matrix), len(matrix[0])

    for i in range(ROWS):
        for j in range(COLS):
            
            if matrix[i][j] == 0:
                for k in range(COLS):
                    if matrix[i][k] != 0:
                        matrix[i][k] = "x"

                for l in range(ROWS):
                    if matrix[l][j] != 0:
                        matrix[l][j] = "x"
    
    for row in range(ROWS):
        for col in range(COLS):
            if matrix[row][col] == "x":
                matrix[row][col] = 0

    return matrix


matrix = [
    [0,1,2,0],
    [3,4,5,2],
    [1,3,1,5]
]


print(matrix)
matrix = matrixZeros(matrix)
print(matrix)