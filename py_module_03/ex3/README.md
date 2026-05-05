# Exercise 3 — Achievement Hunter

**Arquivo:** `ft_achievement_tracker.py`

---

## Funções autorizadas e explicações

### `len()`

Retorna o número de elementos de uma coleção. Usado para contar jogadores e controlar loops.

```python
nomes = ("Alice", "Bob", "Charlie", "Dylan")
print(len(nomes))   # 4
```

---

### `print()`

Exibe valores e conjuntos no terminal.

```python
print(f"Player Alice: {players['Alice']}")
print(f"Common achievements: {common}")
```

---

### `import random` / `random.*`

O módulo `random` fornece funções para geração de valores aleatórios:

- **`random.randint(a, b)`** — retorna um inteiro aleatório entre `a` e `b` (inclusive).

```python
quantidade = random.randint(5, 10)   # ex: 7
```

- **`random.sample(population, k)`** — retorna uma lista com `k` elementos **únicos** escolhidos aleatoriamente da sequência `population`, sem repetição.

```python
pool = ("A", "B", "C", "D", "E")
escolhidos = random.sample(pool, 3)   # ex: ['C', 'A', 'E']
```

Juntos, eles criam um conjunto de conquistas aleatórias para cada jogador.

---

### `set()`

Cria um **conjunto** — uma coleção **não ordenada** de elementos **únicos**. Conjuntos são ideais para operações matemáticas de teoria dos conjuntos.

```python
s = set(["A", "B", "A", "C"])   # {'A', 'B', 'C'}  → sem duplicatas
s = set()                        # conjunto vazio
```

---

### `set.union()`

Retorna um novo conjunto com **todos os elementos** presentes em qualquer um dos conjuntos (equivalente ao operador `|`). Usado para acumular todas as conquistas distintas entre os jogadores.

```python
a = {"Boss Slayer", "Survivor"}
b = {"Survivor", "Speed Runner"}
print(a.union(b))   # {'Boss Slayer', 'Survivor', 'Speed Runner'}
```

---

### `set.intersection()`

Retorna um novo conjunto com apenas os elementos **presentes em todos** os conjuntos (equivalente ao operador `&`). Usado para encontrar conquistas que todos os jogadores têm.

```python
a = {"Boss Slayer", "Survivor", "Untouchable"}
b = {"Survivor", "Speed Runner", "Untouchable"}
print(a.intersection(b))   # {'Survivor', 'Untouchable'}
```

---

### `set.difference()`

Retorna um novo conjunto com os elementos que estão no primeiro conjunto mas **não estão no segundo** (equivalente ao operador `-`). Usado para encontrar conquistas exclusivas de um jogador ou conquistas que estão faltando.

```python
todos = {"A", "B", "C", "D"}
alice = {"A", "C"}

# Conquistas que faltam para Alice:
print(todos.difference(alice))   # {'B', 'D'}

# Conquistas exclusivas de Alice vs todos os outros:
outros = {"B", "C", "D"}
print(alice.difference(outros))  # {'A'}
```

---

## Fluxo do programa

1. Gera conjuntos de conquistas aleatórias para cada jogador com `gen_player_achievements()`.
2. Exibe as conquistas de cada jogador.
3. Usa `union()` para encontrar todas as conquistas distintas entre todos.
4. Usa `intersection()` para encontrar as conquistas que **todos** possuem em comum.
5. Para cada jogador, usa `difference()` para encontrar conquistas **exclusivas** dele.
6. Para cada jogador, usa `difference()` para listar as conquistas que ele **ainda não tem**.

---

## Por que `set()` e não `{}`?

Em Python, `{}` cria um **dicionário vazio**, não um conjunto. Para criar um conjunto vazio, é obrigatório usar `set()`. Um conjunto não vazio pode ser criado com `{"A", "B"}`.
