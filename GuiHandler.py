#GUI File
#Phil Winchester and Dillon Kerr

import networkx as nx
from graphics import *
from random import *
from time import *
from buttonClass import *

class Graph:

    def __init__(self, gWin):

        #self.G = diGraph
        self.win = gWin
        self.edgeList = []
        self.nodeList = []
        self.edgeLabelList = []
        self.pathEdgeList = []
        self.playerInfoList = []
        self.allPlayerPathList = []

#draws the nodes within a random region 
    def createNodes(self):

        for i in range(4):
            x = randrange(2, 7) + (i * 12)
            y = randrange(35, 40)
            
            newNode = Circle(Point(x, y), 1)
            newNode.setOutline('red')
            newNode.setFill('red4')
            newNode.draw(self.win)
            self.nodeList.append(newNode)

        for i in range(3):
            x = randrange(2, 7) + (i * 15)
            y = randrange(22, 28)

            newNode = Circle(Point(x, y), 1)
            newNode.setOutline('red')
            newNode.setFill('red4')
            newNode.draw(self.win)
            self.nodeList.append(newNode)

        x = randrange(20, 30)
        y = randrange(13, 18)
        
        newNode = Circle(Point(x, y), 1)
        newNode.setOutline('red')
        newNode.setFill('red4')
        newNode.draw(self.win)
        self.nodeList.append(newNode)

