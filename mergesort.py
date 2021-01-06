def mergeSort(myList):
    if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]

        print ("mid :",mid)
        print ("left : ",left)
        print ("right :",right)

        # Recursive call on each half
        mergeSort(left)
        mergeSort(right)

        # Two iterators for traversiting the two halves
        i = 0
        j = 0

        # Iteraror for the main list
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                # The value from the left half has been used
                myList[k] = left[i]
                print("Current Results :",myList)
                # move the iterator forward
                i += 1
            else:
                myList[k] = right[j]
                print ("Current Results :",myList)
                j += 1
            # move to the next slot
            k += 1
        
        # for all the remaining values
        while i < len(left):
            myList[k] = left[i]
            print ("Current Results :",myList)
            i += 1
            k += 1

        while j < len(right):
            myList[k] = right[j]
            print ("Current Results :",myList)
            j += 1
            k += 1

myList = [54,26,93,17,77,31,44,55,20]
print (myList)
mergeSort(myList)
print (myList)