# choose a random element as the pivot  the average runtime of quicksort is  o( n log n)
# Empty arrays and arrays with just one element will be the base case. You
# can just return those arrays as is—there’s nothing to sort:

# def quicksort(array):
#     if len(array) < 2:
#         return array

# for arrays with 2 or more elements  
def quicksort(array):
    if len(array) <2:
        return array
    else:
        pivot = array[0] #recursive case
        less = [i for i in array[1:] if i <= pivot] #sub arrays for all elements less than the pivot
        greater = [i for i in array[1:] if i > pivot] # sub arrays of all elements greater than the pivot
        return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([10, 5, 2, 3]))

#quicksort and merge sort both use O(n log n) quicksort is faster
# quicksort has a smaller constant than merge sort.
# constant is the fixed amount of time that the algorithm takes
