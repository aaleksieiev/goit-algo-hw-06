import networkx as nx
import matplotlib.pyplot as plt

from railway_lines_of_Ukraine import railway_lines

def main():
    #G = nx.DiGraph()
    G = nx.Graph()
    G.graph["name"] = "Railway lines of Ukraine"
    G.add_edges_from(railway_lines)

    print(f"Nodes count: {G.number_of_nodes()} \n")
    print(f"Edges count: {G.number_of_edges()} \n")
    print(f"Graph is connected: {nx.is_connected(G)} \n")
    print(f"Degree cenrality: {nx.degree_centrality(G)} \n")
    print(f"Closeness centrality: {nx.closeness_centrality(G)} \n")
    print(f"Betweenness centralit: {nx.betweenness_centrality(G)} \n")

    nx.draw(
        G,
        #nx.shell_layout(G),
        with_labels=True,
        #font_size=10,
        #node_size=1000,
        #node_color="red",
        #font_color="blue",
        #font_weight="bold",
        #arrowsize=5,
    )
    plt.show()

if __name__ == "__main__":
    main()