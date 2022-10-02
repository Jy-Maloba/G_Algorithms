def binary_search(list, item):
    low = 0
    high = len(list)-1

    while low<= high:
        mid = (low+high)/2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid -1
        else:
            low = mid + 1
    return None
my_list = [1, 3, 5, 7, 9]

#logs are the flip of exponentials
# 10**2=100 ---> log_10 100 = 2

# suppose you are looking for a word in a dictionary with 240,000 words. Using binary search, it will take you log_2 240,000 steps which is 18 steps to get to the word

#Exercises
#1. Suppose you have a sorted list of 128 names, and you’re searching
#   through it using binary search. What’s the maximum number of
#   steps it would take?
# answer: log_2 128 = 7 times

#2. Suppose you double the size of the list. What’s the maximum
# number of steps now?
#   answer: log_2 10 = 3 times

#binary search uses logarithmic time O(log n)
#simple search uses linear time O(n). searching one by one from the beginning to the end.

#