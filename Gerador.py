from random import randint

class Gerador:
    def __init__(self, numeros):
        self.numeros = numeros
    
    def gerar(self):
        return sorted([randint(1, 60) for _ in range(self.numeros)])
                

if __name__ == "__main__":
    numeros = int(input("Digite quantos numeros quer gerar: "))

    gerador = Gerador(numeros)

    print("Seus numeros: ", gerador.gerar())