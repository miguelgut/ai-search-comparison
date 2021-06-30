#!/usr/bin/env python

# Fila de prioriades para saber o peso de cada alternativa
from queue import PriorityQueue
from anytree import Node, RenderTree
from anytree.exporter import DotExporter
import time

# Declaração do estado
class Estado(object):
    def __init__(self, value, parent, inicio=0, goal=0):
        self.filhos = []
        self.parent = parent
        self.value = value
        self.dist = 0
        if parent:
            self.path = parent.path[:]
            self.path.append(value)
            self.inicio = parent.inicio
            self.goal = parent.goal
        else:
            self.path = [value]
            self.inicio = inicio
            self.goal = goal

    def getdist(self):
        pass

    def criafilho(self):
        pass

    def toString(self):
        pass


class EstadoString(Estado):
    def __init__(self, value, parent, inicio=0, goal=0):
        super(EstadoString, self).__init__(value, parent, inicio, goal)
        self.dist = self.getdist()

    # Override da função distância:
    # Calcula quanto falta para o estado atual da string chegar ao destino
    def getdist(self):
        if self.value == self.goal:
            return 0
        dist = 0
        for i in range(len(str(self.goal))):
            letter = str(self.goal)[i]
            dist += abs(i - self.value.index(letter))
        return dist
    ## Override da função para criar os nodos filhos
    ## Cria todas as strings adjacentes possíveis a string atual
    def criafilho(self):
        if not self.filhos:
            for i in range(len(str(self.goal)) - 1):
                val = self.value
                val = val[:i] + val[i + 1] + val[i] + val[i + 2:]
                child = EstadoString(val, self)
                self.filhos.append(child)

    def toString(self):
        return str(self.value) + "(" + str(self.dist) + ")"


# Classe responsável para solucionar
class Solucionador:
    def __init__(self, inicio, goal, print_results):
        self.path = []
        self.visited_queue = []
        self.priority_queue = PriorityQueue()
        self.inicio = inicio
        self.goal = goal
        self.print_results = print_results

    def solve(self):
        inicio_state = EstadoString(self.inicio, 0, self.inicio, self.goal)
        count = 0
        self.priority_queue.put((0, count, inicio_state))
        ## Enquanto não há caminho definido e existe uma fila de prioridades para iterar
        while not self.path and self.priority_queue.qsize():
            ## Pega o filho mais próximo e criar suas variações
            closest_child = self.priority_queue.get()[2]
            if(self.print_results == 1):
                print("String com maior prioridade: " + closest_child.value)
            closest_child.criafilho()

            ## Marca este filho como visitado para não buscar novamente 
            self.visited_queue.append(closest_child.value)
            if(self.print_results == 1):
                print("\n")
                print("String atual: " + closest_child.value + " - Distancia atual: " + str(closest_child.dist))
                print("Calculando a distancia dos filhos para saber qual é mais proximo:")

            for child in closest_child.filhos:
                if child.value not in self.visited_queue:
                    count += 1
                    ## Se não há distância do destino ao objetivo, o caminho atual encontrou e acaba a execução
                    if not child.dist:
                        self.path = child.path
                        break

                    if(self.print_results == 1):
                        print(child.value + ": "+ str(child.dist))
                        printManually(closest_child.value,child.value,closest_child.dist, child.dist)
                    ## Se há distância, salva na fila de prioridades rankeado pela distância
                    self.priority_queue.put((child.dist, count, child, child.path))

        print(self.path)
        if not self.path:
            print(f'Goal of {self.goal} is not possible!')
        return self.path

def printPriorityQueue(pq):
    i = j = 0
    solver = Node(pq.queue[0][3])

    for i in range(pq.qsize()):
        ## Sempre começa em 1 pois todas as filas iniciam com a string original
        qElement = pq.queue[i]
        startNode = pq.queue[i][3];
        pathStart = Node(startNode[1], parent=solver)

        ## Sempre começa em 2 pois todas as filas já tem o inicio da arvore na linha acima
        for j in range(2, len(startNode)):
            n = Node(startNode[j], parent=pathStart)
            pathStart = n

    printTree(solver)
    #DotExporter(solver).to_picture("alternate.png")

def printTree(tree):
    for pre, fill, node in RenderTree(tree):
        print("%s%s" % (pre, node.name))

    DotExporter(tree).to_picture("printTree.png")


def printManually(start, destiny, prefix, label):
    print(start +".."+str(prefix)+ " --> " + destiny + ".."+ str(label) + "")

def resolveArvore(inicio, fim, print_results):
    _arvore = Solucionador(inicio, fim, print_results)
    _arvore.solve()

if __name__ == '__main__':
    start_time = time.time()
    #1
    #resolveArvore('abc', 'cba',1);
    
    #2
    #resolveArvore('elcup', 'ucpel',1);
    
    #3
    resolveArvore('eigtclinenia', 'inteligencia', 0);
    
    print("--- %s seconds ---" % (time.time() - start_time))

