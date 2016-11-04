#Networkx test File
#Phil Winchester and Dillon Kerr

from __future__ import division
import networkx as nx
from graphics import *
from GuiHandler import *
   
def classGraph(G, graphInst):
    
    #G = buildClassGraph()
      
    p1List, p1Weight = shortestPath(G, 'S1', 'T1', 'weight') #original weights not adjusted
    p2List, p2Weight = shortestPath(G, 'S2', 'T2', 'weight')
    p3List, p3Weight = shortestPath(G, 'S3', 'T3', 'weight')
    
    repeatedWgt = findRepeats(G, p1List, p2List) + findRepeats(G, p1List, p3List) + findRepeats(G, p2List, p3List)
    
    print "Repeated: " + str(repeatedWgt)
    
    print 'Player 1: Path: ' + str(p1List)
    print 'Player 2: Path: ' + str(p2List)
    print 'Player 3: Path: ' + str(p3List)
  
    totWeightRepeat = p1Weight + p2Weight + p3Weight
    optWeight =  totWeightRepeat - repeatedWgt
    optPathList = (p1List, p2List, p3List)

    print "Overall weight (w/ overlap): " + str(totWeightRepeat)
    print "Optimal total weight (w/o overlap): " + str(optWeight)
    print "Optimal Paths: "
    print optPathList
    print ''
    
    paths = findNash(G, graphInst)

    graphInst.drawInfo(paths, optWeight)
    graphInst.redrawPathEdges()

    return G
    
# Calculates the shortest path from a source node to a sink node
# Returns the path as a list of nodes and the total weight of the path
def shortestPath(G, s, t, wStr):

    pathList = nx.shortest_path(G, s, t, weight = wStr)
    pathWeight = nx.shortest_path_length(G, s, t, weight = wStr)
    
    return pathList, pathWeight

# Determines the min weight path in list of all possible paths
def findMinWeightPath(G, pathList):
  min = 1000
  p = []
  for path in pathList:
    wgt = getPathWeight(G, path)
    if wgt < min:
      min = wgt
      p = path
  
  return p

# Gets the path weight given a specified path
def getPathWeight(G, path):
    edges = getEdges(path)
    sum = 0
    for edge in edges:
      sum += G.get_edge_data(edge[0], edge[1])['weight']
    return sum

# Finds the Nash equilibrium in a graph G with 3 selfish players   
def findNash(G, graphInst):
    i = 1
    sameCount = 0
    isSame = False
    temp1 = []
    temp2 = []
    temp3 = []
    weight1 = 0
    weight2 = 0
    weight3 = 0
    tempList = [temp1, temp2, temp3]
    curPlayer = 0

