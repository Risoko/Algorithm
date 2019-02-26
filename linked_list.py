from random import randint

class _Node:
    
    def __init__(self, next_element=None, data=None):
        self.next = next_element
        self.data = data

    def get_next(self):
        """Return next element
        T = O(1)
        """
        return self.next

    def set_next_element(self, next_element):
        """Set next element
        T = O(1)
        """
        self.next = next_element

    def get_data(self):
        """Return data
        T = O(1)
        """
        return self.data

    def set_data(self, data):
        """Set data
        T = O(1)
        """
        self.data = data

    def __repr__(self):
        return f'{self.data}'

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get_size(self):
        """Return size linked list:
        T = O(1)
        """
        return self.size

    def insert(self, item):
        """Insert element for first position 
        T = O(1)
        """
        element = _Node(data=item)
        if self.head is None:
            self.tail = element
        element.set_next_element(self.head)
        self.head = element
        self.size += 1
        return

    def append(self, item):
        """Append element for last position 
        T = O(1)
        """
        element = _Node(data=item)
        if self.head is None:
            self.head = element
            self.tail = element
            self.size += 1
            return
        self.tail.set_next_element(element)
        self.tail = element
        self.size += 1
        return

    def search(self, element):
        """Search element in list:
        T = O(n)
        """
        helpty = self.head
        while helpty:
            if helpty.get_data() == element:
                return True
            helpty = helpty.get_next()
        return False

    def delete_first(self):
        """Delete first element
        T = O(1)
        """
        if self.get_size() == 0:
            raise Exception('Linked List is empty.')
        elif self.get_size() == 1:
            self.head = None
            self.tail = None
            self.size -= 1
            return
        self.size -= 1
        self.head = self.head.get_next()
        return 

    def delete(self, element):
        """Delete element in list
        T = O(n)
        """
        if self.get_size() == 0:
            raise Exception('Linked List is empty.')
        helpty = self.head
        prev = None
        while helpty:
            if helpty.get_data() == element:
                if prev is None:
                    self.delete_first()
                    return True
                if helpty.get_next() is None:
                    self.tail = prev
                    self.tail.set_next_element(None)
                    self.size -= 1
                    return True
                prev.set_next_element(helpty.get_next())
                self.size -= 1
                return True
            prev = helpty
            helpty = helpty.get_next()
        return False

    def sort(self, *, reverse=False):
        """Method sort linked list use algorithm selection sort."""
        if self.get_size() == 0:
            raise Exception('Linked List is empty.')
        self._selection_sort(reverse)

    def _selection_sort(self, reverse):
        """Selection sort:
        T = theta(n**2)
        """
        helpty = self.head
        prev = None
        while helpty:
            min_element = helpty
            helpty2 = min_element.get_next()
            prev2 = helpty
            chance = None
            seet = 0
            remind = False
            while helpty2:
                if self._helpty_fun(helpty2, min_element, reverse): 
                    remind = True
                    if seet > 0:
                        chance = prev2
                    min_element = helpty2 
                seet += 1
                prev2 = prev2.get_next()
                helpty2 = helpty2.get_next()
            if not remind:
                prev = helpty
                helpty = helpty.get_next()
                continue
            if prev is None:
                if chance is None:
                    self.head = min_element
                    helpty.set_next_element(min_element.get_next())
                    self.head.set_next_element(helpty)
                else:
                    node = helpty.get_next()
                    helpty.set_next_element(min_element.get_next())
                    chance.set_next_element(helpty)
                    self.head = min_element
                    self.head.set_next_element(node)
                helpty = self.head
            else:
                if chance is None:
                    chance = helpty
                    helpty.set_next_element(min_element.get_next())
                    prev.set_next_element(min_element)
                    min_element.set_next_element(chance)
                else:
                    node = helpty.get_next()
                    prev.set_next_element(min_element)
                    helpty.set_next_element(min_element.get_next())
                    chance.set_next_element(helpty)
                    min_element.set_next_element(node)
                helpty = min_element
            prev = helpty
            helpty = helpty.get_next()
        self.tail = prev
        self.tail.set_next_element(None)

    def _helpty_fun(self, a, b, reverse):
        """Help function for selection sort"""
        if reverse:
            return a.get_data() > b.get_data()
        return a.get_data() < b.get_data()

    def clear(self):
        """Method clear linked list."""
        self.head, self.tail = None, None
        return True
        
    def __repr__(self):
        """Representation object."""
        help_list = []
        helpty = self.head
        while helpty:
            help_list.append(helpty)
            helpty = helpty.get_next()
        return f'{help_list}'

if __name__ == "__main__":
    test = LinkedList()
    for x in range(1, 100):
        test.insert(x)
    print(test.head)
    print(test.tail)
    print(test)
    print(test.tail)
    print(test.head)
    print(test.search(120))
    print(test)
    print(test.delete(1))
    print(test)
    print(test.tail)
    print(test.head)
    test.append(20)
    print(test)
    test.sort()
    print(test)
    print(100 * '*')
    test2 = LinkedList()
    [test2.insert(randint(1, 900)) for _ in range(1, 101)]
    print(test2)
    test2.sort()
    print(test2)
    print(test2.head)
    print(test2.tail)
    test2.append(-1000)
    test2.insert(900000)
    print(test2)
    test2.sort(reverse=True)
    print(test2)
    print(test2.head)
    print(test2.tail)
    test2.clear()
    print(test2)
    





    
            

    