import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

from railway_lines_of_Ukraine import railway_lines

def dfs_iterative(graph, start_vertex):
    visited = set()
    # Використовуємо стек для зберігання вершин
    stack = [start_vertex]  
    while stack:
        # Вилучаємо вершину зі стеку
        vertex = stack.pop()  
        if vertex not in visited:
            print(vertex, end=' ')
            # Відвідуємо вершину
            visited.add(vertex)
            # Додаємо сусідні вершини до стеку
            stack.extend(graph.neighbors(vertex))  

def bfs_iterative(graph, start):
    # Ініціалізація порожньої множини для зберігання відвіданих вершин
    visited = set()
    # Ініціалізація черги з початковою вершиною
    queue = deque([start])

    while queue:  # Поки черга не порожня, продовжуємо обхід
        # Вилучаємо першу вершину з черги
        vertex = queue.popleft()
        # Перевіряємо, чи була вершина відвідана раніше
        if vertex not in visited:
            # Якщо не була відвідана, друкуємо її
            print(vertex, end=" ")
            # Додаємо вершину до множини відвіданих вершин
            visited.add(vertex)
            # Додаємо всіх невідвіданих сусідів вершини до кінця черги
            # Операція різниці множин вилучає вже відвідані вершини зі списку сусідів
            queue.extend(set(graph.neighbors(vertex)) - visited)
    # Повертаємо множину відвіданих вершин після завершення обходу
    return visited




def main():

    G = nx.Graph()
    G.graph["name"] = "Railway lines of Ukraine"
    G.add_edges_from(railway_lines)

    print("DFS: \n")

    dfs_iterative(G, "Львів")

    print("\n \n BFS: \n")

    bfs_iterative(G, "Львів")
    
if __name__ == "__main__":
    main()