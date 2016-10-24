def binary_search(items, target, start=0, end=None):
    if end == None:
        end = len(items)
        
    if start == end:
        raise ValueError("%s was not found in the list." % target)
        
    pos = (end - start) // 2 + start
    print "pos:", pos
    
    if target == items[pos]:
        return pos
    elif target > items[pos]:
        return binary_search(items, target, start=(pos + 1), end=end)
    else: # target < items[pos]
        return binary_search(items, target, start=start, end=pos)