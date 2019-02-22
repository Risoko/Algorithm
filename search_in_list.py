def linear_search(L, key):
    """Search key in list.
    Complexity = Theta(n)
    """
    for element in L:
        if element == key:
            return True
    return False

def binary_search(L, key):
    """Search key in list.
    ONLY SORT LIST
    Complexity = Theta(log(n))
    """
    mid = len(L) // 2
    if len(L) == 2:
        return L[0] == key or L[1] == key
    if L[mid] == key:
        return True
    elif L[mid] > key:
        return binary_search(L[:mid], key)
    else:
        return binary_search(L[mid:], key)

if __name__ == "__main__":
    print(linear_search([10, 90, -1, 1, 1000], 100000))
    print(binary_search([element for element in range(10)], 9))