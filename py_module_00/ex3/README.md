# Exercício 3 - ft_harvest_total

## Descrição

Um jardineiro colheu vegetais em três dias diferentes. Neste exercício você vai criar a função `ft_harvest_total`, que pergunta o peso colhido em cada dia e calcula o total da colheita.

Este exercício reforça o uso de **múltiplas variáveis**, **conversão de tipos** e **operações aritméticas** em Python.

## Arquivo

`ft_harvest_total.py`

## Assinatura da função

```python
def ft_harvest_total():
```

## Exemplo de uso

```
Day 1 harvest: 5
Day 2 harvest: 8
Day 3 harvest: 3
Total harvest: 16
```

## Funções autorizadas

### `input()`

A função `input()` lê dados digitados pelo usuário no terminal e os retorna como **string** (`str`).

```python
day1 = input("Day 1 harvest: ")  # retorna "5" (texto)
```

Cada chamada a `input()` pausa o programa e aguarda o usuário digitar um valor e pressionar Enter. Neste exercício, `input()` é chamada três vezes — uma para cada dia de colheita.

### `int()`

A função `int()` converte o texto retornado por `input()` em **número inteiro**, permitindo realizar operações matemáticas com os valores.

```python
day1 = int(input("Day 1 harvest: "))  # "5"  → 5
day2 = int(input("Day 2 harvest: "))  # "8"  → 8
day3 = int(input("Day 3 harvest: "))  # "3"  → 3
total = day1 + day2 + day3            # 5 + 8 + 3 = 16
```

Sem a conversão com `int()`, o operador `+` concatenaria os textos ao invés de somá-los:
```python
"5" + "8" + "3"  # resultado: "583" ← errado!
5   + 8   + 3    # resultado: 16    ← correto!
```

### `print()`

A função `print()` exibe o total calculado na tela.

```python
print(f"Total harvest: {total}")  # exibe "Total harvest: 16"
```

## Observações

- Escreva **apenas** a função, não um programa principal.
- Cada valor de colheita deve ser lido como inteiro.
- O total é a **soma dos três dias**.
- Não chame a função diretamente no arquivo.
- Não escreva código fora da função.
