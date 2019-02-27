try:
    from duble_linked_list import DubleLinkedList
except ModuleNotFoundError:
    raise Exception('You must download file: "duble_linked_list.py" in my git_hub or You will must implement duble linked list')

class TwoWayQueue:

    def __init__(self):
        self.duble_linked = DubleLinkedList()

    def first_enqueue(self, element):
        """Insert element on first position in queue
        T = O(1)
        """
        self.duble_linked.insert(element)
        return

    def last_enqueue(self, element):
        """Insert element on last position in queue
        T = O(1)
        """
        self.duble_linked.append(element)
        return

    def first_dequeue(self):
        """Delete first element in queue
        T = O(1)
        """
        self.duble_linked.delete_first()
        return

    def last_dequeue(self):
        """Delete last element in queue
        T = O(1)
        """
        self.duble_linked.delete_last()
        return

    def get_first(self):
        """Return first element in queue
        T = O(1)
        """
        return self.duble_linked.head

    def get_last(self):
        """Return last element in queue
        T = O(1)
        """
        return self.duble_linked.tail

    def get_size(self):
        """Return size queue.
        T = O(1)
        """
        return self.duble_linked.get_size()


    def __repr__(self):
        """Representation object."""
        help_list = []
        helpty = self.duble_linked.head
        while helpty:
            help_list.append(helpty)
            helpty = helpty.get_next()
        return f'{help_list}'


if __name__ == "__main__":
    test = TwoWayQueue()
    [test.first_enqueue(x) for x in range(1, 6)]
    while test.get_size() != 0:
        print(test.get_first())
        test.first_dequeue()
    [test.first_enqueue(x) for x in range(1, 6)]
    print(110 * '*')
    while test.get_size() != 0:
        print(test.get_last())
        test.last_dequeue()
    
    


    



