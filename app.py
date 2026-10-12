from modelos.restaurante import Restaurante
from modelos.cardapio.babida import Bebida
from modelos.cardapio.prato import Prato

Restaurante_praca = Restaurante('praca', 'gourmet')
bebida_suco = Bebida('suco de melancia', 5, 'grande')
prato_paozinho = Prato('paozinho', 2.00, 'O melhor pao da cidade')

Restaurante_praca.receber_avaliacao('salomao', 10)



def main():
    print(bebida_suco)
    print(prato_paozinho)

if __name__ == '__main__':
    main()