"""
Solutions to module VA bst

Student: Ellen Lodin
Mail: ellen.lodin@telia.com
"""

import random
import math
import matplotlib.pyplot as plt

class BST:

    class Node:
        def __init__(self, key, left=None, right=None):
            self.key = key
            self.left = left
            self.right = right

        def __iter__(self):     # Discussed in the text on generators
            if self.left:
                yield from self.left
            yield self.key
            if self.right:
                yield from self.right

    def __init__(self, root=None):
        self.root = root

    def __iter__(self):         # Discussed in the text on generators
        if self.root:
            yield from self.root

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, r, key):
        if r is None:
            return self.Node(key)
        elif key < r.key:
            r.left = self._insert(r.left, key)
        elif key > r.key:
            r.right = self._insert(r.right, key)
        else:
            pass  # Already there
        return r

    def print(self):
        self._print(self.root)

    def _print(self, r):
        if r:
            self._print(r.left)
            print(r.key, end=' ')
            self._print(r.right)

    def contains(self, k):
        n = self.root
        while n and n.key != k:
            if k < n.key:
                n = n.left
            else:
                n = n.right
        return n is not None

    def size(self):
        return self._size(self.root)

    def _size(self, r):
        if r is None:
            return 0
        else:
            return 1 + self._size(r.left) + self._size(r.right)

    def ipl(self):    
        r = self.root
        lvl = 0
        return self._ipl(r, lvl)
    
    def _ipl(self, r, lvl):
            lvl += 1
            if r is None:
                return 0
            else:
                return lvl + self._ipl(r.left, lvl) + self._ipl(r.right, lvl)
            
    def height(self):                        
        def _height(r):
            if r is None:
                return 0
            else: 
                return 1 + max(_height(r.left), _height(r.right))  
        
        return _height(self.root)


def random_tree(n):    
    random_tree = BST()                           
    rad_list = [random.random() for i in range(n)]
    for x in rad_list:
        random_tree.insert(x)
    return random_tree


def main():
    t = BST()
    for x in [4, 1, 3, 6, 7, 1, 1, 5, 8]:
        t.insert(x)
    t.print()
    ipl = t.ipl()
    print(ipl)

    n = [1000*2**(i+1) for i in range(9)] 
    t = [random_tree(i) for i in n]
    ipl = [i.ipl() for i in t]
    ipl_per_n = [ipl[i]/n[i] for i in range(len(n))]
    theory = [1.39*math.log2(i) for i in n]
    #ipl_theory = [ipl_per_n[i]/theory[i]+1 for i in range(len(n))]

    hight = [i.height() for i in t]
    print(hight)

    plt.plot(n, theory, label='IPL per n (Theory)', color='blue', marker='o')     # n vs theory
    plt.plot(n, ipl_per_n, label='IPL per n', color='green', marker='s')  # n vs ipl_per_n
    plt.plot(n, hight, label='Height', color='red', marker='^')         # n vs hight
    plt.xlabel('n')
    plt.ylabel('Value')
    plt.title('n vs IPL in theory, calculated IPL and tree height')
    plt.legend()
    plt.show()

    
if __name__ == "__main__":
    main()


"""

Results for ipl of random trees
===============================
How well does that agree with the theory?
quite well, since the diffrence is constant about = 0.8 


What can you guess about the
height? To do

"""
