# Exercise 0 — Lambda Sanctum

## Arquivo: `lambda_spells.py`

Este exercício foca no domínio das **funções anônimas (lambda)** e nos padrões funcionais de transformação de dados com `map`, `filter` e `sorted`.

---

## Funções autorizadas e explicações

### `lambda`

Uma expressão `lambda` cria uma função anônima de forma concisa, sem usar `def`. É ideal para operações simples e pontuais, especialmente como argumento de outras funções.

```python
# Sintaxe
lambda argumentos: expressão

# Exemplo
dobrar = lambda x: x * 2
dobrar(5)  # 10
```

**Quando usar lambda vs `def`:**
- Use `lambda` para funções curtas e de uso único (ex: chave de ordenação, filtro simples).
- Use `def` quando a função tiver lógica complexa, precisar de docstring ou for reutilizada em vários lugares.

---

### `sorted(iterable, key=..., reverse=...)`

Retorna uma **nova lista ordenada** a partir de qualquer iterável. Não modifica o original.

```python
sorted([3, 1, 2])                        # [1, 2, 3]
sorted([3, 1, 2], reverse=True)          # [3, 2, 1]
sorted(lista, key=lambda x: x["power"]) # ordena por campo 'power'
```

- `key`: função aplicada a cada elemento para determinar a chave de comparação.
- `reverse=True`: ordena em ordem decrescente.

---

### `filter(function, iterable)`

Retorna um iterador com os elementos do iterável para os quais a função retorna `True`.

```python
numeros = [1, 2, 3, 4, 5]
pares = list(filter(lambda x: x % 2 == 0, numeros))
# [2, 4]
```

É equivalente a uma list comprehension com condição: `[x for x in numeros if x % 2 == 0]`.

---

### `map(function, iterable)`

Aplica uma função a **cada elemento** de um iterável e retorna um iterador com os resultados.

```python
nomes = ["fireball", "heal"]
formatados = list(map(lambda s: "*" + s + "*", nomes))
# ['*fireball*', '*heal*']
```

---

### `max(iterable, key=...)` e `min(iterable, key=...)`

Retornam, respectivamente, o maior e o menor elemento de um iterável. O parâmetro `key` permite definir o critério de comparação.

```python
mages = [{"name": "A", "power": 95}, {"name": "B", "power": 60}]
max(mages, key=lambda m: m["power"])  # {"name": "A", "power": 95}
min(mages, key=lambda m: m["power"])  # {"name": "B", "power": 60}
```

---

### `sum(iterable)`

Retorna a soma de todos os elementos de um iterável numérico.

```python
sum([10, 20, 30])  # 60
sum(map(lambda m: m["power"], mages))  # soma os poderes de todos os mages
```

---

### `round(number, ndigits)`

Arredonda um número para a quantidade especificada de casas decimais.

```python
round(76.6666, 2)  # 76.67
```

---

### `len(iterable)`

Retorna o número de elementos em um iterável (lista, string, dict, etc.).

```python
len([1, 2, 3])  # 3
```

---

## Resumo das funções implementadas

| Função | Descrição |
|---|---|
| `artifact_sorter(artifacts)` | Ordena artefatos por poder (decrescente) usando `sorted` + `lambda` |
| `power_filter(mages, min_power)` | Filtra magos com poder mínimo usando `filter` + `lambda` |
| `spell_transformer(spells)` | Adiciona prefixo/sufixo `*` usando `map` + `lambda` |
| `mage_stats(mages)` | Calcula max, min e média de poder usando `max`, `min`, `sum`, `len` e `lambda` |
