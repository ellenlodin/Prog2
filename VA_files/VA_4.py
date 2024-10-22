"""
Solutions to module VA 4

Student:
Mail:
"""
#!/usr/bin/env python3

from person import Person
"""
Write a script that gives a plot for comparison of two approaches for Fibonacci numbers
"""
#Python
def fib_py(n):
	if n <= 1:
		return n
	else:
		return(fib_py(n-1) + fib_py(n-2))

@njit
def fib_numba(n):
	if n <= 1:
		return n
	else:
		return(fib_py(n-1) + fib_py(n-2))

def main():
	f = Person(50)
	print(f.getAge())
	print(f.getDecades())

	f.setAge(51)
	print(f.getAge())
	print(f.getDecades())

	print(fib_py(47))
	print(fib_numba(47))

if __name__ == '__main__':
	main()

"""What is the result for Fibonacci with n=47? Why?"""