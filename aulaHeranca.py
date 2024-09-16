class Produto:

    descricao = ""
    lucro = 0.0
    custo = 0

    def __init__(self, descricao, custo, lucro,):
        self.descricao = descricao
        self.custo = custo
        self.lucro = lucro

    def calcular_preco(self):
        return self.custo + (self.custo * self.lucro)

    def mostrar_descricao_preco (self):
        return f"Descrição: {self.descricao}\nPreço: R$ {self.calcular_preco():.2f}"

class ProdutoImportado(Produto):
    TAXA_IMPORTACAO = 0.05

    def calcular_preco(self):
        preco_base = super().calcular_preco()
        return preco_base + (preco_base * self.TAXA_IMPORTACAO)

    def mostrar_descricao_preco (self):
        return f"Descrição(importado):{self.descricao}\nPreço: R$ {self.calcular_preco():.2f}"


produto1 = Produto("Laptop do Ben 10, Candide, Modelo: Omnibook, Utiliza 3 pilhas AA (Não Inclusas),Super Compacto com Alça para Transporte",100, 0.2)
produto2 = ProdutoImportado("Laptop do Ben 10, Candide, Modelo: Omnibook, Utiliza 3 pilhas AA (Não Inclusas),Super Compacto com Alça para Transporte",150, 0.15)

print(f"Seu produto é um/a {produto1.mostrar_descricao_preco()} preço do produto 1: R$ {produto1.calcular_preco()}")
print("--- --- ---")
print(f"Seu produto é um/a {produto2.mostrar_descricao_preco()} preço do produto 2 (importado): R$ {produto2.calcular_preco()}")