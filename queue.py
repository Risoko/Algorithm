try:
    from linked_list import LinkedList
except ModuleNotFoundError:
    raise Exception('You must download file: "linked_list.py" in my git_hub or You will must implement linked list')

class Queue:

    def __init__(self):
        self.linked = LinkedList()

    def enqueue(self, element):
        """Insert element in queue
        T = O(1)
        """
        self.linked.append(element)
        return

    def dequeue(self):
        """Delete element in queue
        T = O(1)
        """
        self.linked.delete_first()
        return

    def get_first(self):
        """Return first element in queue
        T = O(1)
        """
        return self.linked.get_head()

    def get_size(self):
        """Return size queue.
        T = O(1)
        """
        return self.linked.get_size()

    def __repr__(self):
        """Representation object."""
        help_list = []
        helpty = self.linked.get_head()
        while helpty:
            help_list.append(helpty)
            helpty = helpty.get_next()
        return f'{help_list}'

if __name__ == "__main__":
    test = Queue()
    [test.enqueue(x) for x in range(1, 101)]
    print(test)
    print(test.get_size())
    test.dequeue()
    print(test)
    print(test.get_first())
    print(test.get_size())
    while test.get_size() != 0:
        print(test.get_first())
        test.dequeue()
    print(test)







