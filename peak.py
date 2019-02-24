class Peak:

    def __init__(self, table):
        self._check_table(table)
        self.table = table

    def _check_table(self, table):
        """Method check table"""
        assert type(table) == list, 'Must be list'
        if table and table[0]:
            try:
                lenght = len(table[0])
            except TypeError:
                raise Exception('List mus be 2D not 1D')
            for element in table[1:]:
                if len(element) == lenght:
                    continue
                else:
                    raise Exception('Element must be the same size')
        else:
            raise Exception('Element must not empty.')
    

    def _check_left(self, position):
        """Check if the item is larger than the left one."""
        idx, idx2 = position
        try:
            if idx2 - 1 < 0:
                raise IndexError
            left = self.table[idx][idx2-1]
        except IndexError:
            return True
        else:
            return left < self.table[idx][idx2]
        

    def _check_right(self, position):
        """Check if the item is larger than the right one."""
        idx, idx2 = position
        try:
            right = self.table[idx][idx2+1]
        except IndexError:
            return True
        else:
            return right < self.table[idx][idx2]

    def _check_down(self, position):
        """Check if the item is larger than the down one."""
        idx, idx2 = position
        try:
            down = self.table[idx+1][idx2]
        except IndexError:
            return True
        else:
            return down < self.table[idx][idx2]

    def _check_up(self, position):
        """Check if the item is larger than the up one."""
        idx, idx2 = position
        try:
            if idx - 1 < 0:
                raise IndexError
            up = self.table[idx-1][idx2]
        except IndexError:
            return True
        else:
            return up < self.table[idx][idx2]

    def _is_peak(self, position):
        """Checks if the element is a peak."""
        return all((self._check_down(position),
                    self._check_left(position),
                    self._check_right(position),
                    self._check_up(position)
                    ))

    def _brute_force(self):
        """Search peak use brute force algorithm."""
        for idx1 in range(len(self.table)):
            for idx2 in range(len(self.table[idx1])):
                position = (idx1, idx2)
                if self._is_peak(position):
                    return position
    
    def _ascend_gradient(self, start=(0,0)):
        """Search peak use ascend gradient algorithm."""
        idx, idx2 = start
        number = 0
        my_dict = {
            1 : self._check_right,
            2 : self._check_down,
            3 : self._check_left,
            4 : self._check_up
        }
        right, down, left, up = True, True, True, True
        while True:
            number += 1
            while my_dict.get(number)((idx, idx2)) == False:
                if number == 1:
                    idx2 += 1
                    right = False
                elif number == 2:
                    idx += 1
                    down = False
                elif number == 3:
                    idx2 -= 1
                    left = False
                elif number == 4:
                    idx -= 1
                    up = False
            if number == 4 and all((right, down, left, up)):
                return (idx, idx2)
            elif number == 4:
                right, down, left, up = True, True, True, True
                number = 0
    
    def _divide_and_command(self):
        """Search peak use divide and command algorithm."""
        table = self.table[:]
        while True:
            mid = len(table[0]) // 2
            max_idx = 0
            for index in range(1, len(table)):
                if table[max_idx][mid] < table[index][mid]:
                    max_idx = index
            position = (max_idx, self.table[max_idx].index(table[max_idx][mid]))
            if self._check_left(position) and self._check_right(position):
                return position
            elif self._check_left(position):
                for idx in range(len(table)):
                    table[idx] = table[idx][mid:]
            elif self._check_right(position):
                for idx in range(len(table)):
                    table[idx] = table[idx][:mid]

    def search_peak(self, algorithm=1):
        """Return Peak in table 
        Algorithm:
        1 - Divide and command
        2 - Ascend gradient
        3 - Brut force
        """
        help_dict = {
            1 : self._divide_and_command(),
            2 : self._ascend_gradient(),
            3 : self._brute_force()
        }
        return help_dict.get(algorithm, 'No implement algorithm')

if __name__ == "__main__":
    A = [
        [16,   1,  3,  4],
        [17, 15, 16,  5],
        [13, 1, 17,  6],
        [12,  9,  3,  7],
        [11, 10,  9,  1]
        ]
    B = [[1,2,3,4,5]]
    C = [[2]]
    D = [
        [1,   2,  3,  4],
        [14, 15, 16,  5],
        [13, 18, 17,  6],
        [12,  9,  3,  7],
        [11, 10,  9,  8]
        ]
    E = [
        [4, 5, 6, 8, 9],
        [90, 8, 0, 9, 7],
        [8, 9, 1, 10, 1000],
        [1, 3, 1, 9, 900]
    ]
    F = [[1],
         [90],
         [3],]
    test = Peak(E)
    print(test.search_peak(3))

    
   
    
    