##    print graphInst.pathEdgeList
##    if graphInst.pathEdgeList > 1:
##        for q in graphInst.pathEdgeList:
##            q.undraw()
    
    # Initialize numPlayers and trueWeight on each edge in G
    for edge in G.edges():
      G.get_edge_data(edge[0], edge[1])['numPlayers'] = []
      G.get_edge_data(edge[0], edge[1])['trueWeight'] = G.get_edge_data(edge[0], edge[1])['weight']
    
    # Perform loop until each player repeats his her path (i.e. does not want to deviate)
    while isSame == False:
      tempG = G.copy()
      listG = []
      weight = 0
      
      # player 1 iteration
      if i == 1:
        curPlayer = 1
        tempG = hypEdges(G, listG, curPlayer)
        listG, weight = shortestPath(tempG, 'S1', 'T1', 'weight')
        print "p1List " + str(listG)
        graphInst.travelEdge(listG, i)
        
        # check if path is same as previous iteration
        if tempList[0] == listG:
          sameCount += 1
        else:
          sameCount = 0
        i+=1
        weight1 = weight
 
      # player 2 iteration
      elif i == 2:
        curPlayer = 2
        tempG = hypEdges(G, listG, curPlayer)
        listG, weight = shortestPath(tempG, 'S2', 'T2', 'weight')
        print "p2List " + str(listG)
        graphInst.travelEdge(listG, i)
        
        # check if path is same as previous iteration
        if tempList[1] == listG:
          sameCount += 1
        else:
          sameCount = 0 
        i+=1
        weight2 = weight
        
      # player 3 iteration
      elif i == 3:
        curPlayer = 3
        tempG = hypEdges(G, listG, curPlayer)
        listG, weight = shortestPath(tempG, 'S3', 'T3', 'weight')
        print "p3List " + str(listG)
        graphInst.travelEdge(listG, i)
        
        # check if path is same as previous iteration
        if tempList[2] == listG:
          sameCount += 1
        else:
          sameCount = 0
        i=1
        weight3 = weight

      # if every player has same path as previous rounds,
      # return a list containing each players path and their weights
      if sameCount == 3:
        return [(tempList[0], weight1), (tempList[1], weight2), (tempList[2], weight3)]
    
      else:
        
        # get a list of edges in the new path
        edges = getEdges(listG)

        # get list of edges from previous path depending on current player
        if i == 2:
          oldEdges = getEdges(tempList[0])
        elif i == 3:
          oldEdges = getEdges(tempList[1])
        else:
          oldEdges = getEdges(tempList[2])
        
        # if player does not include old edge in new path,
        # decrement numPlayers on that edge  
        for oldEdge in oldEdges:
          if oldEdge not in edges:
            otherList = playerList = G.get_edge_data(edge[0], edge[1])['numPlayers']
            if curPlayer in otherList:
              G.get_edge_data(edge[0], edge[1])['numPlayers'].remove(curPlayer)
        
        # if player includes new edge that is not in old path,
        # increment numPlayers on that edge
        for edge in edges:
          if edge not in oldEdges:
            playerList = G.get_edge_data(edge[0], edge[1])['numPlayers']
            if curPlayer not in playerList:
              G.get_edge_data(edge[0], edge[1])['numPlayers'].append(curPlayer)
        
        # update the weights of each edges based on the number of players on the edge
        for edge in G.edges():
          trueWgt = G.get_edge_data(edge[0], edge[1])['trueWeight']
          n = len(G.get_edge_data(edge[0], edge[1])['numPlayers'])
          if n != 0:
            G.get_edge_data(edge[0], edge[1])['weight'] = (trueWgt / n)
          else:
            G.get_edge_data(edge[0], edge[1])['weight'] = trueWgt
          #print "Edge: " + str(edge)
          #print "Num Players:"
          #print G.get_edge_data(edge[0], edge[1])['numPlayers']
          #print "Weight:"
          #print G.get_edge_data(edge[0], edge[1])['weight']
      
      # set the previous path to current path for next iteration
      if i == 2:
        tempList[0] = listG
      elif i == 3:
        tempList[1] = listG
      else:
        tempList[2] = listG  
    sleep(1)
    return

# Creates a copy of the original graph with hypothetical edge
# weights for current player
# Allows player to look in advance to see if changing path will result in lower cost
def hypEdges(bG, path, curPlayer):
    aG = bG.copy()
    edgeList = aG.edges()
    pathEdges = getEdges(path)
    for edge in edgeList:
      if edge not in pathEdges:
        playerList = aG.get_edge_data(edge[0], edge[1])['numPlayers']
        if curPlayer not in playerList:
          aG.get_edge_data(edge[0], edge[1])['numPlayers'].append(curPlayer)
        trueWgt = aG.get_edge_data(edge[0], edge[1])['trueWeight']
        n = len(aG.get_edge_data(edge[0], edge[1])['numPlayers'])
        if n!=0:
          aG.get_edge_data(edge[0], edge[1])['weight'] = (trueWgt / n)
      #print "HypEdge: " + str(edge)
      #print "Hyp NumPlayers:"
      #print G.get_edge_data(edge[0], edge[1])['numPlayers']
    return aG
      
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

