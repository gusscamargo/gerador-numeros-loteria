import random

class Gerador:
    def __init__(self, numeros):
        self.numeros = numeros

    def gerar(self):
        result = []

        while len(result) < self.numeros:
            n = random.randint(1, 60)

            if n not in result:
                result.append(n)
            
        return sorted(result)
                




if __name__ == "__main__":
    numeros = int(input("Digite quantos numeros quer gerar: "))

    gerador = Gerador(numeros)

    print("Seus numeros: ", gerador.gerar())