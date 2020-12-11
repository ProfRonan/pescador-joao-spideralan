"""Arquivo principal que será interpretado pelo interpretador."""


def main():
    """Função principal que será rodada quando o script for passado para o interpretador."""
    # COLOQUE SEU CÓDIGO AQUI
    peso = float(input('Digite o peso total dos peixes: '))
    exc = max(0, peso-50)
    multa = exc * 4
    print(f'O peixe pescado tem {peso}kg, a multa devida é R$ {multa:.2f}.')


if __name__ == '__main__':
    main()
