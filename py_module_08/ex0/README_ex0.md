# Exercise 0 — Entering the Matrix

**Arquivo:** `construct.py`
**Módulos autorizados:** `sys`, `os`, `site`, `print()`

---

## O que o programa faz

Detecta se está rodando dentro de um ambiente virtual Python e exibe informações sobre o ambiente atual. Se nenhum ambiente virtual for detectado, fornece instruções para criar e ativar um.

---

## Funções e módulos utilizados

### `sys.prefix` e `sys.base_prefix`

```python
in_virtual_env = sys.prefix != sys.base_prefix
```

- `sys.prefix` → caminho do ambiente Python **atualmente ativo** (pode ser um venv)
- `sys.base_prefix` → caminho do Python **global/base** do sistema

Quando esses dois valores são **diferentes**, significa que um ambiente virtual está ativo. É a forma padrão de detectar um venv em Python 3.

---

### `sys.executable`

```python
print(f"Current Python: {sys.executable}")
```

Retorna o caminho absoluto do interpretador Python que está executando o script no momento. Útil para mostrar ao usuário exatamente qual Python está sendo usado (global ou do venv).

---

### `os.path.basename()`

```python
env_name = os.path.basename(env_path)
```

Extrai o **nome final** de um caminho de diretório. Por exemplo, de `/home/user/matrix_env` extrai apenas `matrix_env`. Usado para exibir o nome do ambiente virtual de forma legível.

---

### `site.getsitepackages()`

```python
paths = site.getsitepackages()
print(paths[0])
```

Retorna uma lista com os diretórios onde os pacotes instalados ficam armazenados no ambiente Python atual. Quando dentro de um venv, aponta para o diretório isolado do venv; fora dele, aponta para o diretório global do sistema. É o que ilustra a diferença prática entre instalar pacotes globalmente e dentro de um ambiente virtual.

---

## Exemplo de saída

**Fora do ambiente virtual:**
```
MATRIX STATUS: You're still plugged in

Current Python: /usr/bin/python3.11
Virtual Environment: None detected

WARNING: You're in the global environment!
The machines can see everything you install.

To enter the construct, run:
python -m venv matrix_env
source matrix_env/bin/activate  # On Unix
matrix_env\Scripts\activate  # On Windows
Then run this program again.
```

**Dentro do ambiente virtual:**
```
MATRIX STATUS: Welcome to the construct

Current Python: /path/to/matrix_env/bin/python
Virtual Environment: matrix_env
Environment Path: /path/to/matrix_env

SUCCESS: You're in an isolated environment!
Safe to install packages without affecting
the global system.

Package installation path:
/path/to/matrix_env/lib/python3.11/site-packages
```
