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

# class Livro:

#     livros = []

#     def __init__(self, titulo = '', autor = '', ano_publicacao = 0, disponivel = True):
#         self._titulo = titulo
#         self._autor = autor
#         self._ano_publicacao = ano_publicacao
#         self._disponivel = disponivel
#         Livro.livros.append(self) #adiciona o __init__ cada vez que é criado

#     def __str__(self):
#             return f'{self._titulo} | {self._autor} | {self._ano_publicacao} | {self._disponivel}' #retorna algo legivel

#     @classmethod
#     def exibir(cls):
#         for livro in cls.livros:
#               print(f'{livro._titulo.ljust(25)} | {livro._autor.ljust(25)} | {str(livro._ano_publicacao).ljust(25)} | {livro.ativo}')
#               # mostra todos os livros dentro de livros = []
#     @property
#     def ativo(self):
#         return 'Está disponivel' if self._disponivel else 'Não está disponivel' # troca o true e o false

#     @property
#     def emprestarLivro(self):
#         return 'Esta disponivel' if self._disponivel == True else 'Não esta disponivel'
    
#     def verificar_disponibilidade(self):
#          if self._disponivel == False:
#               return print('Livro não esta disponivel')
#          else:
#               return print('Livro disponivel') #verifica se o livro esta disponivel ou não
    

# livro1 = Livro('O Hobbit', 'J.J.R Tolkien', '1958', True)
# livro2 = Livro('O Senhor dos anéis', 'J.J.R Tolkien', '1960', True)


# livro1.exibir()


# class Banco:
#     def __init__(self, nome, endereco):
#         self._nome = nome
#         self._endereco = endereco

# class Agencia(Banco):
#     def __init__(self, nome, endereco, numero):
#         super().__init__(nome, endereco)
    

# class Veiculo:
#     def __init__(self, modelo, marca, estado):
#         self._modelo = modelo
#         self._marca = marca
#         self._estado = estado

#     def __str__(self):
#         return f' Modelo do veículo: {self._modelo}, Marca: {self._marca} e Estado: {self._estado}'

# class Carro(Veiculo):
#     def __init__(self, modelo, marca, estado, portas):
#         super().__init__(modelo, marca, estado)
#         self._portas = portas
#     def __str__(self):
#         return f'{super().__str__()}, com Nº de portas: {self._portas}'

# class Moto(Veiculo):
#     def __init__(self, modelo, marca, estado, tipo):
#         super().__init__(modelo, marca, estado)
#         self._tipo = tipo
#     def __str__(self):
#         return f'{super().__str__()}, a moto é do tipo: {self._tipo}'

# moto = Moto('Moto', 'Yamaha', 'Novo', 'Casual')

# print(moto)