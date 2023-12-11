from pysys import *


graph = None

class Graphs:
    def __init__(self, nameOfGraph, percentUsed):
        self.nameOfGraph = str(nameOfGraph)
        self.percentUsed = percentUsed
        
    def basicInfoGraph(self):
        if self.percentUsed <= 10.0:
            graph = "#|||||||||"
            print(f"{self.nameOfGraph}   {graph}   {self.percentUsed}")
        elif self.percentUsed <= 20.0 and self.percentUsed > 10.0:
            graph = "##||||||||"
            print(f"{self.nameOfGraph}   {graph}   {self.percentUsed}")
        elif self.percentUsed <= 30.0 and self.percentUsed > 20.0:
            graph = "###|||||||"
            print(f"{self.nameOfGraph}   {graph}   {self.percentUsed}")
        elif self.percentUsed <= 40.0 and self.percentUsed > 30.0:
            graph = "####||||||"
            print(f"{self.nameOfGraph}   {graph}   {self.percentUsed}")
        elif self.percentUsed <= 50.0 and self.percentUsed > 60.0:
            graph = "#####|||||"
            print(f"{self.nameOfGraph}   {graph}   {self.percentUsed}")
        elif self.percentUsed <= 60.0 and self.percentUsed > 50.0:
            graph = "######||||"
            print(f"{self.nameOfGraph}   {graph}   {self.percentUsed}")
        elif self.percentUsed <= 70.0 and self.percentUsed > 60.0:
            graph = "#######|||"
            print(f"{self.nameOfGraph}   {graph}   {self.percentUsed}")
        elif self.percentUsed <= 80.0 and self.percentUsed > 70.0:
            graph = "########||"
            print(f"{self.nameOfGraph}   {graph}   {self.percentUsed}")
        elif self.percentUsed <= 90.0 and self.percentUsed > 80.0:
            graph = "#########|"
            print(f"{self.nameOfGraph}   {graph}   {self.percentUsed}")
        else:
            graph = "##########"
            print(f"{self.nameOfGraph}   {graph}   {self.percentUsed}")
            
    def onlyDrawGraph(self):    
        if self.percentUsed <= 10.0:
            graph = "#|||||||||"
            print(f"{graph}")
        elif self.percentUsed <= 20.0 and self.percentUsed > 10.0:
            graph = "##||||||||"
            print(f"{graph}")
        elif self.percentUsed <= 30.0 and self.percentUsed > 20.0:
            graph = "###|||||||"
            print(f"{graph}")
        elif self.percentUsed <= 40.0 and self.percentUsed > 30.0:
            graph = "####||||||"
            print(f"{graph}")
        elif self.percentUsed <= 50.0 and self.percentUsed > 60.0:
            graph = "#####|||||"
            print(f"{graph}")
        elif self.percentUsed <= 60.0 and self.percentUsed > 50.0:
            graph = "######||||"
            print(f"{graph}")
        elif self.percentUsed <= 70.0 and self.percentUsed > 60.0:
            graph = "#######|||"
            print(f"{graph}")
        elif self.percentUsed <= 80.0 and self.percentUsed > 70.0:
            graph = "########||"
            print(f"{graph}")
        elif self.percentUsed <= 90.0 and self.percentUsed > 80.0:
            graph = "#########|"
            print(f"{graph}")
        else:
            graph = "##########"
            print(f"{graph}")