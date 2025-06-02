# Jogo de Cálculo

Este é um jogo simples de matemática desenvolvido em Python. O objetivo é desafiar o jogador com operações matemáticas de diferentes níveis de dificuldade. O jogador informa o nível desejado, responde às perguntas geradas e acumula pontos a cada resposta correta.

## Funcionalidades

- Geração aleatória de operações matemáticas.
- Quatro níveis de dificuldade.
- Operações suportadas: adição, subtração, multiplicação e divisão inteira.
- Sistema de pontuação.
- Repetição do jogo com pontuação acumulada.

## Estrutura do Projeto

```
.
├── main.py                 # Arquivo principal que executa o jogo
└── Models/
    └── calcular.py         # Classe responsável por gerar e validar os cálculos
```

## Requisitos

- Python 3.6 ou superior

## Como executar

1. Clone o repositório:
    
    ```bash
    git clone https://github.com/Wes00-SantAnna/Game.git
    cd nome-do-repositorio
    ```
    
2. Execute o jogo:
    
    ```bash
    python main.py
    ```
    
3. Siga as instruções no terminal para jogar.

## Exemplo de uso

Ao iniciar, você será solicitado a escolher um nível de dificuldade de 1 a 4. Em seguida, o jogo apresentará uma operação matemática. Digite o resultado e acumule pontos com cada resposta correta. Você pode optar por continuar jogando ou sair a qualquer momento.