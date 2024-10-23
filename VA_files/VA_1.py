"""
Solutions to module VA 1
Student: Ellen Lodin
Mail: ellen.lodin@telia.com
"""

from time import perf_counter as pc
import sys
sys.setrecursionlimit(10010)

def exchange(a, coins) -> list: 
    """ Count possible way to exchange a with the coins in coins. Use memorization"""
    memory = {}
    index = 0
    def _exchange(a, index):
        if a == 0:
            return 1
        if a < 0 or index >= len(coins):
            return 0
        
        key = (a,index)

        if key in memory:
            return memory[key]
        
        without_first_coin = _exchange(a, index + 1)
        with_first_coin = _exchange(a - coins[index], index)

        memory[key] = with_first_coin + without_first_coin

        return memory[key]
    
    return _exchange(a, index)

def zippa(l1: list, l2: list) -> list: 
    """ Returns a new list from the elements in l1 and l2 like the zip function"""
    lst1 = l1.copy()
    lst2 = l2.copy()
    if not lst1:
        return lst2
    elif not lst2:
        return lst1
    elif not lst1 and not lst2:
        return ""
    else:
        return [lst1[0] , lst2[0]] + zippa(lst1[1:], lst2[1:])
        
def main():
    print('\nCode that demonstates my implementations\n')
    coins = [1, 5, 10, 50, 100]

    start = pc()
    res1 = exchange(1000, coins)
    stop = pc()
    print(f'result = {res1}, time = {stop-start}')

    start = pc()
    res2 = exchange(2000, coins)
    stop = pc()
    print(f'result = {res2}, time = {stop-start}')

    start = pc()
    res2 = exchange(1000, coins)
    stop = pc()
    print(f'result = {res2}, time = {stop-start}')

    l1 = ['a', 'b', 'c']
    l2 = [2, 4, 6, 'x', 10]

    print(zippa(l1, l2))

if __name__ == "__main__":
    main()

####################################################

"""
  Answers to the none-coding tasks
  ================================
  
  
  Exercise 1

What time did it take to calculate large sums such as 1000 and 2000? 

What happens if you try to calculate e.g. 10000?
  
"""
