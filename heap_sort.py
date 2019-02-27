from random import randint
try:
    from heap import Heap
except ModuleNotFoundError:
    raise Exception('You must download file: "heap.py" in my git_hub or You will must implement heap')

def heap_sort(L, reverse=False):
    """Heap Sort algorithm
    Tmin = theta(nlgn)
    Tave = theta(nlgn)
    Tmax = theta(nlgn)
    In place = No
    """
    if reverse:
        maximum = True
    else:
        maximum = False
    my_heap = Heap()
    my_heap.build_heap(L, maximum)
    return [my_heap.extract() for _ in range(len(L))]

if __name__ == "__main__":
    L = [randint(-100, 100) for _ in range(1, 51)]
    print(L)
    print(120 * '*')
    print(heap_sort(L))
    print(120 * '*')
    print(heap_sort(L, reverse=True))
    i = 0
    while i != 10000:
        L = [randint(-100, 100) for _ in range(1, 51)]
        assert sorted(L) == heap_sort(L)
        i += 1

