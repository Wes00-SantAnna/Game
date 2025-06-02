from Models.calcular import Calcular

def main() -> None:
    pontos: int = 0
    jogar(pontos)

    def jogar(pontos: int) -> None:
        dificuldade: int = int(input('Informa o nível de dificauldade desejado [1, 2, 3 ou 4]: '))
        
        calc: Calcular = Calcular(dificuldade)

        print('Informar o resuldade para a seguinte operação: ')

        calc.mostrar_operacao()

        resultado: int = int(input())

        if calc.validacao(resultado):
            pontos = pontos + 1
            print(f'Total de pontos parcial: {pontos}')

        continuar: int = int(input('Deseja continuar no jogo [1 = sim, 0 = não]?'))
    
        if continuar:
            jogar(pontos)
        else:
            print(f'Tatal pontos final: {pontos}')
    if __name__ == "__main__":
        main()