from modelos.restaurante import Restaurante

Restaurante_praca = Restaurante('praca', 'gourmet')
Restaurante_praca = Restaurante('Mexican Food', 'mexicana')
Restaurante_praca = Restaurante('Japa', 'japonesa')

Restaurante_praca.alternar_estado()


def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()