class Conteudo:
    def __init__(self, titulo, genero):
        self.titulo = titulo
        self.genero = genero
    def exibir_info(self):
        print("CONTEUDO:", self.titulo, "| Genero:", self.genero)

class Serie(Conteudo):
    def __init__(self, titulo, genero, temporadas):
        super().__init__(titulo, genero)
        self.temporadas = temporadas
    def exibir_info(self):
        print("SERIE:", self.titulo,
        "| Genero:", self.genero,
        "| Temporadas:", self.temporadas)

class Documentario(Conteudo):
    def __init__(self, titulo, genero, tema):
        super().__init__(titulo, genero)
        self.tema = tema
    def exibir_info(self):
        print("DOCUMENTARIO:", self.titulo,
        "| Genero:", self.genero,
    "| Tema:", self.tema)

serie1 = Serie("Stranger Things", "Ficcao", 4)
documentario1 = Documentario("Nosso Planeta", "Natureza", "Vida selvagem")
serie1.exibir_info()
documentario1.exibir_info()