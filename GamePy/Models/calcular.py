from random import randint

class Calcular:
    def __init__(self, dificuldade: int) -> None:
        self.__dificuldade = dificuldade
        self.__valor1 = self._gerar_valor()
        self.__valor2 = self._gerar_valor_nao_zero()
        self.__operacao = randint(1, 5)
        self.__resultado = self._gerar_resultado()

    def _gerar_valor(self) -> int:
        if self.__dificuldade == 1:
            return randint(1, 10)
        elif self.__dificuldade == 2:
            return randint(10, 100)
        elif self.__dificuldade == 3:
            return randint(100, 1000)
        elif self.__dificuldade == 4:
            return randint(1000, 10000)
        else:
            print('Operação inválida')

    def _gerar_resultado(self) -> int:
        if self.__operacao == 1:
            return self.__valor1 + self.__valor2
        elif self.__operacao == 2:
            return self.__valor1 - self.__valor2
        elif self.__operacao == 3:
            return self.__valor1 * self.__valor2
        elif self.__operacao == 4:
            return self.__valor1 // self.__valor2

    def mostrar_operacao(self) -> None:
        simbolos = {1: '+', 2: '-', 3: '*', 4: '/'}
        simbolo = simbolos.get(self.__operacao, '?')
        print(f'{self.__valor1} {simbolo} {self.__valor2} = ?')

    def validacao(self, resposta: int) -> bool:
        return resposta == self.__resultado

    def __str__(self) -> str:
        nomes = {1: 'Somar', 2: 'Diminuir', 3: 'Multiplicar', 4: 'Dividir'}
        nome_op = nomes.get(self.__operacao, 'Desconhecida')
        return f'Valor 1: {self.__valor1}\nValor 2: {self.__valor2}\nDificuldade: {self.__dificuldade}\nOperação: {nome_op}'