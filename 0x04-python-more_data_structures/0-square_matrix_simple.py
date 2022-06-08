#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newMatrix = []
    i = 0
    for x in matrix:
        newMatrix.append([])
        for y in matrix[i]:
            newMatrix[i].append(y**2)
        i += 1
    return (newMatrix)
