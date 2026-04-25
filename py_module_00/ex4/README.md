# Exercício 4 - ft_plant_age

## Descrição

Neste exercício você vai criar a função `ft_plant_age`, que pergunta a idade de uma planta em dias e informa se ela já está pronta para a colheita ou se ainda precisa de mais tempo para crescer.

Este exercício introduz o uso de **estruturas condicionais** (`if`/`else`) em Python, permitindo que o programa tome decisões com base em um valor lido do usuário.

## Arquivo

`ft_plant_age.py`

## Assinatura da função

```python
def ft_plant_age():
```

## Exemplos de uso

```
Enter plant age in days: 75
Plant is ready to harvest!
```

```
Enter plant age in days: 45
Plant needs more time to grow.
```

## Lógica de decisão

| Condição            | Mensagem exibida                   |
|---------------------|------------------------------------|
| idade **> 60** dias | `Plant is ready to harvest!`       |
| idade **≤ 60** dias | `Plant needs more time to grow.`   |

> A condição é **estritamente maior que 60**. Uma planta com exatamente 60 dias **não** está pronta.

## Funções autorizadas

### `input()`

A função `input()` lê o valor digitado pelo usuário e o retorna como string.

```python
plant = input("Enter plant age in days: ")  # retorna "75" (texto)
```

### `int()`

A função `int()` converte o texto retornado por `input()` em número inteiro, para que possamos comparar numericamente.

```python
plant = int(input("Enter plant age in days: "))  # "75" → 75
```

Sem essa conversão, a comparação `plant > 60` não funcionaria corretamente, pois comparar texto com número em Python produz erro ou resultado inesperado.

### `print()`

A função `print()` exibe a mensagem correspondente ao resultado da verificação.

```python
if plant > 60:
    print("Plant is ready to harvest!")
else:
    print("Plant needs more time to grow.")
```

A estrutura `if`/`else` avalia a condição e executa apenas o bloco correspondente:
- Se a condição for **verdadeira** (`True`), o bloco do `if` é executado.
- Se for **falsa** (`False`), o bloco do `else` é executado.

## Observações

- Escreva **apenas** a função, não um programa principal.
- O limite é **estritamente maior que 60** — exatamente 60 dias ainda não está pronto.
- Não chame a função diretamente no arquivo.
- Não escreva código fora da função.
