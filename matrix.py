import copy
from fractions import Fraction

class Matrix:

    def __init__(self, m, n, eleList = []):
        self.rows, self.cols = (m, n)
        self.arr = [[Fraction(0.0) for i in range(self.cols)] for j in range(self.rows)]
        k = 0

        if eleList != []:
            for i in range(self.rows):
                for j in range(self.cols):
                    self.arr[i][j] = eleList[k]
                    k+=1

    def showArr(self):
        if self.arr is None:
            return
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                f = Fraction(self.arr[i][j])
                if f.numerator == 0:
                    row.append(' 0 ')
                elif f.denominator == 1:
                    row.append(' {} '.format(str(f.numerator)))
                else:
                    row.append(str(f.numerator) + '/' + str(f.denominator))
            print(row)

    def multiply(self, row, num):
        numb = Fraction(str(num))
        A = copy.deepcopy(self.arr)
        for j in range(self.cols):
            A[row][j] *= numb
        return A[row]

    def __add__(self, A):
        array = Matrix(A.rows, A.cols)
        if A.rows == self.rows and A.cols == self.cols:
            for i in range(A.rows):
                for j in range(A.cols):
                    array.arr[i][j] = A.arr[i][j] + self.arr[i][j]
            return array
        else:
            print('The dementions of matrices do not match')

    def upperTriMat(self):
        A = Matrix(self.rows, self.cols)
        A.arr = copy.deepcopy(self.arr)
        if A.arr[0][0] == 0:
            for k in range(A.rows):
                if A.arr[k][0] != 0:
                    row_substitute = A.arr[0]
                    A.arr[0] = A.arr[k]
                    A.arr[k] = row_substitute
                    break
        for j in range(A.cols):
            for i in range(A.rows):
                if j<i and A.arr[i][j] !=0:
                    if A.arr[j][j] == 0:
                        row_substitute = A.arr[i]
                        A.arr[i] = A.arr[j]
                        A.arr[j] = row_substitute
                        continue
                    row = Matrix(1, A.cols, A.arr[i])
                    row = row + Matrix(1, A.cols, 
                        A.multiply(j, -(A.arr[i][j])/Fraction(A.arr[j][j])))
                    A.arr[i] = row.arr[0]
        return A
    
    def rank(self):
        A = Matrix(self.rows, self.cols)
        A = self.upperTriMat()
        rank = 0
        for i in range(A.rows):
            for j in range(A.cols):
                if A.arr[i][j] !=0:
                    rank += 1
                    break
        return rank

    def transposition(self):
        A = Matrix(self.cols, self.rows)
        for i in range(self.rows):
            for j in range(A.cols):
                A.arr[j][i] = self.arr[i][j]
        return A

    def inverse(self):

        if self.rows != self.cols:
            print('The matrix is not square')
            return

        # being sure that the first column is not a zeros vector
        A = Matrix(self.rows, self.cols)
        A = self.upperTriMat()
        det = 1
        for i in range(A.rows):
            det *= A.arr[i][i]
        if det == 0:
            print('Determinant is zero, therefore inverse matrix doesn\'t exist')
            return

        # create an identity matrix
        identity = Matrix(self.rows, self.cols)
        mat2 = Matrix(self.rows, self.cols*2)
        for i in range(self.rows):
            for j in range(self.cols):
                if i == j:
                    identity.arr[i][j] = 1
                else:
                    identity.arr[i][j] = 0
        
        # make the augmented matrix
        for i in range(self.rows):
            row1 = self.arr[i]
            row2 = identity.arr[i]
            mat2.arr[i] = row1 + row2
            

        for j in range(self.cols):
            # replace the line if the element in the main diagonal is zero
            if mat2.arr[j][j] == 0:
                for i in range(mat2.rows):
                    if mat2.arr[i][j] != 0:
                        row_substitute = mat2.arr[i]
                        mat2.arr[i] = mat2.arr[j]
                        mat2.arr[j] = row_substitute
                        break

            # make the element in the main diagonal equal one
            if mat2.arr[j][j] !=1:
                mat2.arr[j] = mat2.multiply(j, Fraction(1, mat2.arr[j][j]))


            # make the elements in the left side of the augmented matrix zeros
            for i in range(mat2.rows):
                if i != j:
                    row = Matrix(1, mat2.cols, mat2.arr[i])
                    row = row + Matrix(1, mat2.cols, 
                        mat2.multiply(j, -(mat2.arr[i][j])/mat2.arr[j][j]))
                    mat2.arr[i] = row.arr[0]

        inv = Matrix(mat2.rows, self.cols)

        for i in range(mat2.rows):
            inv.arr[i] = mat2.arr[i][self.cols:]
        return inv
