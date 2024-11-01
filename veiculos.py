class Veiculo:
    def __init__(self, marca, modelo, ano, km):
        self.__marca = marca        
        self.__modelo = modelo      
        self.__ano = ano            
        self.__km = km              
    
    def get_marca(self):
        return self.__marca
    
    def set_marca(self, marca):
        self.__marca = marca

    def get_modelo(self):
        return self.__modelo
    
    def set_modelo(self, modelo):
        self.__modelo = modelo
    
    def get_ano(self):
        return self.__ano
    
    def set_ano(self, ano):
        if ano > 1885:
            self.__ano = ano
        else:
            print("Ano inválido")

    def get_km(self):
        return self.__km
    
    def set_km(self, km):
        if km >= 0:
            self.__km = km
        else:
            print("Quilômetro nunca é negativo")

    def mostrar_informacoes(self):
        """Exibe as informações do veículo."""
        print(f"Veículo: {self.__marca} {self.__modelo}, Ano: {self.__ano}, km: {self.__km}")

    def calcular_idade(self, ano_atual):
        """Calcula a idade do veículo."""
        return ano_atual - self.get_ano()

Veiculo1 = Veiculo("Chevrolet", "Corvette C6", 2024, 1500)
Veiculo1.mostrar_informacoes()

ano_atual = 2023
print("Idade do veículo:", Veiculo1.calcular_idade(ano_atual))

Veiculo1.set_km(20000)
print("KM atualizado:", Veiculo1.get_km())

Veiculo1.set_ano(1800)
print("Ano atual:", Veiculo1.get_ano())