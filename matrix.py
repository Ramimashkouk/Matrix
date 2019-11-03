import copy

class Matrix:

    def __init__(self, m, n, eleList = []):
        self.rows, self.cols = (m, n)
        self.arr = [[0 for i in range(self.cols)] for j in range(self.rows)]
        k = 0

        if eleList != []:
            for i in range(self.rows):
                for j in range(self.cols):
                    self.arr[i][j] = eleList[k]
                    k+=1

    def showArr(self):
        for i in range(self.rows):
            print(self.arr[i])

    def multiply(self, row, num):
        A = copy.deepcopy(self.arr)
        for j in range(self.cols):
            A[row][j] *= num
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
        if self.arr[0][0] == 0:
            for k in range(self.rows):
                if self.arr[k][0] != 0:
                    row = self.arr[0]
                    self.arr[0] = self.arr[k]
                    self.arr[k] = row
                    break
        for j in range(self.cols):
            for i in range(self.rows):
                if j<i and self.arr[i][j] !=0:
                    row = Matrix(1, self.cols, self.arr[i])
                    row = row + Matrix(1, self.cols, 
                        self.multiply(j, -(self.arr[i][j])/self.arr[j][j]))

                    self.arr[i] = row.arr[0]
    def rank(self):
        self.upperTriMat()
        rank = 0
        for i in range(self.rows):
            for j in range(self.cols):
                if self.arr[i][j] !=0:
                    rank += 1
                    break
        return rank