#draws all edges b/w nodes in the graph
    def createEdges(self):

        s1 = self.nodeList[0].getCenter()
        a  = self.nodeList[1].getCenter()
        s2 = self.nodeList[2].getCenter()
        s3 = self.nodeList[3].getCenter()
        t1 = self.nodeList[4].getCenter()
        b  = self.nodeList[5].getCenter()
        t3 = self.nodeList[6].getCenter()
        t2 = self.nodeList[7].getCenter()

        #Draw labels on all the nodes
        s1Label = Text(Point(s1.x, s1.y + 2), 'S1')
        s1Label.setTextColor('gold1')
        s1Label.setSize(17)
        s1Label.draw(self.win)

        aLabel = Text(Point(a.x, a.y + 2), 'A')
        aLabel.setTextColor('gold1')
        aLabel.setSize(17)
        aLabel.draw(self.win)

        s2Label = Text(Point(s2.x, s2.y + 2), 'S2')
        s2Label.setTextColor('gold1')
        s2Label.setSize(17)
        s2Label.draw(self.win)

        s3Label = Text(Point(s3.x, s3.y + 2), 'S3')
        s3Label.setTextColor('gold1')
        s3Label.setSize(17)
        s3Label.draw(self.win)

        t1Label = Text(Point(t1.x, t1.y + 2), 'T1')
        t1Label.setTextColor('gold1')
        t1Label.setSize(17)
        t1Label.draw(self.win)

        bLabel = Text(Point(b.x, b.y + 2), 'B')
        bLabel.setTextColor('gold1')
        bLabel.setSize(17)
        bLabel.draw(self.win)

        t3Label = Text(Point(t3.x, t3.y + 2), 'T3')
        t3Label.setTextColor('gold1')
        t3Label.setSize(17)
        t3Label.draw(self.win)

        t2Label = Text(Point(t2.x, t2.y + 2), 'T2')
        t2Label.setTextColor('gold1')
        t2Label.setSize(17)
        t2Label.draw(self.win)

        #1) Draw Line b/w s1 and a nodes and add weight label
        s1a = Line(Point(s1.x,s1.y),Point(a.x,a.y))
        s1a.setFill('dark green')
        s1a.setArrow('last')
        s1a.setWidth(3)
        s1a.draw(self.win)
        self.edgeList.append(s1a)

        s1aAvgX = (s1.x + a.x) / 2
        s1aAvgY = (s1.y + a.y) / 2
        
        s1aWeight = Text(Point(s1aAvgX, s1aAvgY - 1), '3')
        s1aWeight.setSize(17)
        s1aWeight.setTextColor('dark green')
        s1aWeight.draw(self.win)
        self.edgeLabelList.append(s1aWeight)

        #2) Draw Line b/w a and s2 nodes and add weight label
        as2 = Line(Point(a.x,a.y), Point(s2.x,s2.y))
        as2.setFill('dark green')
        as2.setArrow('first')
        as2.setWidth(3)
        as2.draw(self.win)
        self.edgeList.append(as2)

        as2AvgX = (a.x + s2.x) / 2
        as2AvgY = (a.y + s2.y) / 2

        as2Weight = Text(Point(as2AvgX, as2AvgY - 1), '1')
        as2Weight.setSize(17)
        as2Weight.setTextColor('dark green')
        as2Weight.draw(self.win)
        self.edgeLabelList.append(as2Weight)

        #3) Draw Line b/w s2 and s3 nodes and add weight label
        s2s3 = Line(Point(s2.x,s2.y), Point(s3.x,s3.y))
        s2s3.setFill('dark green')
        s2s3.setArrow('first')
        s2s3.setWidth(3)
        s2s3.draw(self.win)
        self.edgeList.append(s2s3)

        s2s3AvgX = (s2.x + s3.x) / 2
        s2s3AvgY = (s2.y + s3.y) / 2

        s2s3Weight = Text(Point(s2s3AvgX, s2s3AvgY - 1), '2')
        s2s3Weight.setSize(17)
        s2s3Weight.setTextColor('dark green')
        s2s3Weight.draw(self.win)
        self.edgeLabelList.append(s2s3Weight)

        #4) Draw Line b/w s1 and t1 nodes and add weight label
        s1t1 = Line(Point(s1.x,s1.y), Point(t1.x,t1.y))
        s1t1.setFill('dark green')
        s1t1.setArrow('last')
        s1t1.setWidth(3)
        s1t1.draw(self.win)
        self.edgeList.append(s1t1)

        s1t1AvgX = (s1.x + t1.x) / 2
        s1t1AvgY = (s1.y + t1.y) / 2

        s1t1Weight = Text(Point(s1t1AvgX + 1, s1t1AvgY), '8')
        s1t1Weight.setSize(17)
        s1t1Weight.setTextColor('dark green')
        s1t1Weight.draw(self.win)
        self.edgeLabelList.append(s1t1Weight)

        #5) Draw Line b/w a and b nodes and add weight label
        ab = Line(Point(a.x,a.y), Point(b.x,b.y))
        ab.setFill('dark green')
        ab.setArrow('last')
        ab.setWidth(3)
        ab.draw(self.win)
        self.edgeList.append(ab)

        abAvgX = (a.x + b.x) / 2
        abAvgY = (a.y + b.y) / 2

        abWeight = Text(Point(abAvgX + 1, abAvgY), '4')
        abWeight.setSize(17)
        abWeight.setTextColor('dark green')
        abWeight.draw(self.win)
        self.edgeLabelList.append(abWeight)

        #6) Draw Line b/w s2 and t3 nodes and add weight label
        s2t3 = Line(Point(s2.x,s2.y), Point(t3.x,t3.y))
        s2t3.setFill('dark green')
        s2t3.setArrow('last')
        s2t3.setWidth(3)
        s2t3.draw(self.win)
        self.edgeList.append(s2t3)

        s2t3AvgX = (s2.x + t3.x) / 2
        s2t3AvgY = (s2.y + t3.y) / 2

        s2t3Weight = Text(Point(s2t3AvgX - 1, s2t3AvgY), '5')
        s2t3Weight.setSize(17)
        s2t3Weight.setTextColor('dark green')
        s2t3Weight.draw(self.win)
        self.edgeLabelList.append(s2t3Weight)

        #7) Draw Line b/w s3 and t3 nodes and add weight label
        s3t3 = Line(Point(s3.x,s3.y), Point(t3.x,t3.y))
        s3t3.setFill('dark green')
        s3t3.setArrow('last')
        s3t3.setWidth(3)
        s3t3.draw(self.win)
        self.edgeList.append(s3t3)

        s3t3AvgX = (s3.x + t3.x) / 2
        s3t3AvgY = (s3.y + t3.y) / 2

        s3t3Weight = Text(Point(s3t3AvgX + 1, s3t3AvgY), '5')
        s3t3Weight.setSize(17)
        s3t3Weight.setTextColor('dark green')
        s3t3Weight.draw(self.win)
        self.edgeLabelList.append(s3t3Weight)

        #8) Draw Line b/w t1 and b nodes and add weight label
        t1b = Line(Point(t1.x,t1.y), Point(b.x,b.y))
        t1b.setFill('dark green')
        t1b.setArrow('first')
        t1b.setWidth(3)
        t1b.draw(self.win)
        self.edgeList.append(t1b)

        t1bAvgX = (t1.x + b.x) / 2
        t1bAvgY = (t1.y + b.y) / 2

        t1bWeight = Text(Point(t1bAvgX, t1bAvgY - 1), '1')
        t1bWeight.setSize(17)
        t1bWeight.setTextColor('dark green')
        t1bWeight.draw(self.win)
        self.edgeLabelList.append(t1bWeight)

        #9) Draw Line b/w b and t3 nodes and add weight label
        bt3 = Line(Point(b.x,b.y), Point(t3.x,t3.y))
        bt3.setFill('dark green')
        bt3.setArrow('last')
        bt3.setWidth(3)
        bt3.draw(self.win)
        self.edgeList.append(bt3)

        bt3AvgX = (b.x + t3.x) / 2
        bt3AvgY = (b.y + t3.y) / 2

        bt3Weight = Text(Point(bt3AvgX, bt3AvgY - 1), '2')
        bt3Weight.setSize(17)
        bt3Weight.setTextColor('dark green')
        bt3Weight.draw(self.win)
        self.edgeLabelList.append(bt3Weight)

        #10) Draw Line b/w t1 and t2 nodes and add weight label
        t1t2 = Line(Point(t1.x,t1.y), Point(t2.x,t2.y))
        t1t2.setFill('dark green')
        t1t2.setArrow('last')
        t1t2.setWidth(3)
        t1t2.draw(self.win)
        self.edgeList.append(t1t2)

        t1t2AvgX = (t1.x + t2.x) / 2
        t1t2AvgY = (t1.y + t2.y) / 2

        t1t2Weight = Text(Point(t1t2AvgX - 1, t1t2AvgY - 1), '2')
        t1t2Weight.setSize(17)
        t1t2Weight.setTextColor('dark green')
        t1t2Weight.draw(self.win)
        self.edgeLabelList.append(t1t2Weight)

        #11) Draw Line b/w b and t2 nodes and add weight label
        bt2 = Line(Point(b.x,b.y), Point(t2.x,t2.y))
        bt2.setFill('dark green')
        bt2.setArrow('last')
        bt2.setWidth(3)
        bt2.draw(self.win)
        self.edgeList.append(bt2)

        bt2AvgX = (b.x + t2.x) / 2
        bt2AvgY = (b.y + t2.y) / 2

        bt2Weight = Text(Point(bt2AvgX - 1, bt2AvgY - 1), '2')
        bt2Weight.setSize(17)
        bt2Weight.setTextColor('dark green')
        bt2Weight.draw(self.win)
        self.edgeLabelList.append(bt2Weight)

        #12) Draw Line b/w t2 and t3 nodes and add weight label
        t2t3 = Line(Point(t2.x,t2.y), Point(t3.x,t3.y))
        t2t3.setFill('dark green')
        t2t3.setArrow('last')
        t2t3.setWidth(3)
        t2t3.draw(self.win)
        self.edgeList.append(t2t3)

        t2t3AvgX = (t2.x + t3.x) / 2
        t2t3AvgY = (t2.y + t3.y) / 2

        t2t3Weight = Text(Point(t2t3AvgX - 1, t2t3AvgY - 1), '2')
        t2t3Weight.setSize(17)
        t2t3Weight.setTextColor('dark green')
        t2t3Weight.draw(self.win)
        self.edgeLabelList.append(t2t3Weight)


