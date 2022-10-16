#intro to graphs
# a graph models a set of connections. It is made up of nodes and edges(circles and connecting lines/arrows)
# nodes directly connected are called neighbours
#Directed graph has arrows and the relationship follow the direction of the arrow(Rama --> Adit) means Rama owes Adit
#Undirected graphs have no arrows and the relationship goes both ways
#Queue uses FIFO data structure
#Stack uses LIFO
#implementing the graph

graph = {}
graph["you"] = ["alice", "bob", "claire"]

#graph with multiple nodes

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

#the order doesn't matter

#BREADTH FIRST SEARCH---Implementing the Algorithm
#It is a first in first out data structure (FIFO)
#It tells you whether there is a pathe from A to B, if there is, It gives you the shortest path

from collections import deque
#pseudocode

def person_is_seller(name):
    return name[-1] == "m" #checks wheather the person's name ends with letter m, if it does, they are a mango seller

# search_queue = deque() #create a new queue
# search_queue += graph["you"] #add all your neighbours to the queue

# while search_queue: #while the queue is not empty
#     person = search_queue.popleft() #grab the first person off the queue
#     if person_is_seller(person):
#         print(person + "is a mango seller! ") #yes they are
#         return True
#     else:
#         search_queue+= graph[person] # no they aren't, add all of their friends to the search queue
# return False # no one in the queue is a mango seller



#keep a list of people you have already checked to avoid repetition/ infinite loop

def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = [] #this array stores people that have already been searched for
    while search_queue:
        person = search_queue.popleft()
        if not person in searched: # search the person if you haven't done it yet
            if person_is_seller(person):
                print (person + " is a mango seller!")
                return True
            else:
                search_queue += graph[person]
                searched.append(person) #mark the person as searched
    return False
search("you")

#The runtime for breadth first search is O(number of people+number of edges)
# commonly written as O(V+E)
#V for number of vertices and E for number of edges

#A tree is a special type of graph where no edges ever point backwards(e.g - familiy tree)

#you need to check nodes in the order they were added to the search list..so the search list needs to be a queue to get the shortest path
