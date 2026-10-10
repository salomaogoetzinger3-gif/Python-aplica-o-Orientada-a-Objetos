from modelos.restaurante import Restaurante

Restaurante_praca = Restaurante('praca', 'gourmet')

Restaurante_praca.receber_avaliacao('salomao', 10)


def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()