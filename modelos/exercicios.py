# class Musica:

#     musicas = []

#     def __init__(self, nome, artista, duracao):
#         self.nome = nome
#         self.artista = artista
#         self.duracao = duracao
#         Musica.musicas.append(self)

#     def __str__(self):
#         return f'{self.nome} | {self.artista} | {self.duracao}'

# musica_queen = Musica('bohemian rhaosody', 'QUEEN', '30min')

# print(musica_queen)

class Carro:
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

    def __str__(self):
        return f'{self.modelo} | {self.cor} | {self.ano}'

carro_brasileiro = Carro('fusca', 'amarelo', '1997')
print(carro_brasileiro)


class Restaurante:
    def __init__(self, nome, categoria, recomendacao):
        self.nome = nome
        self.categoria = categoria
        self.ativo = True
        self.recomendacao = recomendacao
    def __str__(self):
        return f'{self.nome} | {self.categoria} | {self.recomendacao}'

bolo = Restaurante('bolaria', 'bolos', 'boa')

print(bolo)