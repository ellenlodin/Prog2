"""
Solutions to module VA 4

Student: Ellen Lodin
Mail: ellen.lodin@telia.com
"""

from time import perf_counter as pc
import matplotlib.pyplot as plt
from numba import njit
import numpy as np

def fib_mem(x):
    memory = {0: 0, 1: 1}  

    def _fib(x):
        if x in memory:  
            return memory[x]

        memory[x] = _fib(x - 1) + _fib(x - 2)
        return memory[x]
    
    return _fib(x)

def fib_py(n):
    if n <= 1:
        return n
    else:
        return (fib_py(n-1) + fib_py(n-2))

@njit #compiling it to make it faster
def fib_numba(n):
	if n <= 1:
		return n
	else:
		return(fib_numba(n-1) + fib_numba(n-2))

n1 = np.arange(20,45)

t_py = []
t_mem = []
t_numba = []

"""
for i in n1: 
	start1 = pc()
	fib_py(i)
	stop1 = pc()
	t_py.append(stop1-start1)
"""
	
for i in n1: 
	start2 = pc()
	fib_numba(i)
	stop2 = pc()
	t_numba.append(stop2-start2)
      
for i in n1: 
	start3 = pc()
	fib_mem(i)
	stop3 = pc()
	t_mem.append(stop3-start3)
	
#plt.plot(n1, t_py, label='Python processing time', color='blue', marker='o') 
plt.plot(n1, t_mem, label='Python-memorization processing time', color='red', marker='o')    
plt.plot(n1, t_numba, label='Python-Numba processing time', color='green', marker='s')  
plt.xlabel('n')
plt.ylabel('t (s)')
plt.title('Fibonacci Execution Time: Python vs Numba')
plt.legend()
plt.savefig('Fibonacci Execution Time - Python vs Numba.png')
plt.show()

#fib_res_py = fib_py(47)
fib_res_numba = fib_numba(47)

#print(f'Python: fib(47)= {fib_res_py}')
print(f'Numba: fib(47)= {fib_res_numba}')
#fib(47)= 2971215073