
"""
Solutions to module 4
Review date:
"""

student = "Ellen Lodin"
reviewer = ""


import random as r
import matplotlib.pyplot as plt 
import math

def approximate_pi(n):

    def _get_random():
        x = r.uniform(-1, 1)
        y = r.uniform(-1, 1)
        return x, y

    nc = 0
    lc_x = []
    lc_y = []
    ls_x = []
    ls_y = []

    for i in range(n):
        point = _get_random()
        ma = math.sqrt(point[0]**2 + point[1]**2)
        if ma <= 1:
            nc += 1
            lc_x.append(point[0])
            lc_y.append(point[1])
        else:
            ls_x.append(point[0])
            ls_y.append(point[1])

    print(f'Number of points inside the circle: nc={nc}!')

    pi = 4 * nc / n

    print(f'Approximate pi: pi_approx={pi}!')
    print(f'True value of pi: pi={math.pi}!')

    plt.scatter(lc_x, lc_y, color = "Red")
    plt.scatter(ls_x, ls_y, color = "Blue")

    plt.title('Simple Line Plot')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.savefig(f'scatter plot: n = {n}')

    plt.show()

    return pi
    
def main():
    dots = [1000, 10000, 100000]
    for n in dots:
        approximate_pi(n)

if __name__ == '__main__':
	main()
