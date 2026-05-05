# Exercise 6 — Data Alchemist

**Arquivo:** `ft_data_alchemist.py`

---

## Funções autorizadas e explicações

### `import random` / `random.*`

O módulo `random` é usado para gerar scores aleatórios para os jogadores:

- **`random.randint(a, b)`** — retorna um inteiro aleatório entre `a` e `b` (inclusive). Usado dentro da compreensão de dicionário para gerar as pontuações.

```python
score = random.randint(50, 1000)   # ex: 437
```

---

### `print()`

Exibe as listas e dicionários gerados no terminal.

```python
print(f"Initial list of players: {initial_players}")
print(f"Score dict: {scores}")
print(f"High scores: {high_scores}")
```

---

### `len()`

Retorna o número de elementos de uma coleção. Usado para calcular a média dividindo a soma pelo número de jogadores.

```python
nomes = ['Alice', 'Bob', 'Charlie']
print(len(nomes))   # 3

media = total / len(scores)
```

---

### `sum()`

Retorna a soma de todos os valores de um iterável. Usado para somar todos os scores e calcular a média.

```python
scores = {'Alice': 263, 'Bob': 666, 'Charlie': 907}
total = sum(scores.values())   # 1836
```

---

### `round()`

Arredonda um número para um número específico de casas decimais. Usado para exibir a média com 2 casas decimais.

```python
round(410.111, 2)   # 410.11
```

---

## Conceito central: Compreensões (*Comprehensions*)

Compreensões são uma sintaxe elegante e concisa para criar listas e dicionários a partir de iteráveis. Cada compreensão fica em **uma única linha**.

---

### List Comprehension — capitalizar todos os nomes

Cria uma nova lista aplicando uma operação a cada elemento da lista original.

```python
initial = ['Alice', 'bob', 'Charlie', 'dylan']

# Forma tradicional (com loop):
capitalizados = []
for name in initial:
    capitalizados.append(name.capitalize())

# Com list comprehension (equivalente):
capitalizados = [name.capitalize() for name in initial]
# ['Alice', 'Bob', 'Charlie', 'Dylan']
```

---

### List Comprehension com filtro — apenas os já capitalizados

Adiciona uma condição `if` para filtrar elementos.

```python
# str.istitle() retorna True se a primeira letra é maiúscula
# e as demais são minúsculas
originally_cap = [name for name in initial if name.istitle()]
# ['Alice', 'Charlie']
```

---

### Dict Comprehension — criar o dicionário de scores

Cria um dicionário de forma compacta, mapeando cada nome a um score aleatório.

```python
all_capitalized = ['Alice', 'Bob', 'Charlie', 'Dylan']

# Forma tradicional:
scores = {}
for name in all_capitalized:
    scores[name] = random.randint(50, 1000)

# Com dict comprehension (equivalente):
scores = {name: random.randint(50, 1000) for name in all_capitalized}
# {'Alice': 263, 'Bob': 666, 'Charlie': 907, 'Dylan': 170}
```

---

### Dict Comprehension com filtro — apenas os high scores

Filtra o dicionário mantendo apenas os jogadores com score acima da média.

```python
average = sum(scores.values()) / len(scores)

# Dict comprehension com condição:
high_scores = {name: score for name, score in scores.items()
               if score > average}
# {'Bob': 666, 'Charlie': 907}
```

---

## Fluxo do programa

1. Define a lista inicial de jogadores (mistura de capitalizados e não capitalizados).
2. Usa **list comprehension** para criar uma nova lista com todos os nomes capitalizados.
3. Usa **list comprehension com filtro** para criar uma lista só com os nomes que já estavam capitalizados originalmente.
4. Usa **dict comprehension** para criar o dicionário de scores aleatórios a partir da lista totalmente capitalizada.
5. Calcula a média com `sum()`, `len()` e `round()`.
6. Usa **dict comprehension com filtro** para criar o dicionário de high scores (acima da média).
