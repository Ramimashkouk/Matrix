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
print()

a = matrix.Matrix(5 , 3 , [1, -5, 0, 2, 0, 4, 3, -7, 5, 6, 3, -8, 2, 3, 7])
b = matrix.Matrix(3, 4 , [7, 9, 0, -6,-2, 0, 3, -7, 8, -9, 0, 0])

"""c =matrix.Matrix(5, 4)
print('the multibly of matrices a and b is: ')
c = a * b 
c.showArr()"""

print()
#a.transposition().showArr()
#s= matrix.Matrix(4, 3, [1, -1, 0, -1, 2, 1, 2, -3, -1, 0,1,1])
s = matrix.Matrix(5, 4, [5, 3 , 2 , -6 , 0, 2, 0 , 3, -4, 0, 3, -7, 0, 0,0, 2,1, -5, 0, 4])
s.pseudoInverse().showArr()
