# ft_archive_creation — Exercício 1: Criação de Arquivo

Este programa estende o exercício anterior: além de ler e exibir o conteúdo de um arquivo, ele transforma cada linha adicionando o caractere `#` ao final (padrão 2087), exibe o novo conteúdo e pergunta ao usuário se deseja salvar o resultado em um novo arquivo.

---

## Funções e módulos autorizados

> Este exercício herda todas as funções do Exercício 0. As novas funções autorizadas são `io.write()` e `input()`.

---

### `import sys`

Módulo da biblioteca padrão que fornece acesso a parâmetros e funções relacionados ao sistema.

```python
import sys
```

---

### `sys.argv`

Lista de argumentos passados ao script pela linha de comando.

```python
filename: str = sys.argv[1]
```

---

### `len()`

Verifica o número de argumentos recebidos na linha de comando.

```python
if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <file>")
    return
```

---

### `open()`

Abre um arquivo para leitura ou escrita. Neste exercício é usado duas vezes:

**Leitura** — para carregar o conteúdo original do arquivo:

```python
file: typing.IO[str] = open(filename, "r")
```

**Escrita** — para salvar o conteúdo transformado em um novo arquivo. O modo `"w"` cria o arquivo se não existir, ou **sobrescreve** se já existir:

```python
new_file: typing.IO[str] = open(new_filename, "w")
```

---

### `import typing` e `typing.IO`

Usado para anotar o tipo de variáveis que representam objetos de arquivo retornados por `open()`.

```python
import typing

file: typing.IO[str] = open(filename, "r")
new_file: typing.IO[str] = open(new_filename, "w")
```

---

### `io.read()`

Lê todo o conteúdo do arquivo de uma vez e retorna como string.

```python
content: str = file.read()
```

---

### `io.write()`

Método do objeto de arquivo que **escreve uma string** no arquivo aberto em modo de escrita (`"w"`). Diferente de `print()`, não adiciona automaticamente uma nova linha ao final.

```python
new_file.write(new_content)
# Escreve o conteúdo transformado (com # no final de cada linha) no novo arquivo
```

> `io.write()` retorna o número de caracteres escritos, mas esse valor geralmente não é utilizado.

---

### `io.close()`

Fecha o arquivo e libera os recursos do sistema. Deve ser chamado após terminar de usar o arquivo, tanto para leitura quanto para escrita.

```python
file.close()
print(f"File '{filename}' closed.")

new_file.close()
print(f"Data saved in file '{new_filename}'.")
```

> Fechar o arquivo de escrita é especialmente importante: garante que todos os dados em memória (buffer) sejam efetivamente gravados no disco.

---

### `input()`

Função embutida que exibe uma mensagem ao usuário e aguarda que ele digite algo no terminal, retornando o texto digitado como string. A execução do programa fica pausada até que o usuário pressione Enter.

```python
new_filename: str = input("Enter new file name (or empty): ")

if new_filename == "":
    print("Not saving data.")
else:
    print(f"Saving data to '{new_filename}'")
    ...
```

> Se o usuário não digitar nada e apenas pressionar Enter, `input()` retorna uma string vazia (`""`).

---

### `print()`

Exibe mensagens no terminal (saída padrão).

```python
print("=== Cyber Archives Recovery & Preservation ===")
print(new_content, end="")
print("Not saving data.")
```

---

## A função `add_archive_char()`

Esta função percorre o texto caractere por caractere e adiciona `#` ao final de cada linha. Ao encontrar `\n` (quebra de linha), insere `#` antes dela. Se o arquivo não terminar com `\n`, adiciona `#` ao final do texto.

```python
def add_archive_char(text: str) -> str:
    result: str = ""
    i: int = 0

    while i < len(text):
        if text[i] == "\n":
            result += "#\n"
        else:
            result += text[i]
        i += 1

    if len(text) > 0 and text[len(text) - 1] != "\n":
        result += "#"

    return result
```

**Exemplo de transformação:**

```
Entrada:  "linha um\nlinha dois\n"
Saída:    "linha um#\nlinha dois#\n"
```

---

## Tratamento de erros

Qualquer exceção ao abrir, ler ou escrever arquivos é capturada e exibida ao usuário:

```python
try:
    ...
except Exception as e:
    print(f"Error opening file '{filename}': {e}")
```

---

## Exemplo de uso

```bash
$ python3 ft_archive_creation.py fragmento.txt
=== Cyber Archives Recovery & Preservation ===
Accessing file 'fragmento.txt'
---
[FRAGMENT 001] Dados antigos
---
File 'fragmento.txt' closed.

Transform data:
---
[FRAGMENT 001] Dados antigos#
---
Enter new file name (or empty): novo.txt
Saving data to 'novo.txt'
Data saved in file 'novo.txt'.
```
