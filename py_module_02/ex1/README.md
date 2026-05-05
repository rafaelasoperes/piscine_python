# Exercise 1 — ft_raise_exception

## Descrição

Pipeline de validação de dados agrícolas com controle de intervalo. Além de validar o formato da entrada, o programa verifica se a temperatura está dentro do intervalo adequado para o crescimento das plantas (0°C a 40°C). Valores fora do intervalo geram exceções explícitas com `raise`.

---

## Funções autorizadas

### `int()`

Converte um valor para o tipo inteiro.

**Sintaxe:**
```python
int(valor)
```

**Comportamento:**
- Se o valor puder ser convertido, retorna o número inteiro correspondente.
- Se o valor **não** puder ser convertido (ex: `"abc"`), lança uma exceção do tipo `ValueError`.

**Exemplos:**
```python
int("25")    # retorna 25
int("100")   # retorna 100
int("abc")   # lança ValueError
int("-50")   # retorna -50
```

**Como é usada neste exercício:**

Em `input_temperature()`, `int()` converte a string da entrada antes da validação de intervalo. Se a string for inválida, o `ValueError` propagado por `int()` é capturado em `test_temperature()`.

---

### `print()`

Exibe uma mensagem no terminal (saída padrão).

**Sintaxe:**
```python
print(valor)
print(f"Texto {variavel}")
```

**Comportamento:**
- Aceita qualquer tipo de dado e o converte para string antes de exibir.
- Com f-strings, permite inserir variáveis e expressões diretamente no texto.

**Exemplos:**
```python
print(f"Temperature is now {temperature}°C")
print(f"Caught input_temperature error: {error}")
```

**Como é usada neste exercício:**

`print()` exibe o dado de entrada testado, a temperatura válida quando a conversão é bem-sucedida, e a mensagem de erro (seja de formato inválido ou de intervalo fora do permitido).

---

## O uso de `raise` neste exercício

Embora `raise` não seja uma função, é o mecanismo central deste exercício. Ele permite lançar uma exceção manualmente quando os dados falham na validação de negócio:

```python
if temperature > 40:
    raise ValueError(f"{temperature}°C is too hot for plants (max 40°C)")
if temperature < 0:
    raise ValueError(f"{temperature}°C is too cold for plants (min 0°C)")
```

Isso permite distinguir dois tipos de falha que chegam ao mesmo `except ValueError`:
- Falha de formato: vinda de `int()` (ex: `"abc"`)
- Falha de domínio: lançada manualmente (ex: `"100"` ou `"-50"`)

---

## Fluxo do programa

```
test_temperature()
│
├── "25"   →  int("25") = 25   →  0 ≤ 25 ≤ 40  ✓  →  retorna 25
├── "abc"  →  int("abc")       →  ValueError (formato)
├── "100"  →  int("100") = 100 →  100 > 40      →  raise ValueError (intervalo)
└── "-50"  →  int("-50") = -50 →  -50 < 0       →  raise ValueError (intervalo)
```

---

## Exemplo de saída esperada

```
=== Garden Temperature Checker ===

Input data is '25'
Temperature is now 25°C

Input data is 'abc'
Caught input_temperature error: invalid literal for int() with base 10: 'abc'

Input data is '100'
Caught input_temperature error: 100°C is too hot for plants (max 40°C)

Input data is '-50'
Caught input_temperature error: -50°C is too cold for plants (min 0°C)

All tests completed - program didn't crash!
```
