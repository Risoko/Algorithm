from math import floor
from random import randint

class Heap:

    def __init__(self):
        self.table = [None]
        self.size = 0

    def build_heap(self, T, maximum=True):
        """Method build heap with list. If heap is not null clear heap. 
        If maximum = True builds heap based on maximum else maximu = False builds heap based on minimum
        T = theta(lgn). 
        """
        if len(self.table) > 1:
            self.table = [None]
        n = len(T) 
        parent = floor(n / 2)
        self.table += T
        for k in range(parent, 0, -1):
            self._fix_down(self.table, k, n, maximum)
        self.size = n
        return
    
    def insert(self, element, maximum=True):
        """Method append to the heap 
        If maximum = True builds heap based on maximum else maximu = False builds heap based on minimum
        T = theta(nlgn)
        """
        self.table.append(element)
        self.size += 1
        self._fix_up(self.table, maximum)
        return
    
    def extract(self):
        """Delete max or minimum element with heap"""
        if self.get_size() == 0:
            raise Exception('Heap is empty')
        if self.table[1] > self.table[-1]:
            maximum = True
        else:
            maximum = False
        self.size -= 1
        _max = self.table[1]
        self.table[1], self.table[-1] = self.table[-1], self.table[1]
        n = self.get_size()
        self.table = self.table[:-1]
        self._fix_down(self.table, 1, n, maximum)
        return _max

    def get_size(self):
        """Return size heap"""
        return self.size

    def _fix_down(self, h, k, n, maximum):
        """Fix heap from the bottom"""
        l = 2 * k
        r = (2 * k) + 1
        largest = k
        if l <= n and self._help_fun(h, l, k, maximum):
            largest = l
        if r <= n and self._help_fun2(h, r, largest, maximum):
            largest = r
        if largest != k:
            h[k], h[largest] = h[largest], h[k]
            self._fix_down(h, largest, n, maximum)

    def _fix_up(self, heap, maximum):
        """Fix heap from the top"""
        len_heap = len(heap) - 1
        while len_heap > 1 and self._help_fun3(heap, floor(len_heap / 2), len_heap, maximum):            
            heap[len_heap], heap[floor(len_heap / 2)] = heap[floor(len_heap / 2)], heap[len_heap]
            len_heap = floor(len_heap / 2)

    def _help_fun(self, h, l, k, maximum):
        if maximum:
            return h[l] > h[k]
        return h[l] < h[k]

    def _help_fun2(self, h, r, largest, maximum):
        if maximum:
            return h[r] > h[largest]
        return h[r] < h[largest]

    def _help_fun3(self, h, l1, l2, maximum):
        if maximum:
            return h[l1] < h[l2]
        return h[l1] > h[l2]
        
    def __repr__(self):
        return f'{self.table[1:]}'

if __name__ == "__main__":
    test = Heap()
    l = [randint(-20, 20) for _ in range(1, 26)]
    print(l)
    test.build_heap(l, maximum=False)
    print(test.get_size())
    print(test)
    test.insert(900000000, maximum=False)
    print(test)
    for element in range(1, 3):
        test.insert(element, maximum=False)
    test.insert(-900000000000000, maximum=False)
    print(test)
    while test.get_size() != 0:
        print(test.extract())
    
        