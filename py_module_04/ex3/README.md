# ft_vault_security — Exercício 3: Segurança do Cofre

Este programa apresenta a função `secure_archive()`, que fornece acesso seguro a arquivos para leitura ou escrita usando o **context manager** (`with`). A função retorna uma tupla indicando se a operação foi bem-sucedida e o conteúdo resultante ou a mensagem de erro.

---

## Funções autorizadas

### `open()`

Função embutida que abre um arquivo e retorna um objeto de arquivo. Neste exercício é usada **dentro do bloco `with`**, que garante o fechamento automático do arquivo.

```python
with open(file_name, mode) as f:
    ...
```

| Modo  | Significado                              |
|-------|------------------------------------------|
| `'r'` | Leitura de texto (padrão)                |
| `'w'` | Escrita de texto (cria ou sobrescreve)   |

**Por que usar `open()` com `with`?**

Sem `with`, seria necessário chamar `f.close()` manualmente — e se ocorresse um erro entre `open()` e `close()`, o arquivo poderia ficar aberto indefinidamente. O `with` resolve isso automaticamente.

---

### `read()`

Método do objeto de arquivo que lê **todo o conteúdo** e retorna como string.

```python
with open(file_name, mode) as f:
    if mode == 'r':
        data = f.read()
        return (True, data)
```

Exemplos de retorno:

```python
# Arquivo com 3 linhas:
(True, '[FRAGMENT 001] linha um\n[FRAGMENT 002] linha dois\n')

# Arquivo inexistente:
(False, "[Errno 2] No such file or directory: '/not/existing/file'")
```

---

### `write()`

Método que escreve uma string no arquivo aberto em modo de escrita (`'w'`). Não adiciona `\n` automaticamente.

```python
with open(file_name, mode) as f:
    elif mode == 'w':
        f.write(content)
        return (True, 'Content successfully written to file')
```

> Com o `with`, ao sair do bloco (com ou sem erro), o arquivo é fechado e os dados em buffer são **automaticamente gravados no disco** — equivalente a chamar `flush()` e `close()`.

---

### `print()`

Exibe resultados no terminal.

```python
print("=== Cyber Archives Security ===\n")
print(secure_archive("/not/existing/file"))
print(secure_archive("fragment.txt", "r"))
```

---

## O context manager — `with`

O `with` é a novidade central deste exercício. Ele usa o protocolo de **context manager** do Python: ao entrar no bloco, o arquivo é aberto; ao sair — seja normalmente ou por uma exceção — o arquivo é fechado automaticamente.

**Sem `with` (exercícios anteriores):**

```python
file = open(filename, "r")
content = file.read()
file.close()  # Precisa ser chamado manualmente
```

**Com `with` (este exercício):**

```python
with open(filename, "r") as f:
    content = f.read()
# f.close() é chamado automaticamente aqui, mesmo se ocorrer um erro
```

**Vantagens:**

- Elimina o risco de esquecer de fechar o arquivo
- Garante o fechamento mesmo quando ocorre uma exceção
- Código mais limpo e legível

---

## A função `secure_archive()`

```python
def secure_archive(file_name: str, mode: str = 'r',
                   content: str = '') -> tuple[bool, str]:
```

**Parâmetros:**

| Parâmetro   | Tipo  | Obrigatório | Descrição                              |
|-------------|-------|-------------|----------------------------------------|
| `file_name` | `str` | Sim         | Caminho do arquivo                     |
| `mode`      | `str` | Não (`'r'`) | Modo de abertura: `'r'` ou `'w'`       |
| `content`   | `str` | Não (`''`)  | Conteúdo a escrever (apenas modo `'w'`)|

**Retorno:** `tuple[bool, str]`

- `(True, conteúdo)` → operação bem-sucedida
- `(False, mensagem_de_erro)` → operação falhou

**Lógica interna:**

```python
try:
    with open(file_name, mode) as f:
        if mode == 'r':
            data = f.read()
            return (True, data)
        elif mode == 'w':
            f.write(content)
            return (True, 'Content successfully written to file')
except Exception as e:
    return (False, f"[{e.__class__.__name__}] {str(e)}")
```

---

## Tratamento de erros

Exceções são capturadas e retornadas como parte da tupla — o programa nunca quebra:

```python
except Exception as e:
    return (False, f"[{e.__class__.__name__}] {str(e)}")
```

**Exemplos:**

| Situação                  | Retorno                                                      |
|---------------------------|--------------------------------------------------------------|
| Arquivo inexistente       | `(False, "[Errno 2] No such file or directory: '...' ")`     |
| Sem permissão de leitura  | `(False, "[Errno 13] Permission denied: '...'")`             |
| Leitura bem-sucedida      | `(True, "conteúdo do arquivo")`                              |
| Escrita bem-sucedida      | `(True, "Content successfully written to file")`             |

---

## Exemplo de uso

```bash
$ python3 ft_vault_security.py
=== Cyber Archives Security ===

Using 'secure_archive' to read from a nonexistent file:
(False, "[Errno 2] No such file or directory: '/not/existing/file'")

Using 'secure_archive' to read from an inaccessible file:
(False, "[Errno 13] Permission denied: '/etc/shadow'")

Using 'secure_archive' to read from a regular file:
(True, '[FRAGMENT 001] linha um\n[FRAGMENT 002] linha dois\n')

Using 'secure_archive' to write previous content to a new file:
(True, 'Content successfully written to file')
```
