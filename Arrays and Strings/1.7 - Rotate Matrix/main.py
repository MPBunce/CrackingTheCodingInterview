def rotateMatrixClockwise(matrix):

    n = len(matrix[0])

    for i in range(n // 2 + n % 2):
        for j in range(n // 2):
            tmp = matrix[n - 1 - j][i]
            matrix[n - 1 - j][i] = matrix[n - 1 - i][n - j - 1]
            matrix[n - 1 - i][n - j - 1] = matrix[j][n - 1 -i]
            matrix[j][n - 1 - i] = matrix[i][j]
            matrix[i][j] = tmp

    return matrix


def rotateMatrixCounterClockwise(matrix):

    n = len(matrix[0])
    
    for i in range(n // 2 + n % 2):
        for j in range(n // 2):
            tmp = matrix[n - 1 - j][i]
            matrix[n - 1 - j][i] = matrix[n - 1 - i][n - j - 1]
            matrix[n - 1 - i][n - j - 1] = matrix[j][n - 1 -i]
            matrix[j][n - 1 - i] = matrix[i][j]
            matrix[i][j] = tmp

    return matrix


myMatrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(myMatrix)

#clockwise
myMatrix = rotateMatrixClockwise(myMatrix)
print(myMatrix)

#counter clockwise
myMatrix = rotateMatrixCounterClockwise(myMatrix)
print(myMatrix)