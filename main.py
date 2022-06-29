import numba as nb
from numba import njit
from numba import int64
import random
from timeit import Timer


def stupid_inversions(A):
    print(len([1 for i in range(len(A)) for j in range(i + 1, len(A)) if A[i] > A[j]]))


@njit
def stupid_inversions_numba(A):
    print(len([1 for i in range(len(A)) for j in range(i + 1, len(A)) if A[i] > A[j]]))


def unnamed_inversions(A):
    l = len(A)
    B = list(range(1, l+1))
    res = 0
    for i in range(l):
        pos = 0
        while A[i] != B[pos]:
            pos += 1
        res += pos
        B = B[:pos] + B[(pos+1):]
    print(res)

@njit
def unnamed_inversions_numba(A):
    l = len(A)
    B = list(range(1, l+1))
    res = 0
    for i in range(l):
        pos = 0
        while A[i] != B[pos]:
            pos += 1
        res += pos
        B = B[:pos] + B[(pos+1):]
    print(res)


def get_inv_count(arr):
    inv_count = 0
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                inv_count += 1

    print(inv_count)


def fenwick_inversions(A):
    res = 0
    lenght = len(A)
    counts = [0] * lenght
    AReversed = A[::-1]
    for x in AReversed:
        v = x - 1
        while v != 0:
            res += counts[v-1]
            v -= v & -v
        v = x
        while v <= lenght:
            counts[v-1] += 1
            v += v & -v
    print(res)


@njit(locals={'res': int64})
def fenwick_inversions_numba(A):
    res = 0
    lenght = len(A)
    counts = [0] * lenght
    AReversed = A[::-1]
    for x in AReversed:
        v = x - 1
        while v != 0:
            res += counts[v - 1]
            v -= v & -v
        v = x
        while v <= lenght:
            counts[v - 1] += 1
            v += v & -v
    print(res)


def generate_data(leng):
    B = list(range(1, leng+1))
    random.shuffle(B)
    return [B, nb.typed.List(B)]


if __name__ == '__main__':

    data_len = 10000
    [B, B_n] = generate_data(data_len)
    t = Timer(lambda: stupid_inversions(B))
    t1 = t.timeit(number=1)
    print("Инверсии наивным алгоритмом. Массив длиной ", data_len, " значений. Без оптимизации: ", t1)
    t = Timer(lambda: stupid_inversions_numba(B_n))
    t2 = t.timeit(number=1)
    print("Инверсии наивным алгоритмом. Массив длиной ", data_len, " значений. С оптимизацией: ", t2)
    print("Ускорение в ", t1/t2, " раз.")

    data_len = 20000
    [B, B_n] = generate_data(data_len)
    t = Timer(lambda: unnamed_inversions(B))
    t1 = t.timeit(number=1)
    print("Инверсии наивным алгоритмом. Массив длиной ", data_len, " значений Без оптимизации: ", t1)
    t = Timer(lambda: unnamed_inversions_numba(B_n))
    t2 = t.timeit(number=1)
    print("Инверсии наивным алгоритмом. Массив длиной ", data_len, " значений. С оптимизацией: ", t2)
    print("Ускорение в ", t1 / t2, " раз.")

    data_len = 1200000
    [B, B_n] = generate_data(data_len)
    t = Timer(lambda: fenwick_inversions(B))
    t1 = t.timeit(number=1)
    print("Инверсии деревом Фенвика. Массив длиной ", data_len, " значений. Без оптимизации: ", t1)
    t = Timer(lambda: fenwick_inversions_numba(B_n))
    t2 = t.timeit(number=1)
    print("Инверсии деревом Фенвика. Массив длиной ", data_len, " значений. С оптимизацией: ", t2)
    print("Ускорение в ", t1/t2, " раз.")
