class HashTable:
    """Hash table using open addressing"""
    
    def __init__(self, size):
        assert type(size) == int, "Must be type int"
        self.table = [None for _ in range(size)]
        self.size = size

    def _hash_function(self, key):
        """Helpty hash function."""
        return key % self.size

    def _main_hash_function(self, key):
        """Main hash function."""
        for idx in range(self.size):
            yield (self._hash_function(key) + idx) % self.size

    def _slot_is_empty(self, idx):
        """Check slot is empty"""
        return self.table[idx] is None or self.table[idx] == "DELETE"

    def insert(self, key, data):
        """Insert key wit data to hash table."""
        for idx in self._main_hash_function(key):
            if  self._slot_is_empty(idx):
                self.table[idx] = (key, data)
                return True
        raise Exception('Hash table is full.')

    def search(self, key):
        """Search key in hashtable, return Data."""
        for idx in self._main_hash_function(key):
            if self.table[idx][0] == key:
                return self.table[idx][1]
            elif self.table[idx] == None:
                break
        return False

    def delete(self, key):
        """Delete key and data with hash table."""
        for idx in self._main_hash_function(key):
            if self.table[idx][0] == key:
                self.table[idx] = 'DELETE'
                return True
            elif self._slot_is_empty(idx):
                break
        return False

    def __repr__(self):
        return f'{self.table}'

if __name__ =="__main__":
    a = HashTable(11)
    for idx in range(11):
        a.insert(idx, idx**2)
    print(a)
    print(a.search(10))
    print(a.delete(0))
    print(a)
    print(a.insert(10, 'ok'))
    print(a)
