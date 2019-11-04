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

    def initiate(self, A):
        for i in range(self.rows):
            for j in range(self.cols):
                self.arr[i][j] = A.arr[i][j]

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
            print('The dementions of matrices do not match for the add operation')
            return self.nonemat()

    def __sub__(self, A):
        array = Matrix(A.rows, A.cols)
        if A.rows == self.rows and A.cols == self.cols:
            for i in range(A.rows):
                for j in range(A.cols):
                    array.arr[i][j] = self.arr[i][j] - A.arr[i][j]
            return array
        else:
            print('The dementions of matrices do not match for the sub operation')
            return self.nonemat()

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
        for i in range(A.rows):
            for j in range(A.cols):
                A.arr[i][j] = self.arr[j][i]
        return A

    # a function return a none matrix, therefore the showArr() func can recieve the special cases
    def nonemat(self): 
        A = Matrix(1,1)
        A.arr = None
        return A

    def inverse(self):
        
        if self.rows != self.cols:
            print('The matrix is not square')
            return self.nonemat()

        # being sure that the first column is not a zeros vector
        A = Matrix(self.rows, self.cols)
        A = self.upperTriMat()
        det = 1
        for i in range(A.rows):
            det *= A.arr[i][i]
        if det == 0:
            print('Determinant is zero, therefore inverse matrix doesn\'t exist')
            return self.nonemat()

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

    def __mul__(self, A):
        if self.cols != A.rows:
            print('The deminations of matrices do not match for the multibly operation: m != n')
            return self.nonemat()
        mat = Matrix(self.rows, A.cols)

        """for i in range(self.rows):
            for j in range(A.cols):
                mat.arr[i][j] = 0"""

        for i in range(self.rows):
            for j in range(A.cols):
                for k in range(self.cols):
                    mat.arr[i][j] += self.arr[i][k] * A.arr[k][j]
        
        return mat

    def pseudoInverse(self, zeroFirstCol= False):

        """
            If n = m, that means the matrix is squere and we can calculate its inverse

            Otherwise, we need the pseudo Inverse. We calculate it as follow:

            A1plus = (1/(akRow * akCol) ) * akRow
            
            dk = APlus(k-1) * akCol

            ck = akCol - A(k-1) * dk

            if ck == 0 then:
                bk = ckPlus = (1/(ckRow * ckCol)) * ckRow
            else:
                bk = (1/(1+ dkRow * dkCol)) * dkRow * APlus(k-1)
            
            Bk = A(k-1) - dk * bk

            APlus(k) = [Bk, bk]

            A(k) = [a0, a1, .... k]
        """

        if self.rows == self.cols:
            return self.inverse()
        
        akRow = Matrix(1, self.rows)
        for i in range(self.cols):
            akRow.arr[0] = self.transposition().arr[i]
            akCol = akRow.transposition()

            # Calculate A1Plus
            if i == 0:
                q = akRow * akCol
                num = q.arr[0][0]
                if num == 0:    # if the first column is zero remove it and add it to the output matrix as a row
                    if self.cols == 1:
                        print('The matrix is zero matrix')
                        return self.nonemat()
                    ZFC = Matrix(self.rows, self.cols - 1)
                    for q in range(ZFC.rows):
                        for w in range(ZFC.cols):
                            ZFC.arr[q][w] = self.arr[q][w+1]
                    return ZFC.pseudoInverse(True)
                num = 1/num
                q.arr[0][0] = num
                APlus = q * akRow       # This is the A(k-1)plus, will be used in the next round
                
                #Calculate A(k-1) to be used in the next round
                A = Matrix(self.rows, 1)
                for j in range(self.rows):
                    for k in range(self.cols):
                        if k == 0:
                            A.arr[j][k] = self.arr[j][k]
                continue
            
            #Calculate dk, ck
            dk = APlus * akCol
            temp = A * dk
            ck = akCol - temp
            
            #Calculate bk
            temp2 = 0
            for j in range(ck.rows):
                if ck.arr[j][0] != 0:
                    temp2 = 1
                    break
            if temp2 == 1:
                ckCol = ck
                ckRow = ckCol.transposition()
                q = ckRow * ckCol
                num = q.arr[0][0]
                num = 1/num
                q.arr[0][0] = num
                bk = q * ckRow
            else:
                dkCol = dk
                dkRow = dkCol.transposition()
                q = dkRow * dkCol
                num = q.arr[0][0]
                num = 1/(num+1)
                q.arr[0][0] = num
                bkTemp = q * dkRow
                bk = bkTemp * APlus

            #Calculate Bk
            temp3 = dk * bk
            Bk = APlus - temp3


            #   initiate APlus. This is the A(k-1)plus, will be used in the next round
            APlus = Matrix(i+1, self.rows)
            jj=0
            for j in range(Bk.rows):
                APlus.arr[j] = Bk.arr[j]
                jj=j
            APlus.arr[jj+1] = bk.arr[0]

            #Calculate A(k-1) to be used in the next round
            A = Matrix(self.rows, i+1)
            A.initiate(self)

        if zeroFirstCol:  #  Add a zero row to the top of output
            ZFC = Matrix(APlus.rows+1, APlus.cols)
            ZFC.arr[0] = [0 for k in range(ZFC.cols)]
            for i in range(APlus.rows):
                for j in range(APlus.cols):
                    ZFC.arr[i+1][j] = APlus.arr[i][j]
            return ZFC

        return APlus
