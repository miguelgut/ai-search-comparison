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
        self.priority_queue = []
        self.inicio = inicio
        self.goal = goal
        self.print_results = print_results


    def solveBfs(self):
        inicio_state = EstadoString(self.inicio, 0, self.inicio, self.goal)
        self.priority_queue.append(inicio_state)

        count = 0

        closest_child = self.priority_queue[count]
        closest_child.criafilho()

        while not self.path and len(self.priority_queue):
            closest_child = self.priority_queue[count]
            closest_child.criafilho()

            self.visited_queue.append(closest_child.value)
            print("Visitou: "+ str(closest_child.value))

            for child in closest_child.filhos:
                if child.value not in self.visited_queue:
                    
                    if not child.dist:
                        self.path = child.path
                        break

                    self.priority_queue.append(child)
                    count += 1

        if not self.path:
            print(f'Goal of {self.goal} is not possible!')
        return self.path


def printManually(start, destiny, prefix, label):
    print(start +".."+str(prefix)+ " --> " + destiny + ".."+ str(label) + "")

def resolveArvore(inicio, fim, print_results):
    _arvore = Solucionador(inicio, fim, print_results)
    _arvore.solveBfs()
    print(_arvore.path)

if __name__ == '__main__':
    start_time = time.time()
    #1
    #resolveArvore('abc', 'cba',0);
    
    #2
    #resolveArvore('elcup', 'ucpel',1);
    
    #3
    resolveArvore('eigtclinenia', 'inteligencia', 0);
    
    print("--- %s seconds ---" % (time.time() - start_time))

