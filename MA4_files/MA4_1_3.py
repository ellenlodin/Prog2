
"""
Solutions to module 4
Review date:
"""

student = "Ellen Lodin" 
reviewer = ""

import math as m
import random as r
from MA4_1_2 import sphere_volume
import concurrent.futures as future
from time import perf_counter as pc

def sphere_volume(n, d):
    def _generate_point(d):
        point = list(map(lambda _ : r.uniform(-1, 1), range(d)))
        sum_of_squares = sum([i**2 for i in point])
        return point, sum_of_squares

    points = [_generate_point(d) for _ in range(n)]
    nc = sum([1 for i, j in points if j <= 1])
    ratio = nc / n
    hypercub = 2**d
    volume = hypercub * ratio
    return volume

def hypersphere_exact(n,d):
    V = m.pi**(d/2)/(m.gamma(d/2+1))
    return V

#parallel code - parallelize for loop
def sphere_volume_parallel1(n,d,np):
    #using multiprocessor to perform 10 iterations of volume function 
    start = pc() 
    with future.ProcessPoolExecutor() as ex:
        results = ex.map(sphere_volume(n, d), range(np))
    end = pc()
    time = end-start
    return results, time

#Parallel code - parallelize actual computations by splitting data
def sphere_volume_parallel2(n,d,np):
    def _generate_point(d):
        point = list(map(lambda _ : r.uniform(-1, 1), range(d)))
        sum_of_squares = sum([i**2 for i in point])
        return sum_of_squares
    def _worker(d, nd):
        nc = sum([1 for _ in range(nd) if _generate_point(d) <= 1])

    start = pc()

    nd = n//np

    with future.ProcessPoolExecutor() as ex:
        results = list(ex.map(lambda _: _worker(nd, d), range(np)))

    nc = sum(results)
    ratio = nc / n
    hypercub = 2**d
    volume = hypercub * ratio

    end = pc()
    time = end - start
    return volume, time

def main():
    # part 1 -- parallelization of a for loop among 10 processes 
    n = 100000
    d = 11

    start = pc()
    for _ in range (10):
        sphere_volume(n,d)
    end = pc()
    print(end-start)

    n = 1000000
    d = 11
    results, time = sphere_volume_parallel1(n, d, 10)
    print(time)
 
    results, time = sphere_volume_parallel2(n, d, 10)
    print(time)
    
    

if __name__ == '__main__':
	main()
