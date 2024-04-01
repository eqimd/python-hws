import numpy as np

class MyMatrix:
    def __init__(self, data):
        sz = len(data[0])
        for row in data:
            if len(row) != sz:
                raise ValueError("matrix invalid size")

        self.data = data
    
    def __add__(self, other):
        if len(self.data) != len(other.data):
            raise ValueError("matrix dimensions differ")
        
        res = []
        for i in range(len(self.data)):
            if len(self.data[i]) != len(other.data[i]):
                raise ValueError("matrix dimensions differ")
            
            tmp = []
            for j in range(len(self.data[i])):
                elem = self.data[i][j] + other.data[i][j]
                tmp.append(elem)

            res.append(tmp)
        
        return MyMatrix(res)
    
    def __mul__(self, other):
        if len(self.data) != len(other.data):
            raise ValueError("matrix dimensions differ")
        
        res = []
        for i in range(len(self.data)):
            if len(self.data[i]) != len(other.data[i]):
                raise ValueError("matrix dimensions differ")
            
            tmp = []
            for j in range(len(self.data[i])):
                elem = self.data[i][j] * other.data[i][j]
                tmp.append(elem)

            res.append(tmp)
        
        return MyMatrix(res)
    
    def __matmul__(self, other):
        sz1 = len(self.data)
        sz2 = len(other.data[0])

        res = [[0 for _ in range(sz1)] for _ in range(sz2)]

        for i in range(len(self.data)):
            if len(self.data[i]) != len(other.data):
                raise ValueError("matrix dimensions differ")
            
            for j in range(len(other.data[0])):
                for k in range(len(other.data)):
                    res[i][j] += self.data[i][k] * other.data[k][j]
        
        return MyMatrix(np.matmul(self.data, other.data))


def main():
    np.random.seed(0)
    matrix1 = MyMatrix(np.random.randint(0, 10, (10, 10)).tolist())
    matrix2 = MyMatrix(np.random.randint(0, 10, (10, 10)).tolist())

    matrix_sum = matrix1 + matrix2
    matrix_elements_mult = matrix1 * matrix2
    matrix_math_mult = matrix1 @ matrix2


    np.savetxt('matrix+.txt', matrix_sum.data, fmt='%i')
    np.savetxt('matrix*.txt', matrix_elements_mult.data, fmt='%i')
    np.savetxt('matrix@.txt', matrix_math_mult.data, fmt='%i')


if __name__ == '__main__':
    main()