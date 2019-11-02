import copy

class Matrix:

    def __init__(self, m, n, eleList = []):
        self.rows, self.cols = (m, n)
        self.arr = [[0 for i in range(self.cols)] for j in range(self.rows)]
        k = 0

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

    def add(self, row1, row2):
        row = []
        for i in range(len(row1)):
            row.append(row1[i] + row2[i]) # why row[i] = row1[i] + row2[i] didn't work
        return row

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
                row = []
                if j<i and self.arr[i][j] !=0:
                    self.arr[i] = self.add(
                        self.arr[i] , 
                        self.multiply(j, -(self.arr[i][j])/self.arr[j][j])
                        )
    def rank(self):
        self.upperTriMat()
        rank = 0
        for i in range(self.rows):
            for j in range(self.cols):
                if self.arr[i][j] !=0:
                    rank += 1
                    break
        return rank
