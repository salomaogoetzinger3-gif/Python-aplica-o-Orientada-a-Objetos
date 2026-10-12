from modelos.restaurante import Restaurante
from modelos.cardapio.babida import Bebida
from modelos.cardapio.prato import Prato

Restaurante_praca = Restaurante('praca', 'gourmet')
bebida_suco = Bebida('suco de melancia', 5, 'grande')
bebida_suco.aplicar_desconto()
prato_paozinho = Prato('paozinho', 2.00, 'O melhor pao da cidade')
prato_paozinho.aplicar_desconto()
Restaurante_praca.adicionar_no_cardapio(bebida_suco)
Restaurante_praca.adicionar_no_cardapio(prato_paozinho)

Restaurante_praca.receber_avaliacao('salomao', 10)



def main():
    Restaurante_praca.exibir_cardapio

if __name__ == '__main__':
    main()