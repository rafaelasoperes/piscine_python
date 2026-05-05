# ft_ancient_text — Exercício 0: Recuperação de Texto Antigo

Este programa recebe o nome de um arquivo pela linha de comando, lê seu conteúdo e o exibe no terminal — semelhante ao comando `cat` do Linux. Erros como arquivo inexistente ou inacessível são tratados e exibidos ao usuário.

---

## Funções e módulos autorizados

### `import sys`

Módulo da biblioteca padrão do Python que fornece acesso a parâmetros e funções do interpretador e do sistema operacional.

```python
import sys
```

---

### `sys.argv`

Lista que contém os argumentos passados ao script pela linha de comando.

- `sys.argv[0]` → nome do script em execução
- `sys.argv[1]` → primeiro argumento passado (neste caso, o nome do arquivo)

```python
filename: str = sys.argv[1]
# Se o usuário executar: python3 ft_ancient_text.py meu_arquivo.txt
# filename será igual a "meu_arquivo.txt"
```

---

### `len()`

Função embutida do Python que retorna o número de elementos em um objeto iterável (lista, string, etc.).

Usada aqui para verificar se o número correto de argumentos foi passado:

```python
if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <file>")
    return
# len(sys.argv) == 1 significa que nenhum argumento foi passado
# len(sys.argv) == 2 significa que exatamente um argumento foi passado
```

---

### `open()`

Função embutida que abre um arquivo e retorna um objeto de arquivo (file object) para manipulação.

Sintaxe básica:

```python
open(nome_do_arquivo, modo)
```

| Modo | Significado         |
|------|---------------------|
| `'r'`| Leitura (padrão)    |
| `'w'`| Escrita (sobrescreve)|
| `'a'`| Escrita (acrescenta)|

```python
file: typing.IO[str] = open(filename, "r")
# Abre o arquivo para leitura de texto
```

> O tipo retornado por `open()` é um objeto do tipo `IO` (entrada/saída), especificamente `TextIOWrapper` para arquivos de texto.

---

### `import typing` e `typing.IO`

O módulo `typing` fornece suporte a anotações de tipo em Python. `typing.IO` é usado para anotar variáveis que representam objetos de arquivo retornados por `open()`.

```python
import typing

file: typing.IO[str] = open(filename, "r")
# typing.IO[str] indica que é um objeto de arquivo que lida com strings (texto)
```

Isso não altera o comportamento do programa, mas melhora a legibilidade e permite verificação estática de tipos com ferramentas como `mypy`.

---

### `io.read()`

Método do objeto de arquivo que lê **todo o conteúdo** do arquivo de uma vez e o retorna como uma string.

```python
content: str = file.read()
# content agora contém todo o texto do arquivo
print(content, end="")
```

> O parâmetro `end=""` no `print` evita que uma linha em branco extra seja adicionada ao final, já que o próprio conteúdo do arquivo geralmente já termina com `\n`.

---

### `io.close()`

Método que fecha o arquivo aberto, liberando os recursos do sistema operacional associados a ele. É importante fechar arquivos após o uso para evitar vazamento de recursos.

```python
file.close()
print(f"File '{filename}' closed.")
```

---

### `print()`

Função embutida que exibe texto no terminal (saída padrão — `stdout`).

```python
print("=== Cyber Archives Recovery ===")
print(f"Accessing file '{filename}'")
print(content, end="")
```

- O argumento `end=""` substitui o caractere de nova linha padrão por uma string vazia.
- f-strings (`f"..."`) permitem inserir variáveis diretamente dentro da string.

---

## Tratamento de erros

O bloco `try/except` captura qualquer exceção que ocorra ao tentar abrir ou ler o arquivo, como:

- `FileNotFoundError` → arquivo não existe
- `PermissionError` → sem permissão de leitura

```python
try:
    file: typing.IO[str] = open(filename, "r")
    ...
except Exception as e:
    print(f"Error opening file '{filename}': {e}")
```

---

## Exemplo de uso

```bash
$ python3 ft_ancient_text.py fragmento.txt
=== Cyber Archives Recovery ===
Accessing file 'fragmento.txt'
---
[FRAGMENT 001] Linha de exemplo
---
File 'fragmento.txt' closed.
```
