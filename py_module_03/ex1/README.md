# Exercise 1 — Score Cruncher

**Arquivo:** `ft_score_analytics.py`

---

## Funções autorizadas e explicações

### `import sys` / `sys.argv`

O módulo `sys` permite acessar os argumentos passados pela linha de comando através de `sys.argv`, que é uma lista de strings. O índice `0` contém o nome do script; os demais, os argumentos fornecidos pelo usuário.

```python
import sys

args = sys.argv[1:]   # ignora o nome do script
# Executando: python3 ft_score_analytics.py 100 200 300
# args == ['100', '200', '300']
```

---

### `len()`

Retorna o número de elementos de uma sequência. Usado para contar quantos scores válidos foram processados (número de jogadores).

```python
scores = [100, 200, 300]
print(len(scores))   # 3  → total de jogadores
```

---

### `sum()`

Retorna a **soma de todos os elementos** de um iterável numérico.

```python
scores = [1500, 2300, 1800]
print(sum(scores))   # 5600  → pontuação total
```

---

### `max()`

Retorna o **maior valor** de um iterável.

```python
scores = [1500, 2300, 1800]
print(max(scores))   # 2300  → maior pontuação
```

---

### `min()`

Retorna o **menor valor** de um iterável.

```python
scores = [1500, 2300, 1800]
print(min(scores))   # 1500  → menor pontuação
```

---

### `print()`

Exibe valores no terminal. Usado para mostrar todos os resultados das estatísticas de forma formatada.

```python
print(f"Average score: {average}")
print(f"High score: {high}")
```

---

### Bloco `try / except`

Embora não seja uma função, o `try/except` é fundamental neste exercício. Ele permite **capturar erros** sem travar o programa — especialmente quando o usuário passa um valor que não pode ser convertido para inteiro.

```python
try:
    score = int(arg)        # tenta converter para inteiro
    valid_scores += [score]
except ValueError:
    print(f"Invalid parameter: '{arg}'")  # descarta o valor inválido
```

---

## Fluxo do programa

1. Lê os argumentos de `sys.argv[1:]`.
2. Para cada argumento, tenta convertê-lo para `int` com `try/except`.
3. Argumentos inválidos são descartados com uma mensagem de erro.
4. Se nenhum score válido restar, exibe a mensagem de uso e encerra.
5. Caso contrário, calcula e exibe:
   - Total de jogadores → `len()`
   - Pontuação total → `sum()`
   - Média → `total / len()`
   - Maior score → `max()`
   - Menor score → `min()`
   - Amplitude → `max() - min()`
