# Exercise 4 — Inventory Master

**Arquivo:** `ft_inventory_system.py`

---

## Funções autorizadas e explicações

### `import sys` / `sys.argv`

Permite acessar os argumentos passados pela linha de comando. Cada argumento representa um item do inventário no formato `<nome>:<quantidade>`.

```python
import sys
args = sys.argv[1:]
# Executando: python3 ft_inventory_system.py sword:1 potion:5
# args == ['sword:1', 'potion:5']
```

---

### `len()`

Retorna o número de elementos de uma sequência. Usado para controlar loops e contar itens.

```python
item_list = ['sword', 'potion', 'shield']
print(len(item_list))   # 3
```

---

### `print()`

Exibe os dados do inventário no terminal de forma formatada.

```python
print(f"Got inventory: {inventory}")
print(f"Total quantity of items: {total_quantity}")
```

---

### `sum()`

Retorna a soma de todos os valores de um iterável. Usado para calcular a quantidade total de itens no inventário.

```python
inventory = {'sword': 1, 'potion': 5, 'shield': 2}
total = sum(inventory.values())   # 8
```

---

### `list()`

Converte um iterável em uma **lista**. Usado para transformar as chaves do dicionário em uma lista indexável, permitindo acesso por posição.

```python
inventory = {'sword': 1, 'potion': 5}
item_list = list(inventory.keys())   # ['sword', 'potion']
primeiro = item_list[0]              # 'sword'
```

---

### `round()`

Arredonda um número para um dado número de casas decimais. Usado para exibir o percentual de cada item com uma casa decimal.

```python
round(8.333333, 1)   # 8.3
round(41.666666, 1)  # 41.7
```

---

### `dict.keys()`

Retorna uma **visão** de todas as chaves do dicionário (os nomes dos itens).

```python
inventory = {'sword': 1, 'potion': 5}
print(inventory.keys())   # dict_keys(['sword', 'potion'])

# Convertida para lista para acesso por índice:
item_list = list(inventory.keys())
```

---

### `dict.values()`

Retorna uma **visão** de todos os valores do dicionário (as quantidades).

```python
inventory = {'sword': 1, 'potion': 5}
print(inventory.values())   # dict_values([1, 5])

total = sum(inventory.values())   # 6
```

---

### `dict.update()`

Adiciona ou atualiza **um ou mais pares chave-valor** em um dicionário existente. Usado para inserir um novo item ao final do inventário.

```python
inventory = {'sword': 1, 'potion': 5}
inventory.update({'magic_item': 1})
print(inventory)
# {'sword': 1, 'potion': 5, 'magic_item': 1}
```

Também pode ser usado para atualizar o valor de uma chave já existente:

```python
inventory.update({'potion': 10})   # atualiza quantidade de potion
```

---

## Fluxo do programa

1. Lê os argumentos de `sys.argv[1:]`.
2. Para cada argumento, valida o formato `nome:quantidade`.
   - Parâmetros com sintaxe inválida são descartados com mensagem de erro.
   - Itens duplicados são descartados com aviso.
   - Quantidades não numéricas geram erro e são descartadas.
3. Exibe o inventário final (`dict`).
4. Cria e exibe a lista de nomes com `list(dict.keys())`.
5. Calcula o total com `sum(dict.values())`.
6. Calcula e exibe o percentual de cada item.
7. Encontra o item mais e menos abundante.
8. Adiciona um novo item com `dict.update()` e exibe o inventário atualizado.
