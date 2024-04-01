import numpy as np


HASHES = {}


# Хэш -- поэлементная сумма хэшей элементов
class MyHashMixin:
    def __hash__(self):
        hash_value = sum(hash(elem) for row in self.data for elem in row)

        return hash_value
    

class MyHashMatrix(MyHashMixin):
    def __init__(self, data):
        self.data = data
    
    def __add__(self, other):
        if self.data.shape != other.data.shape:
            raise ValueError("matrix dimensions differ")
        
        return MyHashMatrix(self.data + other.data)
    
    def __mul__(self, other):
        if self.data.shape != other.data.shape:
            raise ValueError("matrix dimensions differ")
        
        return MyHashMatrix(self.data * other.data)
    
    def __matmul__(self, other):
        if self.data.shape[1] != other.data.shape[0]:
            raise ValueError("matrix dimension differ")

        hashSelf = hash(self)
        hashOther = hash(other)

        dictSelf = HASHES.get(hashSelf)
        if dictSelf is not None:
            mult = dictSelf.get(hashOther)
            if mult is not None:
                return mult
        
        mult = MyHashMatrix(np.matmul(self.data, other.data))
        if dictSelf is not None:
            dictSelf[hashOther] = mult
        else:
            HASHES[hashSelf] = {hashOther: mult}
        return mult


def main():
    A = MyHashMatrix(np.array(
        [[1, 2, 3],
        [4, 5, 6]],
    ))
    np.savetxt('A.txt', A.data, fmt='%i')

    B = MyHashMatrix(np.array(
        [[1, 2],
        [3, 4],
        [5, 6]],
    ))
    np.savetxt('B.txt', B.data, fmt='%i')

    C = MyHashMatrix(np.array(
        [[1, 5, 3],
        [4, 2, 6]],
    ))
    np.savetxt('C.txt', C.data, fmt='%i')

    D = MyHashMatrix(np.array(
        [[1, 2],
        [3, 4],
        [5, 6]],
    ))
    np.savetxt('D.txt', D.data, fmt='%i')

    AB = A @ B
    CD = MyHashMatrix(np.matmul(C.data, B.data))

    np.savetxt('AB.txt', AB.data, fmt='%i')
    np.savetxt('CD.txt', CD.data, fmt='%i')

    print(hash(A), hash(C))
    print(hash(AB), hash(CD))


if __name__ == '__main__':
    main()
