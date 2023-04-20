class Grafo:
    def __init__(self):
        self.matriz = [
            [0,0,1,0,0],
            [0,0,1,0,0],
            [1,1,0,1,1],
            [0,0,1,0,1],
            [0,0,1,1,0]
        ]

    def tem_ligacao(self, a, b):
        return True if (self.matriz[a][b] == 1) else False

    def print_matriz(self):
        nodos = ['A', 'B', 'C', 'D', 'E']
        for i,item in enumerate(nodos):
            if i==0:
                print("   ", end="")
            print(item + "  ", end="")
        print() # quebra de linha
         
        for i, linha in enumerate(self.matriz):
            print(nodos[i], end=" ")
            print(linha)

g = Grafo()
g.print_matriz()
# verifica se nodos 'E' e 'C' possuem ligação
print("Existe ligacao entre 4 e 2? {}".format(g.tem_ligacao(4,2)))

        
        
