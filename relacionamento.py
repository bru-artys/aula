class Pais:
    def __init__(self,nome, população, area):
        self.nome = nome
        self.populacao = população
        self.area = area
    
    def imprimir_populacao (self):
        print(f"população de {self.nome} tem {self.populacao} habitantes")
    
    def imprimir_area (self):
        print(f"o pais {self.nome} tem uma area de {self.area} em km²")

    def calcular_Densidade_Demografica(self):
        densidade = self.populacao / self.area
        print(f"A densidade demografico de {self.nome} : {densidade:.2f} pessoas/km²")
        return densidade

class Continente:
    def __init__(self,nome):
        self.nome = nome
        self.paises = []

    def adicionarPais(self,pais):
        self.paises.append(pais)
    
    def imprimir_informacoes (self):
        print(f"continente:{self.nome}")
        print("paises:")
        for pais in self.paises:
            print(f"- {pais.nome}")

    def exibir_pais_mais_populoso(self):
        Pais_mais_populoso = ""
        tamanho = 0
        for pais in self.paises:
            if pais.populacao > tamanho:
                Pais_mais_populoso = pais.nome
        print(f"Pais mais populoso: {Pais_mais_populoso}")
    
    def exibir_pais_mais_extenso(self):
        pais_mais_extenso = ""
        tamanho = 0
        tamanho += self.are
        for pais in self.paises:
            if pais.area > tamanho:
                pais_mais_extenso = pais.nome
        print(f"pais mais extenso : {pais_mais_extenso}")

pais1 = Pais( "Brasil",212.6,8.510)
pais2 = Pais("Peru",34.35,1.285)
pais3 = Pais("EUA",54.35,7.285)

pais1.imprimir_populacao()
pais1.imprimir_area()
pais1.calcular_Densidade_Demografica()

print("--- --- ---")
continente1 = Continente ("America do sul")
continente1.adicionarPais(pais3)
continente1.adicionarPais(pais2)
continente1.adicionarPais(pais1)
continente1.imprimir_informacoes()
continente1.exibir_pais_mais_populoso()
continente1.exibir_pais_mais_extenso()