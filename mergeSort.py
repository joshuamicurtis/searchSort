def merge_sort_recursive(items):
    """ Implementation of mergesort 
        O (nlog(n)) run time
    """
    # Base case items has zero or one element and is by definition sorted
    if len(items) <= 1:
        return items
    
    mid = len(items) / 2            # Determine the midpoint and 
    left = items[0:mid]             # split into left and right
    right = items[mid:]
    
    merge_sort_recursive(left)      # Sort left list
    merge_sort_recursive(right)     # Sort right list
    return merge(left, right)       # Merge left and right lists
    
def merge(left, right): 
    result = []
    indexL, indexR = 0, 0
    while indexL < len(left) and indexR < len(right):
        if left[indexL] <= right[indexR]:
            result.append(left[indexL])
            indexL += 1
        else:
            result.append(right[indexR])
            indexR += 1
    
    # One of the lists will have elements left. 
    # Only one of the loops will be entered
    while indexL < len(left):
        result.append(left[indexL])
        indexL += 1
    while indexR < len(right):
        result.append(right[indexR])
        indexR += 1
    return result