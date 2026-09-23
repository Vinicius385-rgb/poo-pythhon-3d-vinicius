class Conteudo:
    def __init__(self, titulo, genero):
        self.titulo = titulo
        self.genero = genero

    def exibir_info(self):
        print(f"Título: {self.titulo} | Gênero: {self.genero}")


class Filme(Conteudo):
    def __init__(self, titulo, genero, duracao):
        super().__init__(titulo, genero)
        self.duracao = duracao

    def exibir_info(self):
        print(f"Filme: {self.titulo} | Gênero: {self.genero} | Duração: {self.duracao} min")


class Serie(Conteudo):
    def __init__(self, titulo, genero, temporadas):
        super().__init__(titulo, genero)
        self.temporadas = temporadas

    def exibir_info(self):
        print(f"Série: {self.titulo} | Gênero: {self.genero} | Temporadas: {self.temporadas}")


class Documentario(Conteudo):
    def __init__(self, titulo, genero, tema):
        super().__init__(titulo, genero)
        self.tema = tema

    def exibir_info(self):
        print(f"Documentário: {self.titulo} | Gênero: {self.genero} | Tema: {self.tema}")


# Missão 3: nova classe
class Podcast(Conteudo):
    def __init__(self, titulo, genero, episodios):
        super().__init__(titulo, genero)
        self.episodios = episodios

    def exibir_info(self):
        print(f"Podcast: {self.titulo} | Gênero: {self.genero} | Episódios: {self.episodios}")


# Missão 1: catálogo misto
catalogo = [
    Filme("Interestelar", "Ficcao", 169),
    Filme("Shrek", "Animacao", 90),
    Serie("Stranger Things", "Ficcao", 4),
    Serie("Round 6", "Suspense", 2),
    Documentario("Nosso Planeta", "Natureza", "Vida selvagem")
]


# Adicionando o Podcast
catalogo.append(
    Podcast("Flow Podcast", "Entrevista", 500)
)


# Missão 2: um único laço
for item in catalogo:
    item.exibir_info()
    