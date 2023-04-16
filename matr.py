b = eval(input())
def sdsd(matrix):
    a = len(matrix)
    for i in range(a):
        for j in range(i, a):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(a):
        matrix[i] = matrix[i][::-1]
    return matrix
print(sdsd(b))
    











