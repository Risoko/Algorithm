from collections import namedtuple
Position = namedtuple('Position', 'Index_in_HT Data')

class HashTable:
    """Hash table using chain method."""

    def __init__(self, size):
        assert type(size) == int, "Must be type int"
        self.size = size
        self.table = [[] for _ in range(size)]

    def _function_hash(self, key):
        """Hashing Function"""
        return key % self.size

    def insert(self, key, data):
        """Insert on hash table:
        Tmin = O(1)
        Tave = O(1)
        Tmax = Theta(n)
        """ 
        bucket = self.table[self._function_hash(key)]
        for index in range(len(bucket)):
            if bucket[index][0] == key:
                bucket[index][1] = data
                return
        bucket.append([key, data])
        return

    def search(self, key):
        """Insert on hash table:
        Tmin = O(1)
        Tave = O(1)
        Tmax = Theta(n)
        """ 
        index = self._function_hash(key)
        bucket = self.table[index]
        for idx in range(len(bucket)):
            if bucket[idx][0] == key:
                return Position(index, bucket[idx][1])
        return Position(False, False)

    def delete(self, key):
        """Insert on hash table:
        Tmin = O(1)
        Tave = O(1)
        Tmax = Theta(n)
        """ 
        index = self._function_hash(key)
        bucket = self.table[index]
        for idx in range(len(bucket)):
            if bucket[idx][0] == key:
                del bucket[idx]
                return True
        return False

    def __repr__(self):
        return f'{self.table}'

if __name__ == "__main__":
    a = HashTable(9)
    print(a)
    print(100 * '*')
    for x in range(21):
        a.insert(x, x**2)
    print(a)
    print(100 * '*')
    a.insert(0, 100000000)
    print(a)
    print(a.search(10))
    print(100 * '*')
    print(a.delete(10))
    print(a)
    a.insert(1, 11111)
    print(a)
