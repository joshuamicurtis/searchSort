import time
from linearSearch import linear_search
from binarySearch import binary_search

def print_timing(func):
    def wrapper(*arg):
        t1 = time.clock()
        res = func(*arg)
        t2 = time.clock()
        print '%s took %0.3fms' % (func.func_name, (t2-t1)*1000.0)
        return res
    return wrapper

if __name__ == "__main__":      
    items = []
    for i in range (100000):
        items.append(i)


    t1 = time.clock()  
    print linear_search(items, 99999) 
    t2 = time.clock()
    print 'linear_search took %0.3fms' % ((t2-t1)*1000.0)
    t1 = time.clock()
    print binary_search(items, 99999)   
    t2 = time.clock()
    print 'binary_search took %0.3fms' % ((t2-t1)*1000.0)   