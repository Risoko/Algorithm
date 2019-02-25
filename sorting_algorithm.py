from random import randint

class Sorting:

    def __init__(self, table):
        assert type(table) == list, "Must be list"
        self.table = table

    def sort(self, number_sort=4):
        """You can check sorting algorithm
        1. Bubble Sort
        2. Selection Sort
        3. Insertion Sort
        4. Quick Sort
        5. Merge Sort
        6. Radix Sort
        7. Counting Sort
        """
        dict_with_algo = {
            1 : self._bubble_sort_classic(),
            2 : self._selection_sort(),
            3 : self._insertion_sort(),
            4 : self._quick_sort(),
            5 : self._merge_sort(),
            6 : self._counting_sort(),
            7 : self._radix_sort()
        }
        return dict_with_algo.get(number_sort, 'No algorithm')

    def _bubble_sort_classic(self):
        """Bubble Sort Algorithm:
         Tmax = theta(n**2)
         Tave = theta(n**2)
         Tmin = theta(n**2)
         Stable: Yes
         """
        copyL = self.table[:]
        for index in range(len(copyL) - 2, -1, -1):
            for idx in range(0, index + 1):
                if copyL[idx] > copyL[idx+1]:
                    copyL[idx], copyL[idx+1] = copyL[idx+1], copyL[idx]
        return copyL

    def _selection_sort(self):
        """Selection Sort Algorithm:
         Tmax = theta(n**2)
         Tave = theta(n**2)
         Tmin = theta(n**2)
         Stable: No
         """
        copyL = self.table[:]
        for index in range(len(copyL) - 1):
            min_idx = index
            for index2 in range(index + 1, len(copyL)):
                if copyL[min_idx] > copyL[index2]:
                    min_idx = index2
            copyL[index], copyL[min_idx] = copyL[min_idx], copyL[index]
        return copyL

    def _insertion_sort(self):
        """Insertion Sort Algorithm:
         Tmax = theta(n)
         Tave = theta(n**2)
         Tmin = theta(n**2)
         Stable: Yes
         """
        copyL = self.table[:]
        for index in range(len(copyL) - 1, -1, -1):
            idx, key = index + 1, copyL[index]
            while idx < len(copyL) and key > copyL[idx]:
                copyL[idx-1] = copyL[idx]
                idx += 1
            copyL[idx-1] = key
        return copyL

    def _quick_sort(self, A=None, first=0, last=None):
        """Merge Sort Algorithm:
         Tmax = theta(nlgn)
         Tave = theta(nlgn)
         Tmin = O(n**2)
         Stable: Yes or No (depends on implementation) my algorithm is no stable
         """
        if A is None:
            A = self.table[:]
        if last is None:
            last = len(A) - 1
        if first < last:
            make_partitaion = self._partition(A, first, last)
            self._quick_sort(A, first, make_partitaion - 1)
            self._quick_sort(A, make_partitaion + 1, last)
        return A

    def _partition(self, A, first, last):
        """Function Partition:
        Complexity = theta(n)
        """
        indicator = first
        piwot = A[last]
        for index in range(first, last): #bez ostatniego bo tam jest piwot
            if A[index] <= piwot:
                A[index], A[indicator] = A[indicator], A[index]
                indicator += 1
        A[indicator], A[last] = A[last], A[indicator]
        return indicator

    def _merge_sort(self, table=None):
        """Merge Sort Algorithm:
         Tmax = theta(nlgn)
         Tave = theta(nlgn)
         Tmin = theta(nlgn)
         Stable: Yes or No (depends on implementation Merge) my algorithm is stable
         """
        if table is None:
            table = self.table[:]
        if len(table) <= 1:
            return table
        mid = len(table) // 2
        left = self._merge_sort(table[mid:])
        right = self._merge_sort(table[:mid])
        return self._merge(left, right)

    def _merge(self, left, right):
        """Function Merge:
        Complexity = theta(n)
        """
        helpty, idx_left, idx_right = [], 0, 0
        while idx_left < len(left) and idx_right < len(right):
            if left[idx_left] < right[idx_right]:
                helpty.append(left[idx_left])
                idx_left += 1
            else:
                helpty.append(right[idx_right])
                idx_right += 1
        helpty += left[idx_left:]
        helpty += right[idx_right:]
        return helpty

    def _counting_sort(self):
        """Counting Sort Algorithm:
         Tmax = theta(n)
         Tave = theta(n)
         Tmin = theta(n)
         Stable: Yes 
         """
        A = self.table[:]
        counts = [0 for i in range(max(A) + 1)]
        for element in A:
            counts[element] += 1 
        for index in range(1, len(counts)):
            counts[index] = counts[index-1] + counts[index]
        output = [0 for _ in range(len(A))]
        for element in A:
            index = counts[element] - 1
            output[index] = element
            counts[element] -= 1 
        return output

    def _radix_sort(self):
        """Counting Sort Algorithm:
        Tmax = theta(n)
        Tave = theta(n)
        Tmin = theta(n)
        Stable: Yes 
        """
        A = self.table[:]
        max_value = max(A) 
        start = 1
        while max_value // start > 0: 
            A = self._counting_sort_radix(A, start) 
            start *= 10
        return A

    def _counting_sort_radix(self, A, start):
        """Function Counting Sort:
        Complexity = theta(n)
        """ 
        b = [0] * len(A)
        count = [0] * 10
        for i in range(0, len(A)): 
            index = A[i] // start
            count[index % 10] += 1
        for i in range(1, 10): 
            count[i] += count[i-1] 
        begin = len(A) - 1
        while begin >= 0: 
            index = A[begin] // start
            b[count[index % 10] - 1] = A[begin]
            count[index % 10] -= 1
            begin -= 1
        return b

    def __repr__(self):
        """Representation object dunder repr"""
        return f'{self.table}'

if __name__ == "__main__":
    lista = [randint(0, 300) for _ in range(1, 31)]
    lista_counting = [randint(0, 9) for _ in range(1, 31)]
    test = Sorting(lista)
    test2 = Sorting(lista_counting)
    print(f'List not sorting: {test} \nList sorting: {test.sort(7)}')
    print(f'List not sorting: {test2} \nList sorting: {test2.sort(6)}')
    
