import networkx as nx
import matplotlib.pyplot as plt
import numpy
import csv

class TubeMap:
    def __init__(self,file_name):
        self.map = None
        self.file_name = filename

    def get_stations(self):
        with open("tube.csv",mode="r",encoding ="utf-8") as stations:
            reader = csv.reader(stations)
            for line in reader:
                print(line[0])
                print(line[1])
                print(line[2:])
                print()
                data = {"line name":line[0],"edge colour":line[1]}
                print(data)
                print()
                print()
                tube_graph = nx.graph()
                tube_graph.add_path(line[2:],data)

    def generate_edge_colours(self,current_map):
        return edge_colours

    def create_graph_plot(self,current_map):
        pass

    def display_full_map(self):
        pass

    def display_travel_map(self,start,end):
        pass

    def get_directions(self,start,end):
        return directions

if __name__ == "__main__":
    
