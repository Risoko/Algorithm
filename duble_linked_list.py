from random import randint

class _Node:
    
    def __init__(self, next_element=None, prev=None, data=None):
        self.next = next_element
        self.data = data
        self.prev = prev

    def get_prev(self):
        """Return prev element
        T = O(1)
        """
        return self.prev

    def set_prev_element(self, prev_element):
        """Set prev element
        T = O(1)
        """
        self.prev = prev_element

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

class DubleLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get_size(self):
        """Return size linked list:
        T = O(1)
        """
        return self.size

    def append(self, element):
        """Append element for last position 
        T = O(1)
        """
        new_element = _Node(data=element)
        if self.head is None:
            self.head = new_element
            self.tail = new_element
            self.size += 1
            return
        self.tail.set_next_element(new_element)
        new_element.set_prev_element(self.tail)
        self.tail = new_element
        self.size += 1
        return

    def insert(self, element):
        """Insert element for first position 
        T = O(1)
        """
        new_element = _Node(data=element)
        if self.head is None:
            self.head = new_element
            self.tail = new_element
            self.size += 1
            return
        new_element.set_next_element(self.head)
        self.head.set_prev_element(new_element)
        self.head = new_element
        self.size += 1
        return

    def delete_first(self):
        """Delete first element
        T = O(1)
        """
        if self.get_size() == 0:
            raise Exception('List is empty.')
        elif self.get_size() == 1:
            self.head = None
            self.tail = None
            self.size -= 1
            return True
        self.head = self.head.get_next()
        self.head.set_prev_element(None)
        self.size -= 1
        return True

    def delete_last(self):
        """Delete last element
        T = O(1)
        """
        if self.get_size() == 0:
            raise Exception('List is empty.')
        elif self.get_size() == 1:
            self.head = None
            self.tail = None
            self.size -= 1
            return True
        self.tail = self.tail.get_prev()
        self.tail.set_next_element(None)
        self.size -= 1
        return True

    def delete(self, element):
        """Delete element in list
        T = O(n)
        """
        if self.get_size() == 0:
            raise Exception('List is empty.')
        helpty = self.head
        while helpty:
            if helpty.get_data() == element:
                if helpty.get_next() is None:
                    self.delete_last()
                    return True
                elif helpty.get_prev() is None:
                    self.delete_first()
                    return True
                else:
                    helpty.get_prev().set_next_element(helpty.get_next())
                    helpty.get_next().set_prev_element(helpty.get_prev())
                    self.size -= 1
                    return True
            helpty = helpty.get_next()
        return False 

    def sort(self, reverse=False):
        """Method sort linked list:
        T = Theta(nlgn) + 2n.
        """
        if self.get_size() == 0:
            raise Exception('List is empty.')
        help_list = []
        helpty = self.head
        while helpty:
            help_list.append(helpty.get_data())
            helpty = helpty.get_next()
        help_list.sort(reverse=reverse)
        self.clear()
        for element in help_list:
            self.append(element)
        
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

    def clear(self):
        """Method clear list."""
        self.tail, self.head = None, None
        return 

    def __repr__(self):
        """Representation object."""
        help_list = []
        helpty = self.head
        while helpty:
            help_list.append(helpty)
            helpty = helpty.get_next()
        return f'{help_list}'

if __name__ == '__main__':
    test = DubleLinkedList()
    [test.insert(randint(-100, 100)) for _ in range(100)]
    print(test)
    test.sort(True)
    print(test)


