import time
import networkx as nx
import numpy.random as rnd
import matplotlib.pyplot as plt
import pydot
from networkx.drawing.nx_pydot import graphviz_layout

# Сложить 2 вектора
def add_vector(vector_one, vector_two):
    if len(vector_one) == len(vector_two):
        result = []
        for i in range(0, len(vector_one)):
            result.append(vector_one[i] + vector_two[i])
        return result
    else:
        return None

# Проверка, что векторы - это одно и то же, но одна из компонент больше или равна
def check_inf(vector_one, vector_two):
    flag = 0
    if len(vector_one) == len(vector_two):
        for i in range(0, len(vector_one)):
            if vector_one[i] <= vector_two[i]:
                flag = flag + 1
        # Есть бесконечность
        if flag == 1:
            return True
        # Нет бесконечности
        else:
            return False
    else:
        # Ошибка с размерностями
        return None

# Проверка, что из корня можно добраться до нужной вершины
# Возвращается true или false
def check_path(root, target, tree):
    return nx.has_path(tree, root, target)

# Проверка, что в векторе нет отрицательных элементов
def check_negative(vector):
    for i in range(0, len(vector)):
        if vector[i] < 0:
            return False
    return True

if __name__ == '__main__':

    plt.figure()

    # Начальная отсечка времени работы программы
    start_time = time.time()

    # Дерево достижимости
    reachability_tree = nx.DiGraph()

    # Размерность системы
    space_size = 5

    node_num = 0

    # Начальный вектор
    d = [1, 0, 0, 0, 0]

    # Управляющие вектора
    W = [[-1, 1, 0, 0, 0], [-1, 0, 0, 1, 0], [0, -1, 2, 0, 0], [0, 1, -1, 0, 0], [0, 0, 0, -1, 2], [0, 0, 0, 1, -1]]

    # Узлы дерева
    l = [[d]]

    # Сохранение номеров веток
    branch_name = []

    # Добавляем начальный вектор как узел дерева
    reachability_tree.add_node(", ".join(map(str, d)))

    # Заданное кол-во шагов
    while node_num != 10:

        L = []
        l_branch_name = []

        # Выбираем узлы с данного шага
        for j in range(0, len(l[node_num])):
            # Проходим по управляющим векторам
            for i in range(0, len(W)):
                # Складываем их
                result = add_vector(l[node_num][j], W[i])
                # Если результат не выходит за 1 четверть плоскости
                if check_negative(result):
                    # Сохраняем новую вершину в массив
                    L.append(result)
                    # Добавляем новую вершину в дерево и добавляем ветки из родительской вершины к новой
                    parent = ", ".join(map(str, l[node_num][j]))
                    son = ", ".join(map(str, result))

                    reachability_tree.add_node(son, vector=son)
                    reachability_tree.add_edge(parent, son, weight=i+1)

        l.append(L)
        node_num = node_num + 1

    # Для проверки
    print("Что лежит в массиве:")
    print(l)

    print("Узлы дерева:")
    print(reachability_tree.nodes)

    print("Ветки дерева:")
    print(reachability_tree.edges.data())

    layout = nx.spring_layout(reachability_tree)

    labels = nx.get_edge_attributes(reachability_tree, "weight")

    pos = nx.planar_layout(reachability_tree)

    nx.draw(reachability_tree, pos,
                     node_color='green',
                     node_size=1500,
                     with_labels=True, arrows = True,
                     width=1, linewidths=0.2, alpha=0.9)

    # Подписи на ребрах. Рисует криво. Переделать нумерацию ребер и вершин?
    # nx.draw_networkx_edge_labels(reachability_tree, layout, edge_labels=labels)

    plt.axis('off')
    plt.show()

    print("--- %s seconds ---" % (time.time() - start_time))
