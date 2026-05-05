# Exercise 0 — Command Quest

**Arquivo:** `ft_command_quest.py`

---

## Funções autorizadas e explicações

### `import sys`

O módulo `sys` dá acesso a variáveis e funções que interagem diretamente com o interpretador Python. Neste exercício, ele é importado para acessar os argumentos passados pela linha de comando.

```python
import sys
```

---

### `sys.argv`

`sys.argv` é uma **lista de strings** que contém os argumentos passados ao script pela linha de comando. O primeiro elemento (`sys.argv[0]`) é sempre o nome do próprio script.

```python
# Executando: python3 ft_command_quest.py hello world 42
# sys.argv == ['ft_command_quest.py', 'hello', 'world', '42']

nome_do_programa = sys.argv[0]   # 'ft_command_quest.py'
primeiro_arg     = sys.argv[1]   # 'hello'
```

---

### `len()`

`len()` retorna o **número de elementos** de uma sequência (lista, string, tupla, etc.).

```python
args = ['hello', 'world', '42']
print(len(args))   # 3

# Usado para saber quantos argumentos foram recebidos:
total = len(sys.argv)   # inclui o nome do script
```

---

### `print()`

`print()` exibe texto ou valores no terminal. Aceita múltiplos argumentos separados por vírgula e possui parâmetros opcionais como `sep` (separador) e `end` (final da linha).

```python
print("Hello, world!")           # Hello, world!
print("Total:", 42)              # Total: 42
print(f"Argumento 1: {sys.argv[1]}")  # usando f-string
```

---

## Fluxo do programa

1. Lê `sys.argv` para obter o nome do programa e os argumentos.
2. Usa `len(sys.argv)` para contar quantos argumentos foram recebidos (incluindo o nome do script).
3. Exibe o nome do programa.
4. Se não houver argumentos além do nome do script, exibe a mensagem `"No arguments provided!"`.
5. Caso contrário, exibe cada argumento numerado e o total.
