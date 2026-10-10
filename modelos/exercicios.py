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

# class Carro:
#     def __init__(self, modelo, cor, ano):
#         self.modelo = modelo
#         self.cor = cor
#         self.ano = ano

#     def __str__(self):
#         return f'{self.modelo} | {self.cor} | {self.ano}'

# carro_brasileiro = Carro('fusca', 'amarelo', '1997')
# print(carro_brasileiro)


# class Restaurante:
#     def __init__(self, nome, categoria, recomendacao):
#         self.nome = nome
#         self.categoria = categoria
#         self.ativo = True
#         self.recomendacao = recomendacao
#     def __str__(self):
#         return f'{self.nome} | {self.categoria} | {self.recomendacao}'

# bolo = Restaurante('bolaria', 'bolos', 'boa')

# print(bolo)

# class Pessoa:
#     def __init__(self, nome='', idade=0, profissao=''):
#         self.nome = nome
#         self.idade = idade
#         self.profissao = profissao
#     def __str__(self):
#         return f'Seu nome {self.nome} - sua idade {self.idade} e sua profissao {self.profissao}'
#     @property
#     def saudacao(self):
#         if self.profissao:
#             return f'olá, sou {self.nome} anos, Trabalho com {self.profissao} '
#         else:
#             return f'Olá, sou {self.nome}'
#     def aniversario(self):
#         self.idade += 1

# class ContaBancaria:
#     def __init__(self, titular='', saldo = 0, ativo = False):
#         self.titular = titular
#         self.saldo = saldo
#         self.ativo = ativo
#     def __str__(self):
#         return f'Olá,{self.titular} seu saldo bancario é de: R${self.saldo}'

#     @property
#     def ativar_conta(self):
#         if self.ativo == True:
#             return 'Sua conta esta ativa'
#         else:
#             return ' Sua conta esta desativada'

# class ClienteBanco:
#     def __init__(self, nome = '', conta = 0, agencia = 0, cpf = 0, rg = 0):
#         self.nome = nome
#         self.conta = conta
#         self.agencia = agencia
#         self.cpf = cpf
#         self.rg = rg
        

# saldoMeu = ContaBancaria('salomao', 200, True)

# print(saldoMeu)