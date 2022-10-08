# Grokking algorithms

## CHAPTER 1
**Algorithm:** set of instructions for accomplishing a task

**Binary Search Algorithm**
Its input is a sorted list of elements. It returns an element from the list by starting the search halfway into the list instead of systematically. It uses logarithmic time O(log n)

**Simple search**
Searching systematically from the beginning to the end one by one. It uses linear time O(n)

**Big O Notation**
Is a special notation that tells you how fast an algorithm is (The run-time of the algorithm)
Big O counts the number of operations
It establishes worst case run-time
Algorithm speed is measured in growth of the number of operations
**Big O runtimes**
- O(log n ) log time: Binary search
- O(n) linear time: Simple search
- O(n log n) fast sorting algorithm:Quicksort algorithm
- O(n<sup>2</sup>) slow sorting algorithm: Selection sort
- O(n!) really slow algorithm: The traveling sales person

## CHAPTER 2
**How memory works**
**Arrays**
In arrays all elements are stored right next to each other in memory. If the spaces aren't enough for the entire array, the whole array will have to be moved to a different memory space where they can be stored next to each other.

In arrays you know the address of all the elements; you can jump from one item to the other, no need to follow a systematic approach from first item to last.
Elements in array are numbered starting from 0

You can request for extra memory spaces within the same line of addresses to prevent moving the entire array incase an addition of an element in the array is required. This is a good approach but it has its downside:
- you may not need the extra memory slots, the memory will be wasted
- you may add more than you requested and have to move anyway.
Linked list solve this problem.

The Runtime for arrays in reading is 0(1)
The Runtime for arrays in Insertion is 0(n)
The Runtime for arrays in deletion is 0(n)
Arrays allow fast reads.
All elements in an array should be the same type

**Linked list**
Here your Items can be anywhere in the memory
Each Item stores the address of the next item in the list. A bunch of random memory addresses are linked together.
Linked lists have one problem. To get to the last item in the list, you'll have to go through all the items in the list. You can't go straight to the last Item because the address of that last item is stored in the second last item...
Linked list are great if you are going to read all items one at a time

The Runtime for Linked lists in reading is 0(n)
The Runtime for Linked lists in writing is 0(1)
The Runtime for Linked lists in Deletion is 0(1)
Lists allow fast inserts and deletes

**Selection Sort**
Picking the largest item from a list and putting it in another list one by one
It takes O(n<sup>2</sup>) operations

## CHAPTER 3
**Recursion**
used when you need to continously revisit an element that contains other elements
A recursion function calls itself. It has a base case and a recursive case:
- base case is when the function stops calling  itself so it doesn't go into an infinite looping
- recursive case is when the function calls itself
def countdown(i):
    print(i)
    if i <= 0: //base case
        return
    else:
        countdown(1-i) //recursive case

**The Stack**
(a pile of elements stacked horizontally.)
Is a list of items like arrays or linked list except addition is done to the top of the list, reading and removal is also done to the element at the top of the list 
A stack has 2 operations: 
- push: adding an item into the stack
- pop: removing an item from the stack
**call stack**
when a function is called within another function before coming back to complete its execution. refer from(stack.py)
All function calls go into the call stack
The call stack gets very large, which takes up alot of memory.

## CHAPTER 4
**Divide and Conquer**
Algorithms aren't very useful if they can only solve one problem. D&C gives you a new way to think ablut solving problems
D&C algorithms are recursive algorithms. To solve a problem using it, there are 2 steps:
- Figure out the base case. This should be the simplest possible case
- Divide or decrease your problem until it becomes the base case
It can use recursion as it divides the problem to find the base case
When you’re writing a recursive function involving an array, the base case is often an empty array or an array with one element. 

**Quicksort**
It also uses D&C. It is a much faster algorithm
Arrays with 0 or 1 element should be returned as they are. there's nothing to sort

How it works:
D&C works by breaking a problem down into smaller and smaller
pieces. If you’re using D&C on a list, the base case is probably an empty array or an array with one element.

- pick a random element from the array (a pivot)
- find elements smaller and larger than the pivot (partitioning). now you have 2 sub-arrays of smaller and larger elements.
- Call quicksort recursively on the 2 sub-arrays. quicksort(smaller) + pivot + quicksort(larger). This gives you a sorted array from the smallest to the largest.

It works with any pivot in arrays with more than 2 elements.

Quicksort's speed depends on the pivot you choose
In the worst case quicksort takes O(n<sup>2</sup>)
In the average case quicksort takes O(n log n)
Merge sort takes O(n log n)

Quicksort has a smaller constant than merge sort, so if they are both O(n log n) time, quicksort is faster. 
Quicksort hits the average case way more often than worst case.

Picking the middle element as the pivot reduces the call stack, you don't need to make any recursive calls; you hit the base case much sooner. The call stack is much shorter.

worst case scenario is when you pick the first element as your pivot
Best case scenario is when you pick the middle element as your pivot.

**Inductive proof**
A way to prove that your algorithm works
It has 2 steps using the example of quicksort:
- base case: show that the algorithm works for base case 0 and 1
- inductive case: if it works for arrays of size 2, it will work for 3, if it works for 3, it will work for 4...etc

## CHAPTER 5
**Hash Tables**
also known as hash map, maps, dictionaries and associated arrays. It is a fast data structure. they take O(1) at an average case.. which is constant time(time will stay the same regardless of how big the hash table is).
Hash tables have really fast search, insert, and delete.
In worst case, it takes O(n) linear time which is really slow.

Dictionaries in python is an example of a hash table.
hash table is a hash function combined with an array
A hash function is where you put in a string and you get back a number. 
maps a name to an index.

A hash function maps strings to numbers
The requirements for a hash function are:
- It needs to be cosistent. If you set "apple" to 4, every time you call "apple" you should get 4
- It should map different words to different numbers. every string with its own number.

Hash tables have some extra logic behind them than other data structures like arrays and lists use hash functions to intelligently figure out where to store elements

Hash tables have keys and values, map the keys to the values..

Hash tables are great when you want to create a mapping from one thing to another, filter out duplicates, cache/memorize data and when you want to look something up.

**Caching** this is when a computer saves user activity in memory so it doesn't have to go to the original source to fetch it when the user needs it some other time. 
Cashing makes things faster.
Data is cached in Hash

**Collisions**
This is when 2 keys are assigned the same slot in array memory. one overwrites the other causing a problem.
This can be solved by creating a linked list at that slot. which slows down the searching process.
A good hash function will give you very few collisions

**Performance**
To avoid collisions you need:
- low load factor calculation (number of items in hash table/total number of slots). load factor measures how many empty slots remain in the hash table. having a load factor greater than 1 means that you have more items than slots in your array. you need to add more slots(resizing). resize when your load factor is greater than 0.7. hash table takes O(1) even with resizing.
- a good hash function: distributes values in the array evenly
