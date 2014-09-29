import csv
import networkx as nx
import matplotlib.pyplot as plt
import numpy

def get_stations():
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


get_stations()
