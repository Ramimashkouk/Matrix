import matrix

"""
m = matrix.Matrix(3, 4, [-5, 6, 0,-6, 0, 2, 1, 6, 11, 0, -2, -7])

print('The rank of the given matrix is {}'.format(m.rank()))

m.showArr()"""

#m = matrix.Matrix(3, 2, [1, 6, 2, 0, 0, -2])

#m = matrix.Matrix(3, 3, [5, -2, 3, 0, 1, 7, -9, 9, 2])

#print('The rank of the given matrix is {}'.format(m.rank()))

#m.showArr()

#m = matrix.Matrix(6, 5, [1, 0, 6, 8, -5, 0, 3, 0, -6, 4, 0, 0, 0, -3, 0, 3, 2, -1, 0, 8, 0, 5, -7, 0, 2, 3, 0,0,0,0])
m = matrix.Matrix(5, 5, [0, 2, 6, 0, -5, 0, 3, -2, 3, -7, 2, 0, 1, -8, 3, -7, 2, 36, 5, -7, 2, 9, 7, 3, 0])

m.inverse().showArr()
print()

print('The rank of the given matrix is {}'.format(m.rank()))

m.upperTriMat().showArr()


