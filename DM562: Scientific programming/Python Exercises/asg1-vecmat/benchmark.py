import time
import vec
import mat
from vec_sparse import Vec as sparse_Vec
from mat_sparse import Mat as sparse_Mat

import numpy as np
import scipy as sp
import scipy.sparse as sps
import sys


class Timer(object):  # this is a special class: context manager
    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, ty, val, tb):
        end = time.time()
        self.elapsed = end - self.start
        return False


def our_timer(repeats, loops):
    #repeats = 5
    #loops = 1000
    def decorator(func):
        def wrapper(*args, **kwargs):
            times = [0]*repeats
            for i in range(repeats):
                with Timer() as t1:
                    for _ in range(loops):
                        func(*args, **kwargs)
                times[i] = t1.elapsed
                #print(func.__name__, times[i])
            print("best of", str(repeats), "times",str(loops),"executions for", func.__name__, str(min(times)))
        return wrapper
    return decorator


@our_timer(3, 1000)
def add_numpy(x, y):
    return x+y


@our_timer(3, 1000)
def add_vec(x, y):
    return x+y


@our_timer(3, 1000)
def mult_numpy(M, N):
    return M.dot(N)


@our_timer(3, 1000)
def mult_mat(M, N):
    return M*N


@our_timer(3, 1000)
def mult_sparse_mat(M, N):
    return M*N


def listlist2sparsemat(L):
    m, n = len(L), len(L[0])
    return sparse_Mat((set(range(m)), set(range(n))), {(r, c): L[r][c] for r in range(m) for c in range(n)})


def sps2sparseMat(M):
    S=M.tolil()
    elems = {(i,S.rows[i][j]): S.data[i][j] for i in range(len(S.data)) for j in range(len(S.data[i]))}
    return (sparse_Mat((set(range(S.shape[0])),set(range(S.shape[1]))), elems) )


if __name__ == '__main__':
    a = np.random.randint(10, 20, (1000))
    b = np.random.randint(10, 20, (1000))
    c = vec.Vec(a.tolist())
    d = vec.Vec(b.tolist())

    add_numpy(a, b)
    add_vec(c, d)

    M = np.random.randint(10, 20, (30, 10))
    N = np.random.randint(10, 20, (10, 30))
    u = np.random.randint(10, 20, (30))
    v = np.random.randint(10, 20, (10))

    mult_numpy(M, v)
    mult_mat(mat.Mat(M.tolist()), vec.Vec(v.tolist()))

    mult_numpy(u, M)
    mult_mat(vec.Vec(u.tolist()), mat.Mat(M.tolist()))

    mult_numpy(M, N)
    mult_mat(mat.Mat(M.tolist()), mat.Mat(N.tolist()))

    print("\n"+"="*20, "Sparse matrices", "="*20)
    M = sps.random(30, 20, density=0.01, format='csc')
    N = sps.random(20, 30, density=0.01, format='csc')
    M_s = sps2sparseMat(M)
    N_s = sps2sparseMat(N)
    M_m = mat.Mat(M.toarray().tolist())
    N_m = mat.Mat(N.toarray().tolist())

    print("Memory array:", M.toarray().nbytes, "bytes")
    print("Memory scipy sparse:", M.data.nbytes + M.indptr.nbytes + M.indices.nbytes, "bytes")
    print("Memory our Mat:", sys.getsizeof(M_m.store), "bytes")
    print("Memory our sparse Mat:", sys.getsizeof(M_s.D)+sys.getsizeof(M_s.f), "bytes")

    mult_numpy(M, N)
    mult_numpy(M.toarray(), N.toarray())
    mult_mat(M_m, N_m)
    mult_sparse_mat(M_s, N_s)
