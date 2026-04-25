# Exercício 2 - ft_plot_area

## Descrição

Um jardim comunitário precisa saber a área de um canteiro retangular. Neste exercício você vai criar a função `ft_plot_area`, que lê o comprimento e a largura de um canteiro e calcula sua área.

Este exercício introduz a **conversão de tipos** em Python: o valor lido pelo `input()` é sempre texto, mas para fazer cálculos matemáticos precisamos converter esse texto para número inteiro com `int()`.

## Arquivo

`ft_plot_area.py`

## Assinatura da função

```python
def ft_plot_area():
```

## Exemplo de uso

```
Enter length: 5
Enter width: 3
Plot area: 15
```

## Funções autorizadas

### `input()`

A função `input()` lê dados digitados pelo usuário no terminal e os retorna como **string** (`str`).

```python
length = input("Enter length: ")  # retorna "5" (texto), não 5 (número)
```

Lembre-se: mesmo que o usuário digite um número, `input()` sempre retorna texto. Por isso precisamos da conversão com `int()`.

### `int()`

A função `int()` **converte um valor para número inteiro**. É muito utilizada em conjunto com `input()` quando esperamos que o usuário digite um número.

```python
length = int(input("Enter length: "))  # converte "5" → 5
width  = int(input("Enter width: "))   # converte "3" → 3
area   = length * width                # agora podemos fazer a multiplicação: 15
```

Características importantes:

- Converte strings numéricas (`"5"`, `"100"`) em inteiros (`5`, `100`).
- Também converte floats para inteiros, descartando a parte decimal: `int(3.9)` → `3`.
- Gera um erro se o valor não puder ser convertido (ex: `int("abc")`), mas você não precisa tratar esse caso neste exercício.

### `print()`

A função `print()` exibe o resultado na tela. Neste exercício ela é usada para mostrar a área calculada.

```python
print(f"Plot area: {area}")  # exibe "Plot area: 15"
```

## Observações

- Escreva **apenas** a função, não um programa principal.
- Comprimento e largura devem ser lidos como inteiros.
- A área é calculada multiplicando comprimento por largura.
- Não chame a função diretamente no arquivo.
- Não escreva código fora da função.
