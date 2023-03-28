def rotate(matrix):

    i = 0
    j = len(matrix) - 1
    n = len(matrix)
    while j > i:
        matrix[i], matrix[j] = matrix[j], matrix[i]
        i += 1
        j -= 1

    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    print(matrix)

# Test case
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(rotate(matrix))