#import needed libraries
from math import sqrt, inf
import matplotlib.pyplot as plt
import random
import pandas as pd

#function to calculate distance between two given nodes
def distance(n1, n2):
    return sqrt((n1[0] - n2[0])**2 + (n1[1] - n2[1])**2)

def nearest_neighbor(node, u = 0):
    print("Jupí, funguju! Pracuju na NN.")
    #set all nodes as unprocessed, create a cycle and initialize it's weigh
    state_of_nodes = ["N"] * (len(node))
    h_cycle = []
    W = 0

    #selecting starting point and setting it as a current node
    start = u
    start_i = node[start]

    #add current node to cycle and change it's status
    state_of_nodes[start] = "D"
    h_cycle.append(start_i)

    #as long as any unprocessed nodes exist
    while "N" in state_of_nodes:
        
        #set minimum distance to infinity
        min_distance = inf

        for index in range(len(node)):

            #get unprocessed nodes
            if state_of_nodes[index] == "N":

                #calculate distance between current node and next node
                dist = distance(start_i, node[index])

                #change minimum distance if the calculated distance is smaller than current min distance
                if dist < min_distance and state_of_nodes[index] != "D":
                    min_distance = dist

                    #save index and nearest neighbor
                    start = index
                    next_n = node[start]  

        #add node to cycle, update W and set new current node and it's status
        h_cycle.append(next_n)
 
        start_i = next_n
        state_of_nodes[start] = "D"

        W += min_distance

    #closing the cycle; calculate distance between starting and last point
    end_distance = distance(start_i, node[0])
    
    h_cycle.append(node[0])
    W += end_distance

    return h_cycle, W

def best_insertion(node : list):
    #declare imput data as a list
    print("Dělám na BI, klid.")
    #set all nodes as unprocessed, copy data, create a cycle and initialize it's weigh
    state_of_nodes = ["N"] * (len(node))
    copy_node = node.copy()
    h_cycle = []
    W = 0

    #choose random three starting nodes
    start = random.sample(range(len(node)),3)

    #add starting points to cycle and change their status
    for idx in start:
        h_cycle.append(node[idx])
        state_of_nodes[idx] = "D"

    #calculate distance of starting three points
    for k in range(3):
        start_distance = distance(node[k], node[k+1])
        W += start_distance
    
    #as long as any unprocessed nodes exist
    while "N" in state_of_nodes:

        #set minimum distance to infinity
        min_distance = inf

        #select random node
        random_idx= random.choice([idx for idx in range(len(node)) if state_of_nodes[idx] == "N"])
        random_node = node[random_idx]

        #iterate over nodes except starting node
        for index in range(len(h_cycle) - 2):

            #index for next node
            if index != len(h_cycle) - 1:
                index_2 = index + 1 
            else: index_2 = 0

            #calculate distance
            dist = distance(h_cycle[index], random_node) + distance(random_node, h_cycle[index_2]) - distance(h_cycle[index], h_cycle[index_2])
            
            #change minimum distance if the calculated distance is smaller than current min distance
            if dist < min_distance:
                min_distance = dist
                node_idx = index + 1
        
        #add node to cycle, remove node from copy_node list and calculate W
        h_cycle.insert(node_idx, random_node)
        copy_node.remove(random_node)
        W += min_distance

        #change status of current node
        state_of_nodes[random_idx] = "D"
    
    #close cycle; add starting point to the end of h_cycle
    h_cycle.append(h_cycle[0])

    return h_cycle, W

#visualization of results
def plot(results):

    #get coords from results
    x = []
    y = []
    for r in results:
        x.append(r[0])
        y.append(r[1])
    ax = plt.axes()
    ax.invert_xaxis()
    ax.invert_yaxis()
    ax.scatter(x, y)
    ax.plot(x, y)
    plt.show()

#get data from file
def load_data(input):
    try:
        with open(input) as inp:
            data = pd.read_csv(inp, sep=";")
            nodes = data[["coord_X", "coord_Y"]].values.tolist()
        return nodes
    except FileNotFoundError:
        print("Couldn't access the file, make sure the path is correct or exists.")
        quit()

#input data
input_file = "ČR_obce_10_tis.csv"
node = load_data(input_file)

#execute algorithms separately
h_cycle_nn, W_nn = nearest_neighbor(node)
print(f"Výsledek NN: W = ", W_nn)
plot(h_cycle_nn)

h_cycle_bi, W_bi = best_insertion(node)
print(f"Výsledek BI: W = ", W_bi)
plot(h_cycle_bi)