#Allows the user to input a custom weight for each edge in the graph
#loops linearly through the list of edges
    def inputEdges(self):
        numE = 0
        eWeight = 0

        for i in self.edgeLabelList:
            eWeight = int(i.getText())
            i.setText(" ")
            inLabel = Entry(Point(i.getAnchor().x, i.getAnchor().y), 10)
            inLabel.setText(eWeight)
            print(eWeight)
            inLabel.draw(self.win)
            self.win.getMouse()
            
            if inLabel.getText() == '':
                edgeText = 1
            else:
                edgeText = inLabel.getText()
                
            i.setText(edgeText)
            inLabel.undraw()
            numE += 1

        return self.edgeLabelList

#draws each players path through G
    def travelEdge(self, p, player):                    
                
        nodeValList = []

        for i in p: #converts the inputed path to specific node, so path draw correctly
            if i == "S1":
                nodeValList.append(0)
            elif i == "A":
                nodeValList.append(1)
            elif i == "S2":
                nodeValList.append(2)
            elif i == "S3":
                nodeValList.append(3)
            elif i == "T1":
                nodeValList.append(4)
            elif i == "B":
                nodeValList.append(5)
            elif i == "T3":
                nodeValList.append(6)
            elif i == "T2":
                nodeValList.append(7)
            else:
                print "~~don't exist~~"

        for n in range(len(nodeValList)):

            if n < (len(nodeValList) - 1): #customizes offset for each player
                if player == 1:
                    n1X = self.nodeList[nodeValList[n]].getCenter().x - 1
                    n1Y = self.nodeList[nodeValList[n]].getCenter().y + 1 
                    n2X = self.nodeList[nodeValList[n+1]].getCenter().x - 1
                    n2Y = self.nodeList[nodeValList[n+1]].getCenter().y + 1
                elif player == 2:
                    n1X = self.nodeList[nodeValList[n]].getCenter().x + 1
                    n1Y = self.nodeList[nodeValList[n]].getCenter().y + 1 
                    n2X = self.nodeList[nodeValList[n+1]].getCenter().x + 1
                    n2Y = self.nodeList[nodeValList[n+1]].getCenter().y + 1
                elif player == 3:
                    n1X = self.nodeList[nodeValList[n]].getCenter().x + 1
                    n1Y = self.nodeList[nodeValList[n]].getCenter().y
                    n2X = self.nodeList[nodeValList[n+1]].getCenter().x + 1
                    n2Y = self.nodeList[nodeValList[n+1]].getCenter().y
                
                travEdge = Line(Point(n1X,n1Y), Point(n2X,n2Y))
                if player == 1:
                    travEdge.setFill('dodger blue')
                elif player == 2:
                    travEdge.setFill('dark orchid')
                elif player == 3:
                    travEdge.setFill('firebrick1')
                    
                travEdge.setArrow('last')
                travEdge.setWidth(3)
                travEdge.draw(self.win)
                self.pathEdgeList.append(travEdge)
