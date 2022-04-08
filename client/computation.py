import numpy as np


class Node:
    # 使用字典来跟踪连接其的节点和每条边的权重
    def __init__(self, key, weight=None):
        self.id = key
        self.connectedTo = {}  # 该字典中存放着该点到其他点的权重
        self.total_weight = weight  # 到达该节点之前所有点的权重

    def addNeighbor(self, to_nn, weight=0):  # 构建字典为当前节点的连接点：路径权重 (nbr为节点的实例对象)
        self.connectedTo[to_nn] = weight

    def __str__(self):
        return 'id: ' + str(self.id) + 'connected with: ' + str(
            [x.id for x in self.connectedTo]) + 'with total_weight: ' + str(
            self.total_weight)

    # def getConnections(self):  # 返回邻接表中的所有的项点
    #     return self.connectedTo.keys()  # 获得当前节点连接的所有节点

    def getId(self):
        return self.id  # 获得当前节点的id

    def getWeight(self):
        return self.total_weight  # 获得当前节点的权重

    def getConnnect(self):
        pass
        # return self.connectedTo[]


class Graph:
    def __init__(self):
        self.nodeDic = {}  # 将所有节点存放入该list
        self.numNode = 0  # 节点总数

    def addNode(self, key, weight):
        self.numNode = self.numNode + 1  # 所有节点总计数加一
        newNode = Node(key, weight)  # 创建一个新节点实例
        self.nodeDic[key] = newNode  # 将新节点存放入nodeDic字典，以便之后使用id索引节点
        # return newNode

    def getNode(self, n):
        if n in self.nodeDic:  # 输入一个id，若该id对应的节点在nodeDic中则返回该节点实例
            return self.nodeDic[n]
        else:
            return None

    def getTotalweight(self, n):
        node = self.getNode(n)
        return node.getWeight()

    def __contains__(self, n):  # 便于使用 n in nodeDic
        return n in self.nodeDic

    def addEdge(self, n, to_n=None, w=0):  # 为一个节点到另外一个节点添加一个权重（输入id）
        if n not in self.nodeDic:
            self.addNode(n, w)
        nv = self.nodeDic[n]
        if to_n not in self.nodeDic:
            self.addNode(to_n, w + nv.total_weight)
        self.nodeDic[n].addNeighbor(self.nodeDic[to_n], w)

    def getVertices(self):  # 获取所有节点实例对象
        return self.nodeDic.keys()

    def __iter__(self):
        return iter(self.nodeDic.values())


class Graph_128:
    def __init__(self, graph, graphList):
        self.graphList = graphList
        self.g = graph
        self.matrix = []
        self.nodeDic_128 = {0: 0, 1: 0, 2: 0, 3: 1, 4: 1, 5: 2, 6: 2, 7: 3, 8: 3, 9: 4, 10: 4, 11: 5, 12: 5, 13: 6,
                            14: 6, 15: 7, 16: 7, 17: 8, 18: 8, 19: 9, 20: 9, 21: 10, 22: 10, 23: 11, 24: 11, 25: 12,
                            26: 12, 27: 13, 28: 13, 29: 14, 30: 14, 31: 15, 32: 15, 33: 16, 34: 16, 35: 17, 36: 17,
                            37: 18, 38: 18, 39: 19, 40: 19, 41: 20, 42: 20, 43: 21, 44: 21, 45: 22, 46: 22, 47: 23,
                            48: 23, 49: 24, 50: 24, 51: 25, 52: 25, 53: 26, 54: 26, 55: 27, 56: 27, 57: 28, 58: 28,
                            59: 29, 60: 29, 61: 30, 62: 30, 63: 31, 64: 31, 65: 32, 66: 32, 67: 33, 68: 33, 69: 34,
                            70: 34, 71: 35, 72: 35, 73: 36, 74: 36, 75: 37, 76: 37, 77: 38, 78: 38, 79: 39, 80: 39,
                            81: 40, 82: 40, 83: 41, 84: 41, 85: 42, 86: 42, 87: 43, 88: 43, 89: 44, 90: 44, 91: 45,
                            92: 45, 93: 46, 94: 46, 95: 47, 96: 47, 97: 48, 98: 48, 99: 49, 100: 49, 101: 50, 102: 50,
                            103: 51, 104: 51, 105: 52, 106: 52, 107: 53, 108: 53, 109: 54, 110: 54, 111: 55, 112: 55,
                            113: 56, 114: 56, 115: 57, 116: 57, 117: 58, 118: 58, 119: 59, 120: 59, 121: 60, 122: 60,
                            123: 61, 124: 61, 125: 62, 126: 62}

    def createGraph(self):
        for num, weight in enumerate(self.graphList):
            self.g.addEdge(self.nodeDic_128[num], num, weight)  # 通过输入的权重节点list来构建图
        return self.g

    def createMatrix(self):
        list_8 = [63, 65, 71, 73, 95, 97, 103, 105]
        for i, m in enumerate(list_8):
            self.matrix.append([self.g.getTotalweight(m), self.g.getTotalweight(m + 1), self.g.getTotalweight(m + 4),
                                self.g.getTotalweight(m + 5), self.g.getTotalweight(m + 16),
                                self.g.getTotalweight(m + 17), self.g.getTotalweight(m + 20),
                                self.g.getTotalweight(m + 21)])
        return self.matrix


if __name__ == "__main__":
    g = Graph()
    graphList = np.ones(127)  # 输入权重list
    graphList = list(graphList)
    g_128 = Graph_128(g, graphList)
    g_create_128 = g_128.createGraph()
    matrix_128 = g_128.createMatrix()
    print(matrix_128)

    for v in g_create_128:
        print(v)
