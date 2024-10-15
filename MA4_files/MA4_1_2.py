
"""
Solutions to module 4
Review date:
"""

student = "Ellen Lodin"
reviewer = ""

import math as m
import random as r

def sphere_volume(n, d):
    # n is a list of set of coordinates
    # d is the number of dimensions of the sphere 
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

def hypersphere_exact(n, d):
    V = m.pi**(d/2)/(m.gamma(d/2+1))
    return V
     
def main():
    n1 = 100000
    d1 = 2
    print(sphere_volume(n1, d1))
    print(hypersphere_exact(d1))
    n2 = 100000
    d2 = 11
    print(sphere_volume(n2, d2))
    print(hypersphere_exact(d2))


if __name__ == '__main__':
	main()
