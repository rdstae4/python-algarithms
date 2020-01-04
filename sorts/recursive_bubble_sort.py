def bubble_sort(list1):
    """
    It is similar is bubble sort but recursive.
    :param list1: mutable ordered sequence of elements
    :return: the same list in ascending order    
    """

    for i, num in enumerate(list1): 
        try: 
            if list1[i+1] < num: 
                list1[i] = list1[i+1] 
                list1[i+1] = num 
                bubble_sort(list1) 
        except IndexError: 
            pass
    return list1 

if __name__ == "__main__":     
    list1 = [22,66,33,99,11]    
    bubble_sort(list1) 
    if(len(list1) == 0):
        print("Empty list")
    else:
        print("Sorted array:")
        for i in range(0, len(list1)): 
            print(list1[i], end=' ') 
