# Exercise 0 — Creature Factory

**Arquivos:** `battle.py`, pacote `ex0/` (`_product.py`, `factory.py`, `__init__.py`)
**Autorizados:** `builtins`, tipos padrão, `import typing`, `import abc`

---

## Padrão de Projeto: Abstract Factory

Este exercício implementa o padrão **Abstract Factory**, que permite criar famílias de objetos relacionados sem expor suas classes concretas. Em vez de instanciar `Flameling()` diretamente, o código cliente recebe uma `FlameFactory` e chama seus métodos — sem saber qual classe concreta será usada.

---

## Módulo `abc` — Classes Abstratas

### `ABC`
Classe base importada de `abc` que transforma uma classe Python comum em uma **classe abstrata**. Uma classe abstrata não pode ser instanciada diretamente; ela serve como contrato que as subclasses devem respeitar.

```python
from abc import ABC, abstractmethod

class Creature(ABC):
    ...
```

Aqui, `Creature` herda de `ABC`, tornando-se um contrato: toda classe que herdar de `Creature` precisa implementar os métodos marcados como abstratos.

### `@abstractmethod`
Decorador que marca um método como **obrigatório de ser implementado** nas subclasses. Tentar instanciar uma classe com um `@abstractmethod` não implementado levanta `TypeError`.

```python
@abstractmethod
def attack(self) -> str:
    pass
```

Aplicado em `Creature.attack` e nos métodos `create_base` / `create_evolved` de `CreatureFactory`, garantindo que cada família de criaturas e cada fábrica forneça sua própria implementação.

---

## Módulo `typing` — Anotações de Tipo

### Anotações de retorno (`-> str`, `-> Creature`, etc.)
O `typing` é usado para tornar as assinaturas das funções explícitas e verificáveis com `mypy`.

```python
def describe(self) -> str:
    return f"{self.name} is a {self.type} type Creature"

def create_base(self) -> Creature:
    ...
```

As anotações documentam o contrato de cada método e permitem que ferramentas de análise estática detectem erros antes da execução.

---

## Funções e Métodos Principais

### `__init__(self, name: str, type: str) -> None`
Construtor da classe `Creature`. Recebe o nome e o tipo da criatura e os armazena como atributos de instância.

```python
def __init__(self, name: str, type: str) -> None:
    super().__init__()
    self.name = name
    self.type = type
```

`super().__init__()` garante que a cadeia de inicialização do MRO (Method Resolution Order) seja respeitada — essencial quando se usa herança múltipla com `ABC`.

### `describe(self) -> str`
Método **concreto** definido em `Creature` e herdado por todas as subclasses. Retorna uma string padronizada com o nome e o tipo da criatura.

```python
def describe(self) -> str:
    return f"{self.name} is a {self.type} type Creature"
```

Por ser concreto (não abstrato), as subclasses **não precisam** reimplementá-lo — herdam o comportamento automaticamente.

### `attack(self) -> str`
Método **abstrato** definido em `Creature`. Cada subclasse concreta (`Flameling`, `Pyrodon`, `Aquabub`, `Torragon`) fornece sua própria mensagem de ataque.

```python
# Em Flameling:
def attack(self) -> str:
    return f"{self.name} uses Ember!"
```

### `create_base(self) -> Creature` e `create_evolved(self) -> Creature`
Métodos **abstratos** de `CreatureFactory`. Cada fábrica concreta os implementa para retornar a criatura base e a evoluída de sua família.

```python
# Em FlameFactory:
def create_base(self) -> Flameling:
    return Flameling()

def create_evolved(self) -> Pyrodon:
    return Pyrodon()
```

---

## Builtins Utilizados

### `print()`
Função embutida usada em `battle.py` para exibir os resultados no terminal.

```python
print(flameling.describe())
print(flameling.attack())
```

### `f-strings` (formatação de strings)
Sintaxe embutida do Python para interpolar variáveis dentro de strings de forma legível.

```python
return f"{self.name} is a {self.type} type Creature"
```

---

## Regra de Encapsulamento do Pacote

O `__init__.py` do pacote `ex0` expõe **apenas as fábricas**, nunca as criaturas concretas:

```python
__all__ = ['CreatureFactory', 'FlameFactory', 'AquaFactory']

from .factory import CreatureFactory, FlameFactory, AquaFactory
```

Isso garante que o código cliente dependa apenas das abstrações, não das implementações — princípio fundamental do padrão Abstract Factory.
