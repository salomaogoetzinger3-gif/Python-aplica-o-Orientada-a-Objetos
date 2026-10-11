from modelos.restaurante import Restaurante

Restaurante_praca = Restaurante('praca', 'gourmet')

Restaurante_praca.receber_avaliacao('salomao', 10)
Restaurante_praca.receber_avaliacao('salomao', 3)
Restaurante_praca.receber_avaliacao('salomao', 3.5)
Restaurante_praca.receber_avaliacao('salomao', 2)


def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()