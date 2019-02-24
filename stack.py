class Stack:

    def __init__(self):
        self.table = []

    def push(self, element):
        """Push element in stack:
        T = O(1)
        """
        self.table.append(element)
        return

    def get_size(self):
        """Return stack's size:
        T = O(1)
        """
        return len(self.table)

    def top(self):
        """Return last element in stack:
        T = O(1)
        """
        if self._is_empty():
            raise Exception('Stack is empty.')
        return self.table[-1]

    def pop(self):
        """Delete element in stack:
        T = O(1)
        """
        if self._is_empty():
            raise Exception('Stack is empty.')
        del self.table[-1]
        return

    def _is_empty(self):
        """Checks if the stack is empty:
        T = O(1)
        """
        return  self.get_size() == 0

    def __repr__(self):
        """REpresentation object."""
        return f'{self.table}'


if __name__ == '__main__':
    test = Stack()
    for element in range(1, 91):
        test.push(element**2)
    print(test)
    print(test.top())
    test.pop()
    print(test)
    print(test.top())
    print(test.get_size())
