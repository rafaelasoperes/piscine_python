# Exercise 3 — Ancient Library

## Arquivo: `functools_artifacts.py`

Este exercício explora o módulo `functools` e o módulo `operator`, que fornecem ferramentas poderosas para programação funcional em Python: redução, aplicação parcial, memoização e despacho por tipo.

---

## Módulos autorizados e explicações

### `functools`

Módulo da biblioteca padrão com utilitários de ordem superior para trabalhar com funções.

---

### `functools.reduce(function, iterable[, initializer])`

Aplica uma função de dois argumentos de forma **acumulativa** sobre os elementos de um iterável, reduzindo-o a um único valor.

```python
import functools

functools.reduce(lambda acc, x: acc + x, [1, 2, 3, 4])
# Passo a passo: ((1+2)+3)+4 = 10
```

Diferente de `map` e `filter`, `reduce` **não** é uma built-in — precisa ser importada de `functools`. É útil para agregações como soma, produto, concatenação ou encontrar máximo/mínimo de forma genérica.

---

### `functools.partial(func, *args, **kwargs)`

Cria uma nova função com alguns argumentos da função original **pré-preenchidos**.

```python
from functools import partial

def encantar(poder: int, elemento: str, alvo: str) -> str:
    return f"Encantamento {elemento} em {alvo} com poder {poder}"

fogo = partial(encantar, poder=50, elemento="fogo")
fogo(alvo="Espada")  # "Encantamento fogo em Espada com poder 50"
```

`partial` é uma forma de **especializar** funções genéricas sem reescrevê-las, criando versões com parte dos argumentos fixos.

---

### `functools.lru_cache(maxsize=...)`

Decorador que implementa **memoização** (cache de resultados). Quando uma função decorada é chamada com os mesmos argumentos, o resultado é retornado do cache sem recalcular.

```python
import functools

@functools.lru_cache(maxsize=None)
def fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
```

- `maxsize=None`: cache ilimitado.
- `maxsize=128`: guarda os 128 resultados mais recentes (LRU = Least Recently Used).
- Verificar o cache: `fibonacci.cache_info()` retorna hits, misses, maxsize e currsize.

**Benefício de performance:** Fibonacci sem cache tem complexidade O(2ⁿ). Com `lru_cache`, cada valor é calculado apenas uma vez — complexidade O(n).

---

### `functools.singledispatch`

Decorador que cria uma **função genérica** com despacho baseado no tipo do primeiro argumento.

```python
import functools

@functools.singledispatch
def processar(valor):
    return f"Tipo desconhecido: {type(valor)}"

@processar.register(int)
def _(valor: int) -> str:
    return f"Inteiro: {valor}"

@processar.register(str)
def _(valor: str) -> str:
    return f"String: {valor}"

processar(42)       # "Inteiro: 42"
processar("hello")  # "String: hello"
processar(3.14)     # "Tipo desconhecido: <class 'float'>"
```

Permite escrever código polimórfico sem `if/elif` baseado em `type()`.

---

### `operator`

Módulo que fornece funções equivalentes aos operadores do Python (`+`, `*`, `>`, etc.), permitindo usá-los como objetos de primeira classe.

```python
import operator

operator.add(3, 4)   # equivale a 3 + 4 → 7
operator.mul(3, 4)   # equivale a 3 * 4 → 12
```

É especialmente útil com `functools.reduce`, onde é necessário passar uma função como argumento:

```python
functools.reduce(operator.add, [1, 2, 3, 4])   # 10
functools.reduce(operator.mul, [1, 2, 3, 4])   # 24
```

---

## Resumo das funções implementadas

| Função | Ferramenta principal | Descrição |
|---|---|---|
| `spell_reducer(spells, operation)` | `functools.reduce` + `operator` | Reduz uma lista de poderes com operação configurável (add, multiply, max, min) |
| `partial_enchanter(base_enchantment)` | `functools.partial` | Cria 3 versões especializadas de um encantamento base com poder e elemento pré-definidos |
| `memoized_fibonacci(n)` | `functools.lru_cache` | Calcula Fibonacci com cache para evitar recálculos exponenciais |
| `spell_dispatcher()` | `functools.singledispatch` | Retorna uma função que se comporta diferente conforme o tipo do argumento (int, str, list) |
