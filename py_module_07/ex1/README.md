# Exercise 1 — Capabilities

**Arquivos:** `capacitor.py`, pacote `ex1/` (`capabilities.py`, `creature.py`, `factory.py`, `__init__.py`)
**Autorizados:** `builtins`, tipos padrão, `import typing`, `import abc`

---

## Padrão de Projeto: Mixin / Interface com Herança Múltipla

Este exercício introduz **capabilities** (capacidades) como classes abstratas independentes — elas **não herdam de `Creature`**. As criaturas concretas herdam de ambas ao mesmo tempo (herança múltipla), adquirindo tanto o comportamento base de `Creature` quanto a capacidade especial.

```python
class Sproutling(Creature, HealCapability):
    ...

class Shiftling(Creature, TransformCapability):
    ...
```

Essa separação garante que as capabilities possam ser reutilizadas futuramente em outras hierarquias, não apenas em `Creature`.

---

## Módulo `abc` — Classes Abstratas

### `ABC` e `@abstractmethod`
Mesmos usos do Exercise 0, agora aplicados também às classes de capability.

```python
class HealCapability(ABC):
    @abstractmethod
    def heal(self) -> str:
        pass
```

```python
class TransformCapability(ABC):
    def __init__(self) -> None:
        self.is_transformed: bool = False

    @abstractmethod
    def transform(self) -> str:
        pass

    @abstractmethod
    def revert(self) -> str:
        pass
```

`HealCapability` define apenas a interface do método `heal`.
`TransformCapability` vai além: além de definir `transform` e `revert` como abstratos, fornece um `__init__` concreto que inicializa o atributo de estado `is_transformed`.

---

## Herança Múltipla e MRO

### `super().__init__()`
Quando uma classe herda de múltiplas bases, o Python usa o **MRO (Method Resolution Order)** para determinar a ordem em que os `__init__` são chamados. Chamar `super().__init__()` propaga a inicialização corretamente por toda a cadeia.

```python
class Shiftling(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__("Shiftling", "Normal")
        TransformCapability.__init__(self)
```

Aqui, `super().__init__("Shiftling", "Normal")` inicializa `Creature`, e `TransformCapability.__init__(self)` garante que `self.is_transformed` seja criado, já que o MRO pode não chamar `TransformCapability.__init__` automaticamente nessa estrutura.

---

## Módulo `typing` — Anotações de Tipo

### Anotação de atributo com tipo explícito
```python
self.is_transformed: bool = False
```

Além de anotar parâmetros e retornos de funções, o `typing` permite anotar atributos de instância diretamente. Isso deixa claro que `is_transformed` é sempre um `bool`, facilitando a verificação com `mypy`.

---

## Atributo de Estado: `is_transformed`

O atributo `is_transformed` armazenado em `TransformCapability` torna o **estado persistente entre chamadas**. Isso afeta diretamente o comportamento do método `attack` nas criaturas que herdam essa capability:

```python
# Em Shiftling:
def attack(self) -> str:
    if self.is_transformed:
        return f"{self.name} performs a boosted strike!"
    return f"{self.name} attacks normally."
```

O fluxo esperado é:
1. `attack()` → ataque normal (transformado = False)
2. `transform()` → muda `is_transformed` para True
3. `attack()` → ataque potencializado (transformado = True)
4. `revert()` → muda `is_transformed` de volta para False

---

## Métodos das Capabilities

### `heal(self) -> str`
Método abstrato de `HealCapability`. Cada criatura com cura implementa sua versão:

```python
# Em Sproutling:
def heal(self) -> str:
    return f"{self.name} heals itself for a small amount"

# Em Bloomelle:
def heal(self) -> str:
    return f"{self.name} heals itself and others for a large amount"
```

### `transform(self) -> str`
Método abstrato de `TransformCapability`. Muda `is_transformed` para `True` e retorna uma string descritiva.

```python
def transform(self) -> str:
    self.is_transformed = True
    return f"{self.name} shifts into a sharper form!"
```

### `revert(self) -> str`
Método abstrato de `TransformCapability`. Muda `is_transformed` de volta para `False`.

```python
def revert(self) -> str:
    self.is_transformed = False
    return f"{self.name} returns to normal."
```

---

## Fábricas de Exercise 1

`HealingCreatureFactory` e `TransformCreatureFactory` herdam de `CreatureFactory` (definido em `ex0`) e implementam `create_base` / `create_evolved` para suas respectivas famílias.

```python
from ex0.factory import CreatureFactory

class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> Sproutling:
        return Sproutling()

    def create_evolved(self) -> Bloomelle:
        return Bloomelle()
```

---

## Regra de Encapsulamento do Pacote

O `__init__.py` de `ex1` expõe apenas as fábricas:

```python
__all__ = ['HealingCreatureFactory', 'TransformCreatureFactory']

from .factory import HealingCreatureFactory, TransformCreatureFactory
```

---

## Builtins Utilizados

### `print()`
Usado em `capacitor.py` para exibir todos os resultados das ações das criaturas no terminal.

### `isinstance(objeto, Classe)`
Embora definido em `ex1`, o `isinstance` é um builtin essencial que será amplamente usado no Exercise 2 para verificar se uma criatura possui uma determinada capability:

```python
isinstance(creature, TransformCapability)  # True se a criatura tem essa capability
```
