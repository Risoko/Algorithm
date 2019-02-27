from random import randint
try:
    from priority_queue import ProrityQueue
except ModuleNotFoundError:
    raise Exception('You must download file: "priority_queue.py" in my git_hub or You will must implement heap')

def sort_priority_queue(L, reverse=False):
    """Sort use priority queue"""
    if reverse:
        maximum = True
    else:
        maximum = False
    queue = ProrityQueue()
    [queue.enqueue(element=elem, priority=elem, maximum=maximum) for elem in L]
    return [queue.dequeue() for _ in range(len(L))]

if __name__ == "__main__":
    i = 0
    while i != 100:
        L = [randint(-20, 100) for _ in range(100)]
        i += 1
        assert sorted(L) == sort_priority_queue(L)


    