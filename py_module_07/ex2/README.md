# Exercise 2 — Abstract Strategy

**Arquivos:** `tournament.py`, pacote `ex2/` (`strategy.py`, `__init__.py`)
**Autorizados:** `builtins`, tipos padrão, `import typing`, `import abc`

---

## Padrão de Projeto: Strategy

O padrão **Strategy** permite definir uma família de algoritmos, encapsular cada um deles em uma classe separada e torná-los intercambiáveis. Aqui, cada `BattleStrategy` encapsula um comportamento de combate diferente, e o código do torneio não precisa saber qual estratégia está sendo usada — ele apenas chama `strategy.act(creature)`.

Isso evita uma cadeia de `if/elif` no código do torneio para tratar cada tipo de criatura separadamente.

---

## Módulo `abc` — Classes Abstratas

### `ABC` e `@abstractmethod`
Usados para definir `BattleStrategy` como contrato que toda estratégia concreta deve implementar.

```python
from abc import ABC, abstractmethod

class BattleStrategy(ABC):

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass

    @abstractmethod
    def act(self, creature: Creature) -> None:
        pass
```

`is_valid` verifica se a criatura é compatível com a estratégia antes do combate.
`act` executa as ações de combate da estratégia sobre a criatura.

---

## Módulo `typing` — Anotações de Tipo

### `cast(Tipo, objeto)`
Função importada de `typing` que **não altera o objeto em tempo de execução**, mas informa ao verificador de tipos (`mypy`) que o objeto deve ser tratado como um tipo específico. É usado quando sabemos (pelo `isinstance`) que o objeto possui certos métodos, mas o tipo estático declarado não os inclui.

```python
from typing import cast

creature_copy = cast(TransformCapability, creature)
print(creature_copy.transform())
print(creature_copy.revert())
```

Aqui, `creature` é do tipo `Creature` (que não tem `transform`), mas após validar com `isinstance`, usamos `cast` para acessar os métodos de `TransformCapability` sem erros de tipo.

### `List` e `Tuple`
Usados em `tournament.py` para anotar coleções com tipos internos explícitos.

```python
from typing import List, Tuple

def create_combat_list(
    raw_list: List[Tuple[CreatureFactory, BattleStrategy]]
) -> List[Tuple]:
    ...
```

`List[X]` indica uma lista cujos elementos são do tipo `X`.
`Tuple[X, Y]` indica uma tupla com elementos dos tipos `X` e `Y` nessa ordem.

---

## Builtin `isinstance(objeto, Classe)`

Função embutida que verifica em tempo de execução se um objeto é instância de uma determinada classe (ou subclasse). É o mecanismo central do método `is_valid` em cada estratégia.

```python
# AggressiveStrategy — válida apenas para criaturas com TransformCapability:
def is_valid(self, creature: Creature) -> bool:
    if isinstance(creature, TransformCapability):
        return True
    return False

# DefensiveStrategy — válida apenas para criaturas com HealCapability:
def is_valid(self, creature: Creature) -> bool:
    if isinstance(creature, HealCapability):
        return True
    return False

# NormalStrategy — válida para qualquer criatura:
def is_valid(self, creature: Creature) -> bool:
    return True
```

---

## Exceções com `raise Exception`

Quando `act` é chamado com uma combinação inválida de criatura e estratégia, uma exceção é levantada com uma mensagem clara. O `raise` é um builtin do Python.

```python
def act(self, creature: Creature) -> None:
    if not self.is_valid(creature):
        raise Exception(
            "Battle error, aborting tournament: "
            f"Invalid Creature '{creature.__class__.__name__}' "
            "for this aggressive strategy"
        )
    ...
```

### `creature.__class__.__name__`
Atributo especial (dunder) disponível em todo objeto Python. Retorna o nome da classe do objeto como string — útil para compor mensagens de erro informativas sem importar nada extra.

---

## Tratamento de Exceções: `try / except / finally`

Em `tournament.py`, o torneio captura as exceções levantadas pelas estratégias inválidas, imprime a mensagem de erro e continua a execução normalmente.

```python
try:
    strategy1.act(adversary1)
    strategy2.act(adversary2)
except Exception as err:
    print(err)
finally:
    print()
```

`try` — bloco que pode levantar uma exceção.
`except Exception as err` — captura qualquer exceção e armazena em `err`.
`finally` — executado **sempre**, com ou sem exceção. Aqui garante uma linha em branco entre batalhas.

---

## As Três Estratégias Concretas

### `NormalStrategy`
Compatível com qualquer criatura. Simplesmente chama `attack`.

```python
def act(self, creature: Creature) -> None:
    print(creature.attack())
```

### `AggressiveStrategy`
Compatível apenas com criaturas que possuem `TransformCapability`. Sequência: `transform → attack → revert`.

```python
creature_copy = cast(TransformCapability, creature)
print(creature_copy.transform())
print(creature.attack())
print(creature_copy.revert())
```

### `DefensiveStrategy`
Compatível apenas com criaturas que possuem `HealCapability`. Sequência: `attack → heal`.

```python
creature_copy = cast(HealCapability, creature)
print(creature.attack())
print(creature_copy.heal())
```

---

## Função `create_combat_list` em `tournament.py`

Monta todas as combinações de duplas de combate sem repetição (cada par luta apenas uma vez).

```python
for adversary1 in battle_list:
    for adversary2 in battle_list:
        if (
            adversary1 is not adversary2
            and (adversary2, adversary1) not in combat_list
        ):
            combat_list.append((adversary1, adversary2))
```

`is not` — operador builtin que verifica identidade de objeto (não igualdade de valor). Garante que uma criatura não lute contra si mesma.
`not in` — operador builtin que verifica ausência em uma sequência. Evita duplicar pares invertidos.

---

## Builtins Utilizados

| Builtin | Uso |
|---|---|
| `print()` | Exibir resultados das batalhas |
| `isinstance()` | Verificar capability da criatura em `is_valid` |
| `raise` | Levantar exceção em combinação inválida |
| `len()` | Exibir número de oponentes no torneio |
| `is not` | Evitar que criatura lute contra si mesma |
| `not in` | Evitar duplicação de pares de combate |
