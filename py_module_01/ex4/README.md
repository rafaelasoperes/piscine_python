# Exercise 4 — ft_garden_security

## Descrição

Sistema de segurança do jardim que protege os dados da planta contra valores inválidos.
Introduz o conceito de **encapsulamento**: os atributos são marcados como protegidos
(prefixo `_`) e só podem ser acessados ou modificados por meio de métodos específicos (getters e setters).

---

## Funções autorizadas

### `print()`

Função nativa do Python que exibe uma mensagem no terminal.

**Como é usada neste exercício:**

Exibe mensagens de confirmação quando um valor é atualizado com sucesso, mensagens de erro quando um valor inválido é rejeitado, e o estado atual da planta.

```python
# Dentro do setter — valor válido:
print(f"Height updated: {value}cm")

# Dentro do setter — valor inválido:
print(f"{self.name}: Error, height can't be negative")
print("Height update rejected")

# No main:
print(f"Current state: {rose.name} : {newHeight:.1f}cm, {newAge} days old")
```

---

### `range()`

Função nativa que gera uma sequência de números inteiros.

**Sintaxe:**
```python
range(início, fim)
range(fim)
```

Disponível para uso em loops numéricos quando necessário iterar um número fixo de vezes.

---

### `round()`

Função nativa que arredonda um número de ponto flutuante.

**Sintaxe:**
```python
round(numero, casas_decimais)
```

**Como é usada neste exercício:**

Garante que a altura seja armazenada com 1 casa decimal no momento da criação do objeto.

```python
def __init__(self, name: str, height: float, age: int):
    self._height: float = round(height, 1)
```

---

## Conceito principal: Encapsulamento

### Atributos protegidos (convenção `_`)

Em Python, prefixar um atributo com `_` sinaliza que ele é **protegido** — ou seja, não deve ser acessado diretamente de fora da classe. É uma convenção, não uma restrição técnica.

```python
self._height: float = round(height, 1)
self._age: int = age
```

### Getters — leitura segura

Métodos que retornam o valor de um atributo protegido:

```python
def get_height(self) -> float:
    return self._height

def get_age(self) -> int:
    return self._age
```

### Setters — escrita com validação

Métodos que modificam atributos apenas se o novo valor for válido, protegendo a integridade dos dados:

```python
def set_height(self, value):
    if value < 0:
        print(f"{self.name}: Error, height can't be negative")
        print("Height update rejected")
    else:
        self._height = value
        print(f"Height updated: {value}cm")
```

**Por que encapsular?**

Sem encapsulamento, qualquer parte do código poderia atribuir um valor absurdo diretamente (`planta._height = -999`). Com getters e setters, toda modificação passa por uma validação centralizada, garantindo que os dados permaneçam consistentes.