#                self.win.getMouse()
            sleep(.5)

        self.allPlayerPathList.append(self.pathEdgeList)
        self.pathEdgeList = []

        if player == 3:
            for j in self.allPlayerPathList[-3:]:
                for h in j:
                    h.undraw()
        
#redraws players last path so as to display the selected path to the user
    def redrawPathEdges(self):
        
        for i in self.allPlayerPathList[-3:]:
            for k in i:
                try:
                    k.draw(self.win)
                    sleep(.25)
                except GraphicsError:
                    print ''
            
#draws POA, Nash, OPT and player Path in GUI
    def drawInfo(self, infoList, optWeight):
        #Add Labels for Nash and add OPT
       player = 1
       strListList = []
       nashWeight = 0

       nashBoxUp = Line(Point(17,0), Point(17,9))
       nashBoxUp.setWidth(3)
       nashBoxUp.setFill('white')
       nashBoxUp.draw(self.win)

       nashBoxAcr = Line(Point(17,9), Point(43,9))       
       nashBoxAcr.setWidth(3)
       nashBoxAcr.setFill('white')
       nashBoxAcr.draw(self.win)

       nashBoxDown = Line(Point(43,9), Point(43,0))
       nashBoxDown.setWidth(3)
       nashBoxDown.setFill('white')
       nashBoxDown.draw(self.win)

       nashText = Text(Point(31,11), 'Nash')
       nashText.setSize(22)
       nashText.setTextColor('white')
       nashText.draw(self.win)
       self.playerInfoList.append(nashText)
       
       for i in infoList:
           pInfo = infoList[player - 1]
           pListInfo = pInfo[0:1]
           pWeight = pInfo[1] #add up for Nash Weight
           nashWeight += pWeight

           for j in pListInfo:
               listInfo = "{ "
               for p in j:
                   listInfo = listInfo + p + ', '
               listInfo = listInfo[:-2] + ' }'
               strListList.append(listInfo)
           

           playerLabel = Text(Point(20, 11 - (3 * player)), "Player " + str(player) + ':')
           playerLabel.setSize(17)
           if player == 1:
              playerLabel.setTextColor('dodger blue')
           elif player == 2:
              playerLabel.setTextColor('dark orchid')
           elif player == 3:
              playerLabel.setTextColor('firebrick1')
           playerLabel.draw(self.win)
           self.playerInfoList.append(playerLabel)

           playerPath = Text(Point(31, 11 - (3 * player)), strListList[player - 1])
           playerPath.setSize(17)
           if player == 1:
              playerPath.setTextColor('dodger blue')
           elif player == 2:
              playerPath.setTextColor('dark orchid')
           elif player == 3:
              playerPath.setTextColor('firebrick1')
           playerPath.draw(self.win)
           self.playerInfoList.append(playerPath)

           playerWeight = Text(Point(41, 11 - (3 * player)), round(pWeight))
           playerWeight.setSize(17)
           if player == 1:
              playerWeight.setTextColor('dodger blue')
           elif player == 2:
              playerWeight.setTextColor('dark orchid')
           elif player == 3:
              playerWeight.setTextColor('firebrick1')
           playerWeight.draw(self.win)
           self.playerInfoList.append(playerWeight)

           player += 1


       nashWeightText = Text(Point(35,46), str(nashWeight))
       nashWeightText.setSize(19)
       nashWeightText.setTextColor('orange2')
       nashWeightText.draw(self.win)
       self.playerInfoList.append(nashWeightText)

       nashLabel = Text(Point(35,48), "Nash Weight")
       nashLabel.setSize(22)
       nashLabel.setTextColor('orange2')
       nashLabel.draw(self.win)
       self.playerInfoList.append(nashLabel)

       optLabel = Text(Point(45,48), 'OPT Weight')
       optLabel.setSize(22)
       optLabel.setTextColor('orange2')
       optLabel.draw(self.win)
       self.playerInfoList.append(optLabel)
        
       optText = Text(Point(45,46), str(optWeight))
       optText.setSize(19)
       optText.setTextColor('orange2')
       optText.draw(self.win)
       self.playerInfoList.append(optText)

       poa = nashWeight / optWeight

       poaLabel = Text(Point(25,48), "POA")
       poaLabel.setSize(22)
       poaLabel.setTextColor('orange2')
       poaLabel.draw(self.win)
       self.playerInfoList.append(poaLabel)

       poaText = Text(Point(25,46), str(poa))
       poaText.setSize(19)
       poaText.setTextColor('orange2')
       poaText.draw(self.win)
       self.playerInfoList.append(poaText)

       optBoxDown = Line(Point(22,50),Point(22,44))
       optBoxDown.setWidth(3)
       optBoxDown.setFill('orange')
       optBoxDown.draw(self.win)

       optBoxAcross = Line(Point(22,44),Point(50,44))
       optBoxAcross.setWidth(3)
       optBoxAcross.setFill('orange')
       optBoxAcross.draw(self.win)

##def main():
##    
##    win = GraphWin('Graph', 700,700)
##    win.setBackground('black')
##    win.setCoords(0,0,50,50)
##
##    title = Text(Point(7,48), "Example of Directed Graph")
##    title.setSize(14)
##    title.setTextColor('white')
##    title.draw(win)
##
##    entryButton = Button(win,7,3,5,10,'blue','white','Enter Weights!')
##    entryButton.draw()
##    
##    G = nx.DiGraph()
##    
##    dG = Graph(G, win)
##
##    dG.createNodes()
##    dG.createEdges()
##    
##    pt = win.getMouse()
##
##    if entryButton.clicked(pt):
##        dG.inputEdges()
##        
##    else:
##        win.getMouse()
##    
##    win.close()


