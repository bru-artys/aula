class produto:

    codigo = ""
    nome = ""
    preco = 0.0
    quantidade = 0

    def __init__ (self, codigo, nome, preco, quantidade ):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def atulizar_preco(self,novo_preco):
         self.preco = novo_preco

    def atualizar_quantidade(self,nova_quantidade):
         self.quantidade = nova_quantidade

    def vender (self,qtd):
        if qtd <= self.quantidade:
         self.quantidade -= qtd
        else:
         print("erro de quantidade")

    def mostrando_produto (self, ):
       print(f"codigo:{self.codigo}")
       print(f"nome:{self.nome}")
       print(f"preco:{self.preco:.2f}")
       print(f"quantidade:{self.quantidade}")


produto1 = produto ("P035","LgK10",900.50,10 )
print(f"produto:{produto1.codigo}, nome:{produto1.nome}, preço:{produto1.preco}, quantidade:{produto1.quantidade}")

produto2 = produto ("B019","notebook_positivo",1775.99,3 )
print(f"produto:{produto2.codigo}, nome:{produto2.nome}, preço:{produto2.preco}, quantidade:{produto2.quantidade}")

produto3 = produto ("E022","celular_xuxa",5000.00,1 )
print(f"produto:{produto3.codigo}, nome:{produto3.nome}, preço:{produto3.preco}, quantidade:{produto3.quantidade}")
print("--- --- ---")

produto1.vender(7)
produto1.atulizar_preco(2199.99)
produto1.mostrando_produto()
