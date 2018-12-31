import numpy as np


def myfunc():
    a = np.array([[1, 2, 3],[4,5,6]])
    b = np.array([[1,4,5],[5,8,6]])
    c = np.array([[1,1],[1,1],[1,1]])
    print(a[0][2])
    print(a+b)
    d = np.eye(2,2,dtype=int)
    e = np.matmul(a, c, d)
    print(e)
    print(d)


if __name__=='__main__':
    myfunc()