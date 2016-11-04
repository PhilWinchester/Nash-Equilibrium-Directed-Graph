#Networkx test File
#Phil Winchester and Dillon Kerr

from __future__ import division
import networkx as nx
from graphics import *
from GuiHandler import *

def testGraph():
    G = nx.DiGraph()

    G.add_edge('S1', 'A', weight = 4)
    G.add_edge('S1', 'T2', weight = 3)
    G.add_edge('S2', 'A', weight = 5)
    G.add_edge('S3', 'S2', weight = 2)
    G.add_edge('S2', 'B', weight = 1)
    G.add_edge('A', 'T1', weight = 2)
    G.add_edge('B', 'T1', weight = 2)
    G.add_edge('T1', 'T2', weight = 4)
    G.add_edge('B', 'C', weight = 3)
    G.add_edge('C', 'T3', weight = 6)

    G = createClassGraph()
    play1List, play1Weight = shortestPath(G, 'S1', 'T1', 'weight')
    play2List, play2Weight = shortestPath(G, 'S2', 'T2', 'weight')
    play3List, play3Weight = shortestPath(G, 'S3', 'T3', 'weight')

    print 'Path: ' + str(play1List) + ', Weight: ' + str(play1Weight)
    print 'Path: ' + str(play2List) + ', Weight: ' + str(play2Weight)
    print 'Path: ' + str(play3List) + ', Weight: ' + str(play3Weight)

    totWeight = play1Weight + play2Weight + play3Weight

    print "Overall weight (w/ overlap): " + str(totWeight)

   
def classGraph():
    
    G = buildClassGraph()

    p1List, p1Weight = shortestPath(G, 'S1', 'T1', 'weight')
    p2List, p2Weight = shortestPath(G, 'S2', 'T2', 'weight')
    p3List, p3Weight = shortestPath(G, 'S3', 'T3', 'weight')
    
    repeatedWgt = findRepeats(G, p1List, p2List) + findRepeats(G, p1List, p3List) + findRepeats(G, p2List, p3List)
    
    print 'Player 1: Path: ' + str(p1List) + ', Weight: ' + str(p1Weight)
    print 'Player 2: Path: ' + str(p2List) + ', Weight: ' + str(p2Weight)
    print 'Player 3: Path: ' + str(p3List) + ', Weight: ' + str(p3Weight)
  
    totWeightRepeat = p1Weight + p2Weight + p3Weight
    optWeight =  totWeightRepeat - repeatedWgt
    optPathList = (p1List, p2List, p3List)

    print "Overall weight (w/ overlap): " + str(totWeightRepeat)
    print "Optimal total weight (w/o overlap): " + str(optWeight)
    print "Optimal Paths: "
    print optPathList
    print ''
    
    paths = findNash(G)
    print paths
    
# Calculates the shortest path from a source node to a sink node
# Returns the path as a list of nodes and the total weight of the path
def shortestPath(G, s, t, wStr):

    pathList = nx.shortest_path(G, s, t, weight = wStr)
    pathWeight = nx.shortest_path_length(G, s, t, weight = wStr)
    
    return pathList, pathWeight

def findNash(G):
    i = 1
    sameCount = 0
    isSame = False
    temp1 = []
    temp2 = []
    temp3 = []
    weight1 = 0
    weight2 = 0
    weight3 = 0
    oldList = [temp1, temp2, temp3]
    tempG = G
    
    for edge in tempG.edges():
      tempG.get_edge_data(edge[0], edge[1])['numPlayers'] = 0

    while isSame == False:
      listG = []
      weight = 0
      
      if i == 1: #player1 plays
        listG, weight = shortestPath(tempG, 'S1', 'T1', 'weight')
        #print "p1List" + str(listG)
        
        if oldList[0] == listG:
          sameCount += 1
          
        i+=1
        oldList[0] = listG
        weight1 = weight
        
      elif i == 2: #player2 plays
        listG, weight = shortestPath(tempG, 'S2', 'T2', 'weight')
        #print "p2List" + str(listG)
        
        if oldList[1] == listG:
          sameCount += 1
          
        else:
          sameCount = 0
          
        i+=1
        oldList[1] = listG
        weight2 = weight
        
      elif i == 3: #player3 plays
        listG, weight = shortestPath(tempG, 'S3', 'T3', 'weight')
        #print "p3List" + str(listG)
        
        if oldList[2] == listG:
          sameCount += 1
          
        else:
          sameCount = 0
          
        i=1
        oldList[2] = listG
        weight3 = weight
      #print 'Same Count: ' + str(sameCount)
      
      currEdges = getEdges(listG)

      if sameCount == 3: #players have stagnated and while breaks
        return [(oldList[0], weight1), (oldList[1], weight2), (oldList[2], weight3)]
    
      else:
          
        if i == 2:
          oldEdges = getEdges(oldList[0])
          
        elif i == 3:
          oldEdges = getEdges(oldList[1])
          
        else:
          oldEdges = getEdges(oldList[2])
          
        
        print "TempEdges: " + str(oldEdges)
        print "Pre-Edges: " + str(currEdges)
        a = False
        
        for oEdge in oldEdges: #previous round edges
          print "Edge: " + str(oEdge)
          
          for cEdge in currEdges:  #current round edges
            print "Edge2: " + str(cEdge)
            
            if oEdge == cEdge:
              print "Breaking!!!!!!!!!!!!!"
              a = True
              pass
            
          if a == False:
            print "a = False"  
            tempG.get_edge_data(edge[0], edge[1])['numPlayers'] -= 1

          if oEdge not in oldEdges:
            print "NOT IN!!!!!!!!!!"
            tempG.get_edge_data(oEdge[0], oEdge[1])['numPlayers'] += 1
            a = tempG.get_edge_data(oEdge[0], oEdge[1])['weight']
            n = tempG.get_edge_data(oEdge[0], oEdge[1])['numPlayers']
            tempG.get_edge_data(oEdge[0], oEdge[1])['weight'] = (a / n)
          
          print "Num Players: " + str(tempG.get_edge_data(oEdge[0], oEdge[1])['numPlayers'])
          print tempG.get_edge_data(oEdge[0], oEdge[1])['weight']

    return
       
# Finds repeated edges between paths and adds weights to a variable
# Returns integers value of weights of repeated edges
def findRepeats(G, p1, p2):
    p1Edges = getEdges(p1)
    p2Edges = getEdges(p2)
    repeat = 0
    for edge1 in p1Edges:
      for edge2 in p2Edges:
        if(edge1 == edge2):
          a = G.get_edge_data(edge1[0], edge1[1])['weight']
          repeat += a 
    return repeat
      
# Returns a list of edges (tuples) in a path
def getEdges(p):
    edges = []
    for i in range(0, len(p)-1):
      edges.append((p[i] , p[i+1]))
    return edges

# Builds an example graph from class
def buildClassGraph():
    G = nx.DiGraph()

    G.add_edge('S1', 'T1', weight = 8)
    G.add_edge('S1', 'A', weight = 3)
    G.add_edge('S2', 'A', weight = 1)
    G.add_edge('S2', 'T3', weight = 5)
    G.add_edge('A', 'B', weight = 4)
    G.add_edge('B', 'T1', weight = 1)
    G.add_edge('T1', 'T2', weight = 5)
    G.add_edge('T2', 'T3', weight = 1)
    G.add_edge('B', 'T2', weight = 2)
    G.add_edge('B', 'T3', weight = 2)
    G.add_edge('S3', 'S2', weight = 2)
    G.add_edge('S3', 'T3', weight = 5)

    return G

# Main Method
def main():
    #print "Test Graph Example: "
    #testGraph()
    
    #print " "
    
    #print "Graph from Class Example: \n"
    #classGraph()

    G = nx.DiGraph()

##    G.add_edge('S1', 'T1', weight = 8)
##    G.add_edge('S1', 'A', weight = 3)
##    G.add_edge('S2', 'A', weight = 1)
##    G.add_edge('S2', 'T3', weight = 5)
##    G.add_edge('A', 'B', weight = 4)
##    G.add_edge('B', 'T1', weight = 1)
##    G.add_edge('T1', 'T2', weight = 5)
##    G.add_edge('T2', 'T3', weight = 1)
##    G.add_edge('B', 'T2', weight = 2)
##    G.add_edge('B', 'T3', weight = 2)
##    G.add_edge('S3', 'S2', weight = 2)
##    G.add_edge('S3', 'T3', weight = 5)
##
##    print "Player 1 All Paths: "
##    shortG1 = nx.all_simple_paths(G, 'S1', 'T1')
##    for i in shortG1:
##        print i
##    print "Player 1 Shortest Path: " + str(nx.shortest_path(G, 'S1', 'T1', weight = 'weight')) + '\n'
##
##    print "Player 2: "
##    shortG2 = nx.all_simple_paths(G, 'S2', 'T2')
##    for i in shortG2:
##        print i
##    print "Player 2 Shortest Path: " + str(nx.shortest_path(G, 'S2', 'T2', weight = 'weight')) + '\n'
##                                           
##    print "Player 3: "
##    shortG3 = nx.all_simple_paths(G, 'S3', 'T3')
##    for i in shortG3:
##        print i
##    print "Player 3 Shortest Path: " + str(nx.shortest_path(G, 'S3', 'T3', weight = 'weight')) + '\n'

        
    win = GraphWin('Graph', 700,700)
    win.setBackground('black')
    win.setCoords(0,0,50,50)

    title = Text(Point(7,48), "Example of Directed Graph")
    title.setSize(14)
    title.setTextColor('white')
    title.draw(win)

    entryButton = Button(win,7,3,5,10,'blue','white','Enter Weights!')
    entryButton.draw()
    
    G = nx.DiGraph()
    
    dG = Graph(G, win)

    dG.createNodes()
    dG.createEdges()
    
    pt = win.getMouse()

    if entryButton.clicked(pt):
        dG.inputEdges()
    else:
        win.getMouse()
    
    win.close()
    

main()
