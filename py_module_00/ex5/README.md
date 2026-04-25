# Exercício 5 - ft_water_reminder

## Descrição

Neste exercício você vai criar a função `ft_water_reminder`, que pergunta há quantos dias as plantas não são regadas e decide se é hora de regar ou se elas ainda estão bem.

Este exercício reforça o uso de **estruturas condicionais** (`if`/`else`) aplicadas a um contexto prático de cuidado com o jardim.

## Arquivo

`ft_water_reminder.py`

## Assinatura da função

```python
def ft_water_reminder():
```

## Exemplos de uso

```
Days since last watering: 4
Water the plants!
```

```
Days since last watering: 1
Plants are fine
```

## Lógica de decisão

| Condição          | Mensagem exibida      |
|-------------------|-----------------------|
| dias **> 2**      | `Water the plants!`   |
| dias **≤ 2**      | `Plants are fine`     |

> A condição é **estritamente maior que 2**. Com exatamente 2 dias sem regar, as plantas ainda estão bem.

## Funções autorizadas

### `input()`

A função `input()` lê o valor digitado pelo usuário e o retorna como string.

```python
reminder = input("Days since last watering: ")  # retorna "4" (texto)
```

O texto exibido entre parênteses funciona como instrução para o usuário, indicando o que deve ser digitado.

### `int()`

A função `int()` converte a string retornada por `input()` em número inteiro, necessário para a comparação numérica.

```python
reminder = int(input("Days since last watering: "))  # "4" → 4
```

Com o valor convertido, podemos comparar `reminder > 2` corretamente.

### `print()`

A função `print()` exibe a mensagem de aviso ou de tranquilidade, dependendo do resultado da condição.

```python
if reminder > 2:
    print("Water the plants!")
else:
    print("Plants are fine")
```

- Se faz **mais de 2 dias**, o programa alerta para regar as plantas.
- Caso contrário, informa que as plantas estão bem.

## Observações

- Escreva **apenas** a função, não um programa principal.
- O limite é **estritamente maior que 2** — exatamente 2 dias ainda está dentro do limite seguro.
- Não chame a função diretamente no arquivo.
- Não escreva código fora da função.
