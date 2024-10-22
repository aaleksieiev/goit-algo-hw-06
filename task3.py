import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

from railway_lines_of_Ukraine import railway_lines_with_dist

def dijkstra(graph, start):
    # Ініціалізація відстаней та множини невідвіданих вершин
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    unvisited = list(graph.nodes())

    while unvisited:
        # Знаходження вершини з найменшою відстанню серед невідвіданих
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        # Якщо поточна відстань є нескінченністю, то ми завершили роботу
        if distances[current_vertex] == float('infinity'):
            break

        # Переглядаємо всіх сусідів поточної вершини
        for neighbor in graph.neighbors(current_vertex):
             # отримуємо вагу ребра
            weight = graph[current_vertex][neighbor].get('weight', 1)
            distance = distances[current_vertex] + weight

            # Якщо нова відстань коротша, то оновлюємо найкоротший шлях
            if distance < distances[neighbor]:
                distances[neighbor] = distance

        # Видаляємо поточну вершину з множини невідвіданих
        unvisited.remove(current_vertex)

    return distances

def main():

    G = nx.Graph()
    G.graph["name"] = "Railway lines of Ukraine"
    G.add_weighted_edges_from(railway_lines_with_dist)

    # Виклик функції для вершини A
    print(dijkstra(G, "Львів"))
    
if __name__ == "__main__":
    main()