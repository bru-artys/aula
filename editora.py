class Editora:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco

    def __str__(self):
        return (f"Editora: {self.nome}, Endereço: {self.endereco}")


class Publicacao:
    def __init__(self, titulo = str, editora = str, total_paginas = int):
        self.titulo = titulo
        self.editora = editora  
        self.total_paginas = total_paginas
        self.paginas_lidas =[]

    def paginas_lidas(self, paginas_lidas):
        if 0 <= paginas_lidas <= self.total_paginas:
            self.paginas_lidas = paginas_lidas
        else:
            paginas_lidas > self.total_paginas
            print("Número de páginas lidas inválido.")

    def exibir_progresso(self):
        paginas_restantes = self.total_paginas - self.paginas_lidas
        print(
            f"Foram lidas {self.paginas_lidas} páginas do livro '{self.titulo}'. "
            f"Restam {paginas_restantes} páginas a serem lidas."
        )
     def verificando_paginas(self):
         self.paginas_lidas - self.total_paginas
         if self.paginas_lidas > self.total_paginas:
            print (f"")

    def __str__(self):
        return f"Título: {self.titulo}, Total de páginas: {self.total_paginas}"


editora1 = Editora("Editora Alpha", "Rua das Flores, 123")
livro1 = Publicacao("Python para Todos", editora1, 150)

livro1.paginas_lidas(160)
livro1.exibir_progresso()
print(livro1.editora)
