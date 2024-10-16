
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
        results = ex.map(sphere_volume, [n]*np, [d]*np)
    end = pc()
    time = end-start
    print(f'Processing time of 10 processes parallelized: t = {time}s')
    med_result = sum(results)/np
    return med_result

#Parallel code - parallelize actual computations by splitting data

def _generate_point(d): 
    point = list(map(lambda _ : r.uniform(-1, 1), range(d)))
    sum_of_squares = sum(i**2 for i in point)
    return sum_of_squares <= 1 #returns True/False

def _worker(d, nd):
    sum_of_points = sum([_generate_point(d) for _ in range(nd)])
    return sum_of_points

def sphere_volume_parallel2(n,d,np):

    start = pc()
    nd = n//np

    with future.ProcessPoolExecutor() as ex:
         results = ex.map(_worker, [d] * np, [nd] * np)

    nc = sum(results)
    ratio = nc / n
    hypercub = 2**d
    volume = hypercub * ratio

    end = pc()

    time = end - start
    print(f'Processing time of one process with parallelization: t = {time}s')
    return volume

def main():

    print(f'Exact volyme of the hypersphere: V={hypersphere_exact(1,11)}m3')

    #part 1 -- parallelization of a for loop among 10 processes 
    print('PART 1')
    
    start = pc()
    for _ in range (10):
        sphere_volume(100000, 11)
    end = pc()
    time1 = end-start
    print(f'Processing time of 10 processes in a for loop: t = {time1}s')

    volyme1 = sphere_volume_parallel1(100000, 11, 10)
    print(f'Average volume from 10 processes parallelized: V = {volyme1}m3')

    #part 2 -- parallelization of a for loop among 10 processes 
    print('PART 2')

    start = pc()
    sphere_volume(1000000, 11)
    end = pc()
    time2 = end-start
    print(f'Processing time of one process without parallelization: t = {time2}s')

    volyme2 = sphere_volume_parallel2(1000000, 11, 10)
    print(f'Volume from one process with parallelization: V = {volyme2}m3')
    

if __name__ == '__main__':
	main()
