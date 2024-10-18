import networkx as nx
import matplotlib.pyplot as plt

from railway_lines_of_Ukraine import railway_lines

def main():
    #G = nx.DiGraph()
    G = nx.Graph()
    G.graph["name"] = "Railway lines of Ukraine"
    G.add_edges_from(railway_lines)
    
if __name__ == "__main__":
    main()