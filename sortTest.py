# Test different sorting algorithms implemented in Python
# A random list is created, and each algorithm uses that same list

import random
import time
import heapq

N = 1000
list1 = []

for i in range(N):
    list1.append(random.randint(0, N-1))
    
#print list1

def print_timing(func):
    def wrapper(*arg):
        t1 = time.clock()
        res = func(*arg)
        t2 = time.clock()
        print '%s took %0.3fms' % (func.func_name, (t2-t1)*1000.0)
        return res
    return wrapper
    
@print_timing
def bubble_sort(items):
    """ Implementation of bubble sort 
        O(n^2) run time. 
        Not very useful.
    """
    
    for i in range(len(items)):
        for j in range(len(items)-1-i):
            if items[j] > items[j+1]:
                items[j], items[j+1] = items[j+1], items[j]
    #print items

@print_timing
def insertion_sort(items):
    """ Implementation of insertion sort 
        O(n^2) run time.
    """
    for i in range(1, len(items)):
        j = i
        while j > 0 and items[j] < items[j-1]:
            items[j], items[j-1] = items[j-1], items[j]
            j-=1
    #print items

@print_timing
def merge_sort(items):
    merge_sort_recursive(items)
    #print items
   
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
        
# quick sort
@print_timing
def quick_sort(list2):
    quick_sort_r(list2, 0, len(list2) - 1)
    #print list2
# quick_sort_r, recursive (used by quick_sort)
def quick_sort_r(list2 , first, last):
    if last > first:
        pivot = partition(list2, first, last)
        quick_sort_r(list2, first, pivot - 1)
        quick_sort_r(list2, pivot + 1, last)
# partition (used by quick_sort_r)
def partition(list2, first, last):
    sred = (first + last)/2
    if list2[first] > list2 [sred]:
        list2[first], list2[sred] = list2[sred], list2[first]  # swap
    if list2[first] > list2 [last]:
        list2[first], list2[last] = list2[last], list2[first]  # swap
    if list2[sred] > list2[last]:
        list2[sred], list2[last] = list2[last], list2[sred]    # swap
    list2 [sred], list2 [first] = list2[first], list2[sred]    # swap
    pivot = first
    i = first + 1
    j = last
  
    while True:
        while i <= last and list2[i] <= list2[pivot]:
            i += 1
        while j >= first and list2[j] > list2[pivot]:
            j -= 1
        if i >= j:
            break
        else:
            list2[i], list2[j] = list2[j], list2[i]  # swap
    list2[j], list2[pivot] = list2[pivot], list2[j]  # swap
    return j

# heap sort
@print_timing
def heap_sort(items):
    first = 0
    last = len(items) - 1
    create_heap(items, first, last)
    for i in range(last, first, -1):
        items[i], items[first] = items[first], items[i]
        establish_heap_property(items, first, i - 1)
    #print items
        
# create_heap (used by heap_sort)
def create_heap(items, first, last):
    i = last/2
    while i >= first:
        establish_heap_property(items, i, last)
        i -= 1
        
# establish_heap_property (used by create_heap)
def establish_heap_property(items, first, last):
    while 2 * first + 1 <= last:
        k = 2 * first + 1
        if k < last and items[k] < items[k+1]:
            k += 1
        if items[first] >= items[k]:
            break
        items[first], items[k] = items[k], items[first]
        first = k

#python heap sort
@print_timing
def python_heap_sort(items):
    """ Implementation of heap sort using python's heapq module"""
    heapq.heapify(items)
    items[:] = [heapq.heappop(items) for i in range(len(items))]
    
@print_timing
def python_sort(items):
    """Use python's built in sort method"""
    items.sort
 
if __name__ == "__main__" :
    list2 = list(list1)
    bubble_sort(list2)
    insertion_sort(list2)
    merge_sort(list2)
    quick_sort(list2)
    heap_sort(list2)
    python_heap_sort(list2)
    python_sort(list2)