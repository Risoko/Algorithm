class HashTable:
    """Hash table using direct addressing"""
    
    def __init__(self, size):
        assert type(size) == int, "Must be type int"
        self.table = [None for _ in range(size)]

    def insert(self, key, data):
        """Insert on hash table:
        complexity = O(1)
        """ 
        if self._check_position(key):
            self.table[key] = data
            return
        raise Exception('Position is busy')

    def _check_position(self, key):
        try:
            self.table[key] is None
        except IndexError:
            raise Exception('Index is too big')
        else:
            return self.table[key] is None

    def search(self, key):
        """Search on hash table:
        complexity = O(1)
        """ 
        if self._check_position(key):
            raise Exception('Position is empty.')
        return self.table[key]

    def delete(self, key):
        """Delete on hash table:
        complexity = O(1)
        """ 
        if self._check_position(key):
            raise Exception('Position is empty.')
        self.table[key] = None
        return True
    
    def __repr__(self):
        return f'{self.table}'

if __name__ == "__main__":
    a = HashTable(10)
    print(a)
    for idx in range(10):
        a.insert(idx, idx**2)
    print(a)
    print(a.search(4))
    print(a.delete(5))
    print(a)
