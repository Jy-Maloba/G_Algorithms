# divide and conquer works  by breaking a problem down into smaller pieces

# given an array of numbers [2,4,6] to add them up and return the total
#using loops
def sum(arr):
    total = 0
    for i in arr:
        total += i
    return total
print(sum([2,4,6]))

#using recursive function
