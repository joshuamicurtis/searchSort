def bubble_sort(items):
    """ Implementation of bubble sort 
        O(n^2) run time. 
        Not very useful.
    """
    
    for i in range(len(items)):
        for j in range(len(items)-1-i):
            if items[j] > items[j+1]:
                items[j], items[j+1] = items[j+1], items[j]