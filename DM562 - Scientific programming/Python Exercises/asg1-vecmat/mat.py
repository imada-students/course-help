from vec import Vec


def getitem(M, k):
    """
    Returns the value of entry k in M, where k is a 2-tuple of indices
    >>> M = Mat([[1,2,3],[1,2,3]])
    >>> M[0,0]
    1
    >>> M[1,2]
    3
    """
    assert k[0] in range(M.size[0]) and k[1] in range(M.size[1])
    return M.store[k[0]][k[1]]


def equal(A, B):
    """
    Returns true iff A is equal to B.

    >>> A = Mat([[1,2,3],[1,2,3]])
    >>> B = Mat([[1,2,3],[1,2,3]])
    >>> C = Mat([[1,2,3],[1,2,0]])
    >>> A == B
    True
    >>> B == A
    True
    >>> A == C
    False
    >>> C == A
    False
    >>> A == Mat([[1,2,3],[1,2,3]])
    True
    """
    assert A.size == B.size
    for rows, (Arow, Brow) in enumerate(zip(A.store, B.store)):
        for columns, (Acol, Bcol) in enumerate(zip(Arow, Brow)):
            if Acol != Bcol:
                return False
    return True


def setitem(M, k, val):
    """
    Set entry k of Mat M to val, where k is a 2-tuple.
    >>> M = Mat([[1,2,3],[1,2,3]])
    >>> M[0, 1] = 0
    >>> M[1,2] = 0
    >>> M == Mat([[1,0,3],[1,2,0]])
    True
    """
    assert k[0] in range(M.size[0]) and k[1] in range(M.size[1])
    M.store[k[0]][k[1]] = val


def add(A, B):
    """
    Return the sum of Mats A and B.

    >>> A1 = Mat([[1,2,3],[1,2,3]])
    >>> A2 = Mat([[1,1,1],[1,1,1]])
    >>> B = Mat([[2,3,4],[2,3,4]])
    >>> A1 + A2 == B
    True
    >>> A2 + A1 == B
    True
    >>> A1 == Mat([[1,2,3],[1,2,3]])
    True
    >>> zero = Mat([[0,0,0],[0,0,0]])
    >>> B + zero == B
    True
    """
    assert A.size == B.size
    return Mat([[Acol + Bcol for index, (Acol, Bcol) in enumerate(zip(Arow, Brow))] for index, (Arow, Brow) in enumerate(zip(A.store, B.store))])


def scalar_mul(M, x):
    """
    Returns the result of scaling M by x.

    >>> M = Mat([[1,1,1],[2,2,2]])
    >>> 0*M == Mat([[0,0,0],[0,0,0]])
    True
    >>> 1*M == M
    True
    >>> 0.25*M == Mat([[0.25,0.25,0.25],[0.5,0.5,0.5]])
    True
    """
    return Mat([[column * x for column in row] for row in M.store])


def transpose(M):
    """
    Returns the matrix that is the transpose of M.

    >>> M = Mat([[1,2,3],[1,2,3]])
    >>> M.transpose() == Mat([[1,1],[2,2],[3,3]])
    True
    """
    dim = M.size
    output = Mat([[0 for i in range(0, dim[0])] for q in range(0,dim[1])])  #Creates a 0 matrix with inverted dimentions of input
    for row in range(0, dim[0]):
        for col in range(0, dim[1]):
            output[col, row] = M[row, col]          #Copy each element over in the new matrix, but swap row and column indexes
    return output
    


def vector_matrix_mul(v, M):
    """
    returns the product of vector v and matrix M

    >>> v1 = Vec([2,2])
    >>> M1 = Mat([[1,2,3],[1,2,3]])
    >>> v1*M1 == Vec([4,8,12])
    True
    >>> v1 == Vec([2,2])
    True
    >>> M1 == Mat([[1,2,3],[1,2,3]])
    True
    """
    assert M.size[0] == v.size
    store = [0] * M.size[1]
    for height in range(0, M.size[1]):
        for width in range(0,M.size[0]):
            store[height] = store[height] + v[width] * M[width, height]
    return Vec(store)

def matrix_vector_mul(M, v):
    """
    Returns the product of matrix M and vector v.

    >>> N1 = Mat([[-1,-2,-3],[1,2,3]])
    >>> u1 = Vec([3,2,1])
    >>> N1*u1 == Vec([-10,10])
    True
    >>> N1 == Mat([[-1,-2,-3],[1,2,3]])
    True
    >>> u1 == Vec([3,2,1])
    True
    """
    assert M.size[1] == v.size
    store = [0] * M.size[0]
    for height in range(0, M.size[0]):
        for width in range(0,M.size[1]):
            store[height] = store[height] + v[width] * M[height, width]
            #print(store)
    return Vec(store)


def matrix_matrix_mul(A, B):
    """
    Returns the result of the matrix-matrix multiplication, A*B.

    >>> A = Mat([[0,3,2],[5,4,1]])
    >>> B = Mat([[1,4],[5,2],[0,3]])
    >>> A*B == Mat([[15,12],[25,31]])
    True
    >>> C = Mat([[4,-3],[1,0],[1,-2]])
    >>> D = Mat([[3,-2],[4,-1]])
    >>> C*D == Mat([[0,-5],[3,-2],[-5,0]])
    True
    >>> E = Mat([[1,2],[3,4]])
    >>> F = Mat([[0,5],[0,0]])
    >>> E*F == Mat([[0,5],[0,15]])
    True
    >>> F.transpose()*E.transpose() == Mat([[0,0],[5,15]])
    True
    """
    assert A.size[1] == B.size[0]
    store = [[0]*B.size[1] for i in range(0, A.size[0])]
    for width in range(0, A.size[0]):
        for height in range(0, B.size[1]):
            sum = 0
            for index in range(0, A.size[1]):
                sum = sum + A[width, index] * B[index, height]
            store[width][height] = sum
    return Mat(store)

################################################################################


class Mat:
    def __init__(self, store):
        assert isinstance(store, list)
        assert isinstance(store[0], list)
        s = len(store[0])
        assert s != 0
        for i in range(1, len(store)):
            assert s == len(store[i])
        self.size = (len(store), s)
        self.store = store

    __getitem__ = getitem
    __setitem__ = setitem
    transpose = transpose

    def __neg__(self):
        return (-1)*self

    def __mul__(self, other):
        if Mat == type(other):
            return matrix_matrix_mul(self, other)
        elif Vec == type(other):
            return matrix_vector_mul(self, other)
        else:
            return scalar_mul(self, other)
            # this will only be used if other is scalar (or not-supported). mat and vec both have __mul__ implemented

    def __rmul__(self, other):
        if Vec == type(other):
            return vector_matrix_mul(other, self)
        else:  # Assume scalar
            return scalar_mul(self, other)

    __add__ = add

    def __radd__(self, other):
        "Hack to allow sum(...) to work with matrices"
        if other == 0:
            return self

    def __sub__(a, b):
        return a+(-b)

    __eq__ = equal

    def copy(self):
        return Mat([self.store[i].copy() for i in range(self.size[0])])

    def __str__(M, rows=None, cols=None):
        "string representation for print()"
        if rows == None:
            rows = range(M.size[0])
        if cols == None:
            cols = range(M.size[1])
        separator = ' | '
        numdec = 3
        pre = 1+max([len(str(r)) for r in rows])
        colw = {col: (1+max([len(str(col))] + [len('{0:.{1}G}'.format(M[row, col], numdec)) if isinstance(
            M[row, col], int) or isinstance(M[row, col], float) else len(str(M[row, col])) for row in rows])) for col in cols}
        s1 = ' '*(1 + pre + len(separator))
        s2 = ''.join(['{0:>{1}}'.format(str(c), colw[c]) for c in cols])
        s3 = ' '*(pre+len(separator)) + '-'*(sum(list(colw.values())) + 1)
        s4 = ''.join(['{0:>{1}} {2}'.format(str(r), pre, separator)+''.join(['{0:>{1}.{2}G}'.format(M[r, c], colw[c], numdec) if isinstance(
            M[r, c], int) or isinstance(M[r, c], float) else '{0:>{1}}'.format(M[r, c], colw[c]) for c in cols])+'\n' for r in rows])
        return '\n' + s1 + s2 + '\n' + s3 + '\n' + s4

    def pp(self, rows, cols):
        print(self.__str__(rows, cols))

    def __repr__(self):
        "evaluatable representation"
        return "Mat(" + str(self.store) + ", " + str(self.size) + ")"

    def __iter__(self):
        raise TypeError('%r object is not iterable' % self.__class__.__name__)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
