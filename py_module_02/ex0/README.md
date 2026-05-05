# Exercise 0 — ft_first_exception

## Descrição

Validação básica de dados agrícolas com tratamento de exceções. O programa recebe leituras de temperatura de sensores de campo e filtra dados corrompidos antes que contaminem a análise.

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
int("abc")   # lança ValueError: invalid literal for int() with base 10: 'abc'
int(3.7)     # retorna 3 (trunca o valor)
```

**Como é usada neste exercício:**

Dentro de `input_temperature()`, `int()` é chamada para converter a string recebida do sensor em um número inteiro. Caso a string seja inválida, a exceção gerada por `int()` é capturada pelo bloco `except` em `test_temperature()`.

---

### `print()`

Exibe uma mensagem no terminal (saída padrão).

**Sintaxe:**
```python
print(valor)
print(f"Texto {variavel}")  # com f-string
```

**Comportamento:**
- Aceita qualquer tipo de dado e o converte para string antes de exibir.
- Com f-strings, permite inserir variáveis diretamente no texto.

**Exemplos:**
```python
print("Olá")                        # exibe: Olá
print(f"Temperatura: {25}°C")       # exibe: Temperatura: 25°C
print(f"Erro: {erro}")              # exibe a mensagem da exceção
```

**Como é usada neste exercício:**

`print()` é usada em `test_temperature()` para mostrar o dado de entrada, o resultado da conversão quando bem-sucedida, a mensagem de erro quando a conversão falha, e a confirmação de que o programa não travou.

---

## Fluxo do programa

```
test_temperature()
│
├── valor = "25"  →  input_temperature("25")  →  int("25") = 25  ✓
│   └── print: "Temperature is now 25°C"
│
└── valor = "abc"  →  input_temperature("abc")  →  int("abc")  ✗ ValueError
    └── except captura o erro
        └── print: "Caught input_temperature error: ..."
```

---

## Exemplo de saída esperada

```
=== Garden Temperature ===

Input data is '25'
Temperature is now 25°C

Input data is 'abc'
Caught input_temperature error: invalid literal for int() with base 10: 'abc'

All tests completed - program didn't crash!
```