# Main Method
def main():

    hasInput = False
    
    #print "Graph from Class Example: \n"
    #G = classGraph()

    win = GraphWin('Graph', 800,800)
    win.setBackground('black')
    win.setCoords(0,0,50,50)

    title = Text(Point(7,46), "Example of a Directed Graph")
    title.setSize(14)
    title.setTextColor('white')
    title.draw(win)

    reloadButton = Button(win,4,48,3,7,'grey11','grey28','Reload Graph')
    reloadButton.draw()

    entryButton = Button(win,4,3,5,7,'blue','white','Enter Weights!')
    entryButton.draw()

    quitButton = Button(win,47,3,5,5,'red','white','Quit')
    quitButton.draw()

    runAlgButton = Button(win,12,3,5,7,'green4','white','Find Paths!')
    runAlgButton.draw()
    
    dG = Graph(win)

    dG.createNodes()
    dG.createEdges()
    
    pt = win.getMouse()
    
    while not quitButton.clicked(pt):

        if entryButton.clicked(pt):
            edgeList = dG.inputEdges()
            newG = nx.DiGraph()
            
##            for i in edgeList:
##                print i.getText()
                
            newG.add_edge('S1', 'A', weight = int(edgeList[0].getText()))
            newG.add_edge('S2', 'A', weight = int(edgeList[1].getText()))
            newG.add_edge('S3', 'S2', weight = int(edgeList[2].getText()))
            newG.add_edge('S1', 'T1', weight = int(edgeList[3].getText()))
            newG.add_edge('A', 'B', weight = int(edgeList[4].getText()))
            newG.add_edge('S2', 'T3', weight = int(edgeList[5].getText()))
            newG.add_edge('S3', 'T3', weight = int(edgeList[6].getText()))
            newG.add_edge('B', 'T1', weight = int(edgeList[7].getText()))
            newG.add_edge('B', 'T3', weight = int(edgeList[8].getText()))
            newG.add_edge('T1', 'T2', weight = int(edgeList[9].getText()))
            newG.add_edge('B', 'T2', weight = int(edgeList[10].getText()))
            newG.add_edge('T2', 'T3', weight = int(edgeList[11].getText()))
                
            hasInput = True
            
        if runAlgButton.clicked(pt):

            if len(dG.pathEdgeList) > 1:
                for i in dG.pathEdgeList:
                    i.setWidth(1)
                    i.undraw()
                for j in dG.playerInfoList:
                    j.setSize(12)
                    j.undraw()
            
            if hasInput == True:
                classGraph(newG, dG)
                
                
            else:
                G = nx.DiGraph() #duplicate instead of list of players
 
                G.add_edge('S1', 'A', weight = 3)  #1
                G.add_edge('S2', 'A', weight = 1)  #2
                G.add_edge('S3', 'S2', weight = 2) #3
                G.add_edge('S1', 'T1', weight = 8) #4
                G.add_edge('A', 'B', weight = 4)   #5
                G.add_edge('S2', 'T3', weight = 5) #6
                G.add_edge('S3', 'T3', weight = 5) #7
                G.add_edge('B', 'T1', weight = 1)  #8
                G.add_edge('B', 'T3', weight = 2)  #9
                G.add_edge('T1', 'T2', weight = 5) #10
                G.add_edge('B', 'T2', weight = 2)  #11
                G.add_edge('T2', 'T3', weight = 1) #12
                
                classGraph(G, dG)

        if reloadButton.clicked(pt):

            win.close()

            main()
            
        pt = win.getMouse()

        
    win.close()
    
main()



'''
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

    # Builds an example graph from class
def buildClassGraph():
    G = nx.DiGraph()
 
    G.add_edge('S1', 'A', weight = 3)  #1
    G.add_edge('S2', 'A', weight = 1)  #2
    G.add_edge('S3', 'S2', weight = 2) #3
    G.add_edge('S1', 'T1', weight = 9) #4
    G.add_edge('A', 'B', weight = 4)   #5
    G.add_edge('S2', 'T3', weight = 5) #6
    G.add_edge('S3', 'T3', weight = 5) #7
    G.add_edge('B', 'T1', weight = 1)  #8
    G.add_edge('B', 'T3', weight = 2)  #9
    G.add_edge('T1', 'T2', weight = 5) #10
    G.add_edge('B', 'T2', weight = 2)  #11
    G.add_edge('T2', 'T3', weight = 1) #12 
    

    return G
'''
