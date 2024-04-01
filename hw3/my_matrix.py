import numpy as np

class MyMatrix:
    def __init__(self, data: np.ndarray):
        self.data = data
    
    def __add__(self, other: np.ndarray):
        if self.data.shape != other.data.shape:
            raise ValueError("matrix dimensions differ")
        
        return MyMatrix(self.data + other.data)
    
    def __mul__(self, other: np.ndarray):
        if self.data.shape != other.data.shape:
            raise ValueError("matrix dimensions differ")
        
        return MyMatrix(self.data * other.data)
    
    def __matmul__(self, other: np.ndarray):
        if self.data.shape[1] != other.data.shape[0]:
            raise ValueError("matrix dimension differ")
        
        return MyMatrix(np.matmul(self.data, other.data))


def main():
    np.random.seed(0)
    matrix1 = MyMatrix(np.random.randint(0, 10, (10, 10)))
    matrix2 = MyMatrix(np.random.randint(0, 10, (10, 10)))

    matrix_sum = matrix1 + matrix2
    matrix_elements_mult = matrix1 * matrix2
    matrix_math_mult = matrix1 @ matrix2


    np.savetxt('matrix+.txt', matrix_sum.data, fmt='%i')
    np.savetxt('matrix*.txt', matrix_elements_mult.data, fmt='%i')
    np.savetxt('matrix@.txt', matrix_math_mult.data, fmt='%i')


if __name__ == '__main__':
    main()