# Exercise 5 — Stream Wizard

**Arquivo:** `ft_data_stream.py`

---

## Funções autorizadas e explicações

### `next()`

`next()` avança um **gerador** (ou qualquer iterador) e retorna o próximo valor produzido por ele. Cada chamada a `next()` executa o gerador até o próximo `yield`.

```python
gen = gen_event()
evento = next(gen)   # ex: ('alice', 'run')
evento = next(gen)   # ex: ('bob', 'sleep')
```

Se o gerador for infinito (como `gen_event()`), `next()` pode ser chamado indefinidamente. Se o gerador for finito e já tiver terminado, `next()` lança `StopIteration`.

---

### `range()`

Gera uma sequência de números inteiros, muito usada em loops `for`. Recebe até três argumentos: `start`, `stop` e `step`.

```python
range(5)        # 0, 1, 2, 3, 4
range(1, 6)     # 1, 2, 3, 4, 5
range(0, 10, 2) # 0, 2, 4, 6, 8

# Usado para repetir 1000 vezes:
for i in range(1000):
    player, action = next(meu_gerador)
    print(f"Event {i}: Player {player} did action {action}")
```

---

### `len()`

Retorna o número de elementos de uma sequência. Usado para controlar o loop de consumo de eventos.

```python
eventos = [('alice', 'run'), ('bob', 'sleep')]
print(len(eventos))   # 2
```

---

### `print()`

Exibe os eventos e os estados das listas no terminal.

```python
print(f"Event {i}: Player {player} did action {action}")
print(f"Built list of 10 events: {eventos_estaticos}")
```

---

### `import random` / `random.*`

O módulo `random` é usado tanto no gerador de eventos quanto no consumidor:

- **`random.choice(seq)`** — escolhe um elemento aleatório de uma sequência.

```python
players = ['alice', 'bob', 'charlie', 'dylan']
player = random.choice(players)   # ex: 'bob'
```

- **`random.randrange(stop)`** — retorna um índice aleatório entre `0` e `stop - 1`. Usado para escolher a posição de um evento a ser consumido.

```python
idx = random.randrange(5)   # 0, 1, 2, 3 ou 4
```

---

### `import typing` / `typing.Generator`

O módulo `typing` fornece suporte a **anotações de tipos** mais expressivas. `typing.Generator` é usado para indicar que uma função é um gerador e especificar os tipos que ela produz.

```python
from typing import Generator

def gen_event() -> Generator[tuple[str, str], None, None]:
    ...
```

Os três parâmetros de `Generator` são:
1. **YieldType** — tipo do valor produzido pelo `yield` (`tuple[str, str]`)
2. **SendType** — tipo do valor que pode ser enviado ao gerador (aqui `None`)
3. **ReturnType** — tipo do valor retornado ao fim (aqui `None`)

---

## Conceito: Geradores e `yield`

Um **gerador** é uma função que usa `yield` em vez de `return`. Ao contrário de uma função normal que retorna tudo de uma vez, um gerador **produz um valor por vez**, pausando e retomando sua execução a cada chamada de `next()`.

```python
def gen_event():
    while True:           # loop infinito — o gerador nunca se esgota
        player = random.choice(players)
        action = random.choice(actions)
        yield (player, action)   # produz e pausa aqui
```

**Vantagens:** economizam memória, pois não armazenam todos os valores de uma vez — ideal para fluxos de dados contínuos ou muito grandes.

---

## Fluxo do programa

1. Cria o gerador `gen_event()` com um loop `while True` e `yield`.
2. Chama `next()` 1000 vezes com `range(1000)` para exibir os eventos.
3. Cria uma lista estática de 10 eventos chamando `next()` mais 10 vezes.
4. Cria o gerador `consume_event()` que recebe a lista, escolhe um elemento aleatório, remove-o e o entrega com `yield`.
5. Usa `consume_event()` diretamente em `for event in consumidor:` até a lista se esvaziar.
