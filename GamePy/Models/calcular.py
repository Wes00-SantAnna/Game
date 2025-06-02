from random import randint

class Calcular:
    def __init__(self, dificuldade: int) -> None:
        self.__dificuldade = dificuldade
        self.__valor1 = self._gerar_valor()
        self.__valor2 = self._gerar_valor()
        self.__operacao = randint(1, 3)
        self.__resultado = self._gerar_resultado()

    def _gerar_valor(self) -> int:
        if self.__dificuldade == 1:
            return randint(0,10)
        elif self.__dificuldade == 2:
            return randint(0,100)
        elif self.__dificuldade == 3:
            return randint(0,10000)
        elif self.__dificuldade == 4:
            return randint(0,100000)
        else:
            print('Operação inválida')

    def _gerar_resultado(self) -> int:
        if self.__operacao == 1:
            return self.__valor1 + self.__valor2
        elif self.__operacao == 2:
            return self.__valor1 - self.__valor2
        elif self.__operacao == 3: 
            return self.__valor1 * self.__valor2
        else:
            print("A operação selecionada não está disponíve")

    def mostrar_operacao(self) -> None:
      pass

    def validacao(self, resposta: int) -> bool:
        pass

    def __str__(self) -> str:
        pass