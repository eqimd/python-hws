import numpy as np


class MyStrMixin:
    def __str__(self):
        s = ''
        for x in self.data:
            for y in x:
                s += str(y) + ' '
            s += '\n'
        return s
    

class MySaveMixin:
    def save(self, fn):
        np.savetxt(fn, self.data, fmt='%i')


class MyMixinMatrix(np.lib.mixins.NDArrayOperatorsMixin, MyStrMixin, MySaveMixin):
    _HANDLED_TYPES = (np.ndarray,)

    def __init__(self, data: np.ndarray):
        self.data = data

    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        out = kwargs.get('out', ())
        for x in inputs + out:
            # Only support operations with instances of _HANDLED_TYPES.
            # Use ArrayLike instead of type(self) for isinstance to
            # allow subclasses that don't override __array_ufunc__ to
            # handle ArrayLike objects.
            if not isinstance(x, self._HANDLED_TYPES + (MyMixinMatrix,)):
                return NotImplemented

        # Defer to the implementation of the ufunc on unwrapped values.
        inputs = tuple(x.data if isinstance(x, MyMixinMatrix) else x
                       for x in inputs)
        if out:
            kwargs['out'] = tuple(
                x.data if isinstance(x, MyMixinMatrix) else x
                for x in out)
        result = getattr(ufunc, method)(*inputs, **kwargs)

        if type(result) is tuple:
            # multiple return values
            return tuple(type(self)(x) for x in result)
        elif method == 'at':
            # no return value
            return None
        else:
            # one return value
            return type(self)(result)

    @property
    def data(self):
        return self._data
    
    @data.setter
    def data(self, new_data):
        self._data = np.array(new_data)


def main():
    np.random.seed(0)
    matrix1 = MyMixinMatrix(np.random.randint(0, 10, (10, 10)))
    matrix2 = MyMixinMatrix(np.random.randint(0, 10, (10, 10)))

    matrix_sum = matrix1 + matrix2
    matrix_elements_mult = matrix1 * matrix2
    matrix_math_mult = matrix1 @ matrix2

    matrix_sum.save('matrix+.txt')
    matrix_elements_mult.save('matrix*.txt')
    matrix_math_mult.save('matrix@.txt')


if __name__ == '__main__':
    main()