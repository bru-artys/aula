class Disciplina():
    nome = ""
    professor = ""
    n1= 0
    n2 = 0

    def __init__(self, nome, professor, n1 = 0, n2 = 0):
        self.nome = nome
        self.professor = professor
        self.n1 = n1
        self.n2 = n2

    def calcularMedia(self):
        return (self.n1*2 + self.n2*3)/5.0
    

class DisciplinaAnual(Disciplina):
    n3 = 0 
    n4 = 0

    def __init__(self, nome, professor, n1=0, n2=0, n3 = 0 , n4 = 0):
        super().__init__(nome, professor, n1, n2)
        self.n3 = n3
        self.n4 = n4 

    def calcularMedia(self):
        return (self.n1*2 + self.n2*2 + self.n3*3 + self.n4*3 )/10


disciplina1 = DisciplinaAnual("matematica","olswaldo",60,70,50,80)
disciplina1.calcularMedia
disciplina2 = Disciplina("filosofia","lula",100,90)
