# -*- coding: utf-8 -*-
#Lefa Raleting
#14222460
#Reference 
#Imports
import random
#import queue
import time


#Creating a node
#This node takes on a character object and array of nodes as arguments
class node(object):
    def __init__(self,object,children= [],path=""): #Creating a node with an emtpy array of children
        self.object=object #Object to store the move "R" "P" or "S"
        self.children=children #each node can have no children or all three
        self.path=path #This is to keep the path upto that point
        
    def haschildren(self): #this function determines if the current node has children
       return len(self.children)!=0 #if the length of the children array is >0 then it has children
   
    def isleaf(self): #this is to check if the current node is a leaf node
       return len(self.children)==0#if the current node has no children , then its a leaf node
    
    def item(self,):
        return self.object #this return the move of the current node
        
"""Task1: Create a BST that take a depth as and argument,
The tree must be recursively built
 """       

class tree(object): 
    def __init__(self): #initialization of the tree
        self.root=node("Start") #tree starts of with a abituary root node "Start"
       
        
    def haschildren(self,currentnode):#this is to determine if the passed node in the argument
       return currentnode.haschildren()# has any children if so return true else return false
   
    
    def insert1(self,currentnode): 
            
        index=0
        while index!=3 :
            if index==0:
                currentnode.children.append(node("R",[]))
            if index == 1:
                currentnode.children.append(node("P",[]))
            if index== 2:
                currentnode.children.append(node("S",[]))
            index +=1
        
    def _insert(self,currentnode):#This funtion  recursively transverses to leaf node to add 
        #To add currentnode to the lead node as a child node
        if currentnode.haschildren():#current node has children
            i=0 #transverse all the children
            while i!=3:#while it i is not equal to three the children have not all been tranvesed 
                self._insert(currentnode.children[i])#recursively call insert function
                #print id(currentnode.children[i])
               # print i
                i+=1
        else: #you have reached leaf node
           self.insert1(currentnode) #insert node onto leaf
          
           
#______________________________________________________________________        
#Task1

def buildtree(depth): #this function then uses the above functions to recursively 
    tree1=tree() #build a tree dynamically 
    i=0
    while i<depth:# a Tree of the specified depth
        tree1._insert(tree1.root); #This call insert of class tree
        i+=1 #continue incrementing until you reach the specified depth
    return tree1 #return the tree






    
 #______________________________________________________________________       
 
    
#task2
"""Design a bfs and dfs alrogithm that will be used to transverse
and return the sequence of nodes it visits in the tree
Basically you must just keep track of of the nodes visited for each node.

I'm going to need a variable for visted and sequence(dynamic path) at least.

"""

def BFS(depth,paths="x"): #This BFS algorithm takes in a depth
    
    tree= buildtree(depth)  #create a tree of specified depth
    visited=[] #list to keep track of the visited nodes as they are being transversed
    visited_val=[]# list to keep track of the sequence visited
    temp=tree.root #create a strating position of the tree inorder to transversed 
    queue=[temp] #start at root using a queue which uses FIFO structure
    
    #Transverssal
    while  len(queue)!=0: #while que is not empty 
        node=queue.pop(0) # enque the first element
        #print id(node)
        
        if node in visited: #if  the node is already in the visted list then 
            #break the while loop
            break
        else: #else the node hasent been explored
            visited.append(node)# add to visited node list
            
            # Add node to path
           # visited_val.append(path +node.object )
            #print id(node)
            if node.object == "Start": #if its root node add nothing to path
                    node.path+=""
            else:
                    node.path+=node.object #else add the current object to path
                    visited_val.append(node.path ) 
            if node.haschildren(): #add children to queue
                
                    
                i=0
                if(node.path==paths):
                       # print "found: " + paths
                        #print (visited_val)
                        return visited_val
                
                while i!=3: 
                    #print node.children[i].object
                    
                    node.children[i].path=node.path
                    
                    #visited_val.append(node.path +node.children[i].object ) 
                   # visited_val.append([visited_val])
                    #print id(node.children[i])
                    queue.append(node.children[i])
                    i+=1
    return visited_val
    #print visited_val 
            

