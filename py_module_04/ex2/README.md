# ft_stream_management — Exercício 2: Gerenciamento de Streams

Este programa estende o exercício anterior com duas mudanças principais: mensagens de erro são enviadas para o **stream de erro** (`stderr`) em vez do terminal normal, e a entrada do usuário é lida diretamente pelo **stream de entrada** (`stdin`), sem usar a função `input()`.

---

## Funções e módulos autorizados

> Este exercício herda as funções dos exercícios anteriores. As novidades são: `sys.stdin`, `sys.stdout`, `sys.stderr`, `io.readline()` e `io.flush()`.

---

### `import sys`

Módulo que fornece acesso aos três streams padrão do sistema operacional, entre outros recursos.

```python
import sys
```

---

### `sys.argv`

Lista de argumentos passados ao script pela linha de comando.

```python
filename = sys.argv[1]
```

---

### `sys.stdin`

Stream de **entrada padrão** — por padrão, representa o teclado. Permite ler o que o usuário digita sem usar `input()`.

```python
new_filename = sys.stdin.readline().strip()
# Lê uma linha digitada pelo usuário e remove o \n do final com strip()
```

> A diferença entre `sys.stdin.readline()` e `input()` é que `readline()` opera diretamente sobre o stream, o que dá mais controle sobre a leitura (por exemplo, é possível redirecionar `stdin` para um arquivo).

---

### `sys.stdout`

Stream de **saída padrão** — por padrão, representa o terminal. Equivalente ao destino padrão de `print()`, mas com controle mais fino.

```python
sys.stdout.write("Enter new file name (or empty): ")
sys.stdout.flush()
```

> Usado aqui para exibir o prompt sem quebra de linha ao final (diferente de `print()`, que sempre adiciona `\n`).

---

### `sys.stderr`

Stream de **saída de erro** — separado do `stdout`. Usado para exibir mensagens de erro sem misturá-las com a saída normal do programa. No terminal, ambos aparecem juntos, mas podem ser redirecionados de forma independente.

```python
sys.stderr.write(f"[STDERR] Error opening file '{filename}': {e}\n")
```

**Por que isso importa?**

```bash
# Redirecionar apenas erros para um arquivo de log:
$ python3 ft_stream_management.py foo 2> erros.log

# Redirecionar apenas a saída normal:
$ python3 ft_stream_management.py arquivo.txt > saida.txt
```

---

### `len()`

Verifica o número de argumentos recebidos.

```python
if len(sys.argv) < 2:
    return
```

---

### `open()`

Abre um arquivo para leitura ou escrita.

```python
with open(filename, 'r') as file:
    ...
with open(new_filename, 'w'):
    pass
```

---

### `import typing` e `typing.IO`

Permite anotar variáveis que representam objetos de arquivo com tipos precisos para verificação estática.

```python
import typing
file: typing.IO[str] = open(filename, "r")
```

---

### `io.read()`

Lê todo o conteúdo de um arquivo de uma vez como string.

```python
content: str = file.read()
```

---

### `io.readline()`

Lê **uma única linha** do stream. Diferente de `read()`, não lê o arquivo inteiro — avança linha por linha a cada chamada.

Usado aqui para ler a entrada do usuário via `sys.stdin`:

```python
new_filename = sys.stdin.readline().strip()
```

- `readline()` inclui o `\n` ao final da linha
- `.strip()` remove esse caractere (e quaisquer espaços extras)

---

### `io.write()`

Escreve uma string diretamente em um stream ou arquivo, sem adicionar `\n` automaticamente.

```python
sys.stdout.write("Enter new file name (or empty): ")
sys.stderr.write(f"[STDERR] Error opening file '{filename}': {e}\n")
```

> Aqui `io.write()` é usado tanto em `sys.stdout` quanto em `sys.stderr` — pois ambos são streams do tipo `IO` e possuem o método `write()`.

---

### `io.flush()`

Força o envio imediato do conteúdo que está no buffer do stream para o destino (terminal, arquivo, etc.).

```python
sys.stdout.write("Enter new file name (or empty): ")
sys.stdout.flush()
```

**Por que é necessário?**

Em Python, streams de saída podem ser **bufferizados**: o texto é acumulado em memória antes de ser exibido. Sem `flush()`, o prompt poderia aparecer apenas depois que o usuário já tivesse digitado algo. `flush()` garante que a mensagem seja exibida imediatamente.

---

### `io.close()`

Fecha o arquivo e libera recursos. Aqui não é chamado explicitamente — o arquivo é fechado automaticamente pelo bloco `with` (context manager), que garante o fechamento mesmo em caso de erro.

---

### `print()`

Exibe mensagens na saída padrão (`stdout`).

```python
print("=== Cyber Archives Recovery & Preservation ===")
print(f"[FRAGMENT {i:03d}] {line.strip()}")
```

---

## Os três streams padrão — resumo

| Stream       | Objeto Python | Uso típico              | Número |
|--------------|---------------|--------------------------|--------|
| Entrada      | `sys.stdin`   | Ler dados do usuário     | 0      |
| Saída normal | `sys.stdout`  | Exibir resultados        | 1      |
| Saída de erro| `sys.stderr`  | Exibir mensagens de erro | 2      |

---

## Tratamento de erros

Erros de abertura de arquivo são enviados para `stderr`:

```python
except Exception as e:
    sys.stderr.write(f"[STDERR] Error opening file '{filename}': {e}\n")
```

---

## Exemplo de uso

```bash
$ python3 ft_stream_management.py foo
=== Cyber Archives Recovery & Preservation ===
Accessing file 'foo'
[STDERR] Error opening file 'foo': [Errno 2] No such file or directory: 'foo'

$ python3 ft_stream_management.py fragmento.txt
=== Cyber Archives Recovery & Preservation ===
Accessing file 'fragmento.txt'
---
[FRAGMENT 001] Linha de dados
---
File 'fragmento.txt' closed.

Transform data:
---
[FRAGMENT 001] Linha de dados#
---
Enter new file name (or empty):
```
