def linear_search(items, target):
    for position, item in enumerate(items):
        if item == target:
            return position
   
    raise ValueError("%s was not found in the list." % desired_item)