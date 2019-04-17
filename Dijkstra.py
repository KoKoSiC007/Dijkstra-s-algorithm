import math
import networkx as nx
import matplotlib.pyplot as plt


def findLowestCostNode(cost):
    lowestCost = math.inf
    lowestCostNode = None
    for node in cost:
        price = cost[node]
        if price < lowestCost and node not in processed: # если прайс ноды меньше минимального и нода не обработана
            lowestCost = price
            lowestCostNode = node
    return lowestCostNode



def dijkstra(g: nx.DiGraph, start, end = None):
    infe = [math.inf] * len(g.nodes)
    cost = dict(zip(g.nodes,infe))  # Стоимость вершин по дефолту inf
    cost[start] = 0
    parents = {} # посешенные першины и их потомки вида НАСЛЕДНИК: ПОТОМК
    # прямой ход
    node = findLowestCostNode(cost)  # ищем ближайшую ноду
    while node is not None:
        price = cost[node]
        neighbors = graph.adj[node]  # все соседи найденой ноды
        for n in neighbors.keys():
            if neighbors[n]['width'] < 0:  #  проверка на отрицательные вершины тк алгоритм работает только с графами без отрицательных вершин
                raise Exception("В графе не должно быть отрицательных ребер.")
            newсost = price + neighbors[n]['width']  #  если текуший прайс ноды больше или равен прайсу предыдушей ноды плюс путь до текушей ноды то устанавливаеться новый прайс
            if cost[n] >= newсost:
                cost[n] = newсost
                parents[n] = node
        processed.append(node)
        node = findLowestCostNode(cost)

    if end == None: # если не указана точка end то функция просто вернет стоимость вершин
        return cost
    # обратный ход
    # print(cost)
    print("Min Price : "+str(cost[end]))
    if cost[end] == math.inf : raise Exception("Минимальный путь не найден")
    path = []
    while True:
        neighbors = graph.adj[end] # находим всех соседий end
        for n in neighbors.keys():
            if neighbors[n]['width'] == (cost[end] - cost[n]):  #  проверяем есть прайс конца - прайс соседа равен пути между ними значит мы проходили по этой ноде записаем в path
                path.append(end)
                end = n
                if end == start: # если текущяя точка равна началу то мы дошли
                    path.append(start)
                    return path[::-1]
                continue

    return path  #  возвращяем путь



#  File input

graph = nx.read_edgelist('text.txt', create_using=nx.Graph(), data=(('width', int),))
processed = []

dict = dijkstra(graph,'v0','v4')
print(" -> ".join(dict))


nx.draw(graph, with_labels=True)
plt.show()
