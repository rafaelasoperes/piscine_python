# Exercise 2 — ft_different_errors

## Descrição

Demonstração dos diferentes tipos de erros que um programa de jardim pode encontrar. Cada tipo de problema em Python gera uma exceção específica. Saber distingui-las permite criar mensagens de erro mais claras e tratar cada situação de forma apropriada.

---

## Funções autorizadas

### `print()`

Exibe uma mensagem no terminal (saída padrão).

**Sintaxe:**
```python
print(valor)
print(f"Texto {variavel}")
```

**Comportamento:**
- Aceita qualquer tipo de dado e exibe como texto.
- Usado para mostrar o progresso dos testes e as mensagens de erro capturadas.

**Exemplos:**
```python
print("Testing operation 0...")
print(f"Caught ValueError: {error}")
print("Operation completed successfully")
```

**Como é usada neste exercício:**

`print()` é usada em `test_error_types()` para indicar qual operação está sendo testada, exibir o tipo e a mensagem de cada erro capturado, e confirmar quando uma operação conclui sem erros.

---

### `open()`

Abre um arquivo para leitura ou escrita.

**Sintaxe:**
```python
open(caminho_do_arquivo)
open(caminho_do_arquivo, modo)
```

**Comportamento:**
- Se o arquivo existir, retorna um objeto de arquivo que pode ser lido.
- Se o arquivo **não** existir, lança `FileNotFoundError`.
- Quando não há erros, o arquivo deve ser fechado com `.close()` ou usando `with`. Neste exercício, como o erro é lançado antes de o arquivo ser aberto, não é necessário fechar.

**Exemplos:**
```python
open("/non/existent/file")
# lança: FileNotFoundError: [Errno 2] No such file or directory: '/non/existent/file'

f = open("arquivo.txt")
# abre o arquivo com sucesso
```

**Como é usada neste exercício:**

Em `garden_operations()` com `operation_number == 2`, `open()` tenta abrir um caminho inválido para simular uma falha de acesso a arquivo — situação comum em sistemas de IoT que tentam ler logs ou configurações inexistentes.

---

### `int()`

Converte um valor para o tipo inteiro.

**Sintaxe:**
```python
int(valor)
```

**Comportamento:**
- Se o valor puder ser convertido, retorna o inteiro correspondente.
- Se **não** puder (ex: `"abc"`), lança `ValueError`.

**Exemplos:**
```python
int("abc")   # lança ValueError: invalid literal for int() with base 10: 'abc'
int("42")    # retorna 42
```

**Como é usada neste exercício:**

Em `garden_operations()` com `operation_number == 0`, `int("abc")` é chamado para simular a chegada de um dado corrompido de sensor que deveria ser numérico.

---

## Tipos de erro demonstrados

| operation_number | Código problemático          | Exceção gerada       |
|-----------------|------------------------------|----------------------|
| 0               | `int("abc")`                 | `ValueError`         |
| 1               | `10 / 0`                     | `ZeroDivisionError`  |
| 2               | `open("/non/existent/file")` | `FileNotFoundError`  |
| 3               | `"plants: " + 5`             | `TypeError`          |
| 4               | (nenhum erro)                | —                    |

---

## Como capturar múltiplos tipos com um único `try`

Python permite encadear vários `except` em um único bloco `try`. Cada cláusula captura apenas o tipo especificado:

```python
try:
    garden_operations(operation)
except ValueError as error:
    print(f"Caught ValueError: {error}")
except ZeroDivisionError as error:
    print(f"Caught ZeroDivisionError: {error}")
except FileNotFoundError as error:
    print(f"Caught FileNotFoundError: {error}")
except TypeError as error:
    print(f"Caught TypeError: {error}")
```

---

## Exemplo de saída esperada

```
=== Garden Error Types Demo ===
Testing operation 0...
Caught ValueError: invalid literal for int() with base 10: 'abc'
Testing operation 1...
Caught ZeroDivisionError: division by zero
Testing operation 2...
Caught FileNotFoundError: [Errno 2] No such file or directory: '/non/existent/file'
Testing operation 3...
Caught TypeError: can only concatenate str (not "int") to str
Testing operation 4...
Operation completed successfully

All error types tested successfully!
```