def DFS(depth): #this is a dfs algorithm 
    tree=buildtree(depth) #create a tree ofa specific depth 
    visited=[] #this list is to keep track of specified 
    visited_val=[] #this keeps track of the value of the visted nodes
    temp=tree.root# create a abitury node to transverse
    stack=[temp] # this algorithm uses a Stack which is LIFO structure 
    
    while len(stack)!=0: #While stack is not empty 
        
        node=stack.pop() #pop out the last node 
        
        if node in visited:#if the current node has been visted
            break #break sequence
        else: #elese explore
            #Add node to visted nodes
            visited.append(node)
            #path=visited.reverse()
            if node.object == "Start": #if its root node add nothing to path
                    node.path+=""
            else: #else add current move to path
                    node.path+=node.object
                    visited_val.append(node.path)
            if node.haschildren(): #explore the children
                i=0
                while i!=3:
                    #add to stack 
                    stack.append(node.children[i]) #add children to unvisted stack
                    if node.object !="Start":
                        node.children[i].path=node.path
                    i+=1
    visited_val.reverse()
            
    return visited_val
    
    
#DFS(2)

#Task 3
    
#This code must run a the codes until repetion is found
#When this happens you must note the sequence
#use this sequence to trigger the repetion and win the game
#Rinput("enter")
#PC=input()


def win(prev): #this algorithm is used once a repeat has been found
     if prev=="R":
            return "P"
     elif prev=="P":
        return "S"
     elif prev=="S":
            return "R"
def selectgame(bfs_dfs,d):
    if(bfs_dfs==0):
        return BFS(d)
    else: 
        return DFS(d)

#print selectgame(1,5)[4][0]
#variables


prev=input
if prev=="":
    bfs_dfs=1#random.randint(0,1) #randomly select between 0 =bfs or 1 =dfs or you can hard code the game choice
    play="R" #always start with rock
    sequence=[] #empty sequence
    node_= 3 
    index=0
    repeat = ""
    winner=0 #0 means we havent found winning sequence
    d=5 #intially starts at depth of 5 and increases as the moves unfold
    var=selectgame(bfs_dfs,d) #This returns either the bfs transversed nodes or DFS
    a=0
else:
    
   
    #game starts
    if repeat=="": 
        #tranverse through the tree starting at i
        
        play= var[node_][index] #play the next move at the position index 
        repeat=prev#let the repeat checker equal to to the prev move
        index+=1   #increment position    
    elif repeat==prev:
        winner=1 #So that it can stop transversing
        a=0
        sequence=(var[node_]) #stores the sequence  that caused the break  anything between 2-5 moves
        j=0
        #print (sequence)
        play=win(prev)
        
        
        falsesequence=0
        #counter=0
    else: 
        #not repeated but sequence hasnt been found
        
        if winner==0: #TRANSVERSING THROUGH LIST
            if index<len(var[node_]):
             
                play= (var[node_][index])
                index+=1
                
            else:
               
                node_+=1              
                index=0 #stat again to the intial index before going out of bound
                play=var[node_][index]
                #counter+1
                index+=1
                
        else:# break sequence has been found
            
            #Check if it was a false sequence
            if falsesequence==1:
                winner=0 #if its a false sequence set flag to zero
            if index< len(sequence): #if the length of the sequence is less than
                #the length of the node then it was a false signal
                #continue transversing
                
                play = var[node_][index] #generate the next move in the list
                index += 1
                #sequence=[]
                if index== len(var[node_]): #if after increment and index = len of the var path node
                    falsesequence=1 #then its a false sequence
                    repeat="x" #clear the repetition placeholder so that it doesnt trigger the win cycle function
                    
                  
                    
            else: #This is the correct sequence
                if (j< len(sequence)): #so transvers through the whole breakable sequence, whether its 2 or 5
                    play=sequence[j] #only stop at the end of the len of the sequence
                    j+=1
    repeat=prev   #this stores the previously played move
# Play the selected object.
output= play     

#__________________________output_____________________________________________


"""Pool 1: 1 bots loaded
Pool 2: 1 bots loaded
Playing 10 matches per pairing.
Running matches in 8 threads
10 matches run
total run time: 0.42 seconds

breakable.py: won 0.0% of matches (0 of 10)
    won 25.3% of rounds (2533 of 10000)
    avg score -241.4, net score -2414.0

eai320_prac_1_14222460.py: won 100.0% of matches (10 of 10)
    won 49.5% of rounds (4947 of 10000)
    avg score 241.4, net score 2414.0
    
"""

    