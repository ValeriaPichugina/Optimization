import random
import timeit

def inversions(A):
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

B = list(range(1, 2001))
random.shuffle(B)

if __name__=='__main__':
    from timeit import Timer
    t = Timer(lambda: inversions(B))
    print(t.timeit(number=1))