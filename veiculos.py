class Veiculo:
    __marca = ""
    __modelo = ""
    __ano = 0
    __km = 0

    def __init__(self, marca, modelo, ano, km):
        self.__marca = marca         # Atributo público
        self.__modelo = modelo       # Atributo público
        self.__ano = ano             # Atributo público
        self.__km = km

    def mostrar_informacoes(self):
        """Exibe as informações do veículo."""
        return f"Veículo: {self.__marca} {self.__modelo}, Ano: {self.__ano}, km: {self.__km}"

    def calcular_idade(self, ano_atual):
        """Calcula a idade do veículo."""
        return ano_atual - self.ano

    def get_marca (self):
        return self.__marca
    
    def set_marca (self):
        self.__marca

    def get_modelo (self):
        return self.__modelo
    
    def set_modelo (self):
        self.__modelo
    
    def get_ano (self):
        return self.__ano
    
    def set_ano (self):
        self.__ano

    def get_km (self):
        return self.__km
    
    def set_modelo (self):
        self.__km


Veiculo1 = Veiculo("Chevrolet", "Chevrolet")