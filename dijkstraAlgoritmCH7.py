#breadth first search finds the path with the fewest nodes
#BFS, can work on unweighted graph

#Dijkstra algorithm finds the path with the least cost/time/Weight
#Dijkstra works on weighted and directed acyclic graphs
#Dijkstra doesn't use negative weight edges, 
#negative weight edges are used in Bellman-ford algorithm

#DIJKSTRA ALGORITHM
# Find the cheapest node. his is the node you can get to in the least
# amount of time.
# 2. Check whether there’s a cheaper path to the neighbors of this node.
# If so, update their costs.
# 3. Repeat until you’ve done this for every node in the graph.
# 4. Calculate the inal path.

#nodes and their neighbours
graph = {}
graph["start"]["a"]=6
graph["start"]["b"]=2

graph["a"] = {}
graph["a"]["fin"]=1

graph["b"]={}
graph["b"]["a"]=3
graph["b"]["fin"]=5

graph["fin"] = {}

#hash table for cost of each node
infinity = float("inf")
costs={}
costs["a"]=6
costs["b"]=2
costs["fin"]=infinity

#hash table for the parents
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs: #Go through each node.
        cost = costs[node]
        if cost < lowest_cost and node not in processed: #if it is the lowest cost so far and hasn't been processed yet
            lowest_cost = cost #… set it as the new lowest-cost node.
            lowest_cost_node = node
    return lowest_cost_node

#an array to keep track of nodes already processed
processed = []

node = find_lowest_cost_node(costs)#find the lowest cost node that you haven't processed yet
while node is not None: #if you have processed all the nodes this while loop is done
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys(): #go through all the neighbours of this node
        new_cost = cost + neighbors[n] #if it is cheaper to get to this neighbour
        if costs[n] > new_cost: #by going through this node
            costs[n] = new_cost #update the cost of this node
            parents[n] = node #this node becomes the new parent for this neighbour

processed.append(node) #mark the node as processed
node = find_lowest_cost_node(costs) #find the next node to process and loop