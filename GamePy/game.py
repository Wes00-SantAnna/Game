from Models.calcular import Calcular

def jogar(pontos: int) -> None:
    dificuldade: int = int(input('Informe o nível de dificuldade desejado [1, 2, 3 ou 4]: '))
    
    calc: Calcular = Calcular(dificuldade)

    print('Informe o resultado para a seguinte operação: ')
    calc.mostrar_operacao()

    try:
        resposta: int = int(input())
    except ValueError:
        print("Resposta inválida. Digite um número inteiro.")
        return jogar(pontos)

    if calc.validacao(resposta):
        pontos += 1
        print(f'✅ Resposta correta! Pontos: {pontos}')
    else:
        print(f'❌ Resposta incorreta. O resultado era {calc._Calcular__resultado}.')
        print(f'Pontos: {pontos}')

    continuar: int = int(input('Deseja continuar no jogo? [1 = sim, 0 = não]: '))
    if continuar:
        jogar(pontos)
    else:
        print(f'Total de pontos final: {pontos}')


def main() -> None:
    pontos: int = 0
    jogar(pontos)

if __name__ == "__main__":
    main()
