
def getitem(v, k):
    """
    Return the value of entry k in vector v.
    Entries start from zero

    >>> v = Vec([1,2,3,4])
    >>> v[2]
    3
    >>> v[0]
    1
    """
    assert k in range(v.size)
    return v.store[k]


def setitem(v, k, val):
    """
    Set the element of v with index k to be val.
    The function should only set the value of elements already in the vector.
    It cannot extend the vector.

    >>> v = Vec([1,2,3])
    >>> v[2] = 4
    >>> v[2]
    4
    >>> v[0] = 3
    >>> v[0]
    3
    >>> v[1] = 0
    >>> v[1]
    0
    """
    assert k in range(v.size)
    v.store[k] = val


def equal(u, v):
    """
    Return true iff u is equal to v.

    >>> Vec([1,2,3]) == Vec([1,2,3])
    True
    >>> Vec([0,0,0]) == Vec([0,0,0])
    True

    """
    assert v.size == u.size
    return u.store == v.store


def add(u, v):
    """
    Returns the sum of the two vectors.

    >>> a = Vec([1, 2, 3])
    >>> b = Vec([1, 1, 1])
    >>> c = Vec([2, 3, 4])
    >>> a + b == c
    True
    >>> a == Vec([1, 2, 3])
    True
    >>> b == Vec([1, 1, 1])
    True
    """
    assert u.size == v.size
    return Vec([compv + compu for index, (compv, compu) in enumerate(zip(u.store,v.store))])

def dot(u, v):
    """
    Returns the dot product of the two vectors.

    >>> u1 = Vec([1, 2])
    >>> u2 = Vec([1, 2])
    >>> u1*u2
    5
    >>> u1 == Vec([1, 2])
    True
    >>> u2 == Vec([1, 2])
    True

    """
    assert u.size == v.size
    sum = 0
    for index, (compv, compu) in enumerate(zip(u.store,v.store)):
        sum = sum + compv * compu
    return sum


def scalar_mul(v, alpha):
    """
    Returns the scalar-vector product alpha times v.

    >>> zero = Vec([0, 0, 0, 0])
    >>> u = Vec([1, 2, 3, 4])
    >>> 0*u == zero
    True
    >>> 1*u == u
    True
    >>> 0.5*u == Vec([0.5, 1, 1.5, 2])
    True
    >>> u == Vec([1, 2, 3, 4])
    True
    """
    return Vec([comp * alpha for comp in v.store])


def neg(v):
    """
    Returns the negation of a vector.

    >>> u = Vec([1, 2, 3, 4])
    >>> -u
    Vec([-1, -2, -3, -4], 4)
    >>> u == Vec([1, 2, 3, 4])
    True
    >>> -Vec([1, 2]) == Vec([-1, -2])
    True
    """
    return Vec([-comp for comp in v.store])

###############################################################################################################################


class Vec:
    """
    A vector has two attributes:
    store - the list containing the data
    size - the size of the vector
    """

    def __init__(self, data):
        assert isinstance(data, list)
        self.store = data
        self.size = len(self.store)

    __getitem__ = getitem
    __setitem__ = setitem
    __neg__ = neg
    __rmul__ = scalar_mul  # if left arg of * is primitive, assume it's a scalar

    def __mul__(self, other):
        # If other is a vector, returns the dot product of self and other
        if isinstance(other, Vec):
            return dot(self, other)
        else:
            return NotImplemented  # Will cause other.__rmul__(self) to be invoked

    def __truediv__(self, other):  # Scalar division
        return (1/other)*self

    __add__ = add

    def __radd__(self, other):
        "Hack to allow sum(...) to work with vectors"
        if other == 0:
            return self

    def __sub__(a, b):
        "Returns a vector which is the difference of a and b."
        return a+(-b)

    __eq__ = equal

    def __str__(v):
        "pretty-printing. Used when print is called"
        D_list = range(v.size)
        numdec = 3
        wd = dict([(k, (1+max(len(str(k)), len('{0:.{1}G}'.format(v[k], numdec))))) if isinstance(
            v[k], int) or isinstance(v[k], float) else (k, (1+max(len(str(k)), len(str(v[k]))))) for k in D_list])
        s1 = ''.join(['{0:>{1}}'.format(str(k), wd[k]) for k in D_list])
        s2 = ''.join(['{0:>{1}.{2}G}'.format(v[k], wd[k], numdec) if isinstance(
            v[k], int) or isinstance(v[k], float) else '{0:>{1}}'.format(v[k], wd[k]) for k in D_list])
        return "\n" + s1 + "\n" + '-'*sum(wd.values()) + "\n" + s2

    def __repr__(self):
        "used when just typing >>> v"
        return "Vec(" + str(self.store) + ", " + str(self.size) + ")"

    def copy(self):
        "Don't make a new copy of the domain D"
        return Vec(self.store.copy())

    def __iter__(self):
        raise TypeError('%r object is not iterable' % self.__class__.__name__)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
