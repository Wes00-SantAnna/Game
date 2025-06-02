from random import randint

class Calcular:
    def __init__(self: object, dificuldade: int) -> int:
        self.__dificuldade = dificuldade
        self.__valor1: int = self._gerar_valor
        self.__valor2: int = self._gerar_valor
        self.__resultado: int = self._gerar_valor
        self.__operacao: int = randint(1, 3)

    @property
    def dificauldade(self: object) -> int:
        return self.__dificuldade
    
    @property
    def valor1(self: object) -> int:
        return self.__valor1
    
    @property
    def valor2(self: object) -> int:
        return self.__valor2
    
    @property
    def operacao(self: object) -> int:
        return self.__operacap
    
    @property
    def resultado(self: object) -> int:
        return self.__resultado
    
    def __str__(self: object) -> str:
        op: str = ''
        if self.operacao == 1:
            op = 'Somar'
        elif self.operacao == 2:
            op = 'Diminuir'
        elif self.operacap == 3:
            op = 'Multiplicar'
        else:
            op = 'Operação desconhecida'
        return f'Valor 1: {self.valor1}\nValor2: {self.valor2}\nDificaldade: {self.dificuldade}\nOperação: {op}'

    @property
    def _gerar_valor(self: object) -> int:
        pass

    @property
    def _gerar_resultado(self: object) -> int:
        pass
    
    @property
    def validacao(self: object, resposta: int) -> bool:
        pass

    @property
    def mostrar_operacao(self: object) -> None:
        pass