# Exercício 6 - ft_count_harvest

## Descrição

Neste exercício você vai criar **duas funções** que fazem a mesma coisa de formas diferentes: contar os dias até a colheita, do dia 1 até um número informado pelo usuário, e ao final anunciar que é hora de colher.

- `ft_count_harvest_iterative` — usa um **laço de repetição** (`for`)
- `ft_count_harvest_recursive` — usa **recursão** (uma função que chama a si mesma)

As duas funções devem produzir **saídas idênticas**. A diferença está apenas na abordagem interna.

## Arquivos

- `ft_count_harvest_iterative.py`
- `ft_count_harvest_recursive.py`

## Assinaturas das funções

```python
def ft_count_harvest_iterative():

def ft_count_harvest_recursive():
```

## Exemplo de uso (ambas as funções)

```
Days until harvest: 5
Day 1
Day 2
Day 3
Day 4
Day 5
Harvest time!
```

## Funções autorizadas

### `input()`

Lê o número de dias digitado pelo usuário como string.

```python
harvest = input("Days until harvest: ")  # retorna "5" (texto)
```

### `int()`

Converte o texto retornado por `input()` em número inteiro para uso nos laços e comparações.

```python
harvest = int(input("Days until harvest: "))  # "5" → 5
```

### `print()`

Exibe cada dia e a mensagem final de colheita.

```python
print(f"Day {day}")    # exibe "Day 1", "Day 2", etc.
print("Harvest time!") # exibe ao final
```

### `range()`

A função `range()` gera uma **sequência de números inteiros** e é usada na versão iterativa para controlar o laço `for`.

```python
range(1, 6)  # gera: 1, 2, 3, 4, 5  (o limite superior é exclusivo)
```

Uso dentro do `for`:
```python
for day in range(1, harvest + 1):
    print(f"Day {day}")
```

- O primeiro argumento é o número **inicial** (inclusivo).
- O segundo argumento é o número **final** (exclusivo) — por isso usamos `harvest + 1` para incluir o último dia.

## Recursão (versão recursiva)

Na versão recursiva, a função resolve o problema **chamando a si mesma** com um valor diferente a cada vez, até atingir a condição de parada.

O subject aceita três abordagens para implementar a recursão:

**1. Função auxiliar aninhada (nested helper)**
```python
def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))

    def helper(current):
        if current > days:
            print("Harvest time!")
            return
        print(f"Day {current}")
        helper(current + 1)

    helper(1)
```

**2. Parâmetro com valor padrão**
```python
def ft_count_harvest_recursive(current=None, days=None):
    if current is None:
        days = int(input("Days until harvest: "))
        current = 1
    if current > days:
        print("Harvest time!")
        return
    print(f"Day {current}")
    ft_count_harvest_recursive(current + 1, days)
```

**3. Função auxiliar separada**
```python
def _helper(current, days):
    if current > days:
        print("Harvest time!")
        return
    print(f"Day {current}")
    _helper(current + 1, days)

def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))
    _helper(1, days)
```

Escolha a abordagem que fizer mais sentido para você.

## Observações

- Escreva **apenas** as funções, não um programa principal.
- As duas funções devem produzir saída **idêntica** para a mesma entrada.
- Não chame as funções diretamente nos arquivos.
- Não escreva código fora das funções.
