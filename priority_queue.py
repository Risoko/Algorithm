try:
    from heap import Heap
except ModuleNotFoundError:
    raise Exception('You must download file: "heap.py" in my git_hub or You will must implement heap')

class ProrityQueue:

    def __init__(self):
        self.heap = Heap()
        self.help = 0

    def enqueue(self, element, priority=0, maximum=True):
        """Insert element to queue.
         If maximum = True builds queue based on maximum prioritet else maximu = False builds heap based on minimum prioritet"""
        self.heap.insert((priority, self.help, element), maximum)
        self.help += 1
        return

    def dequeue(self):
        """Delete element with queue"""
        return self.heap.extract()[2]

    def get_size(self):
        """Return size queue"""
        return self.heap.get_size()

    def __repr__(self):
        """Representation object."""
        lista = [x[2] for x in self.heap.table[1:]] 
        return f'{lista}'
    
if __name__ == "__main__":
    test = ProrityQueue()
    for element in range(1, 10000):
        test.enqueue(element, element**101)
    print(test)
    while test.get_size() != 0:
        print(test.dequeue())

    