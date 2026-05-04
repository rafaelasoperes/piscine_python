# Exercise 4 — Master's Tower

## Arquivo: `decorator_mastery.py`

Este exercício aborda a criação de **decoradores** — funções que envolvem outras funções para modificar ou estender seu comportamento — e o uso de `@staticmethod` em classes. Também utiliza `functools.wraps` para preservar os metadados da função original.

---

## Ferramentas autorizadas e explicações

### `functools.wraps`

Quando se cria um decorador, o wrapper substitui a função original. Isso faz com que atributos importantes como `__name__`, `__doc__` e `__module__` sejam perdidos. `functools.wraps` corrige isso copiando os metadados da função original para o wrapper.

```python
import functools

def meu_decorador(func):
    @functools.wraps(func)       # preserva __name__, __doc__, etc.
    def wrapper(*args, **kwargs):
        print("antes")
        result = func(*args, **kwargs)
        print("depois")
        return result
    return wrapper

@meu_decorador
def saudacao():
    """Diz olá."""
    print("Olá!")

saudacao.__name__  # "saudacao" (não "wrapper")
saudacao.__doc__   # "Diz olá."
```

Sem `@functools.wraps`, `saudacao.__name__` retornaria `"wrapper"`, o que dificulta debugging e introspecção.

---

### Decoradores

Um decorador é uma função que **recebe uma função** e **retorna uma nova função** com comportamento modificado. A sintaxe `@decorador` é açúcar sintático para `func = decorador(func)`.

```python
# Estas duas formas são equivalentes:

@spell_timer
def fireball():
    ...

# é o mesmo que:
def fireball():
    ...
fireball = spell_timer(fireball)
```

**Decoradores com parâmetros (fábricas de decoradores):**
Quando o decorador precisa de argumentos próprios, adiciona-se uma camada extra:

```python
def power_validator(min_power: int):   # nível 1: recebe o parâmetro
    def decorator(func):               # nível 2: recebe a função
        @functools.wraps(func)
        def wrapper(power, *args, **kwargs):  # nível 3: envolve a chamada
            if power < min_power:
                return "Insufficient power for this spell"
            return func(power, *args, **kwargs)
        return wrapper
    return decorator

@power_validator(min_power=10)
def cast(power: int) -> str:
    return f"Spell cast with {power} power"
```

**Separação de responsabilidades com decoradores:**
Decoradores permitem separar lógica transversal (logging, validação, retry, timing) da lógica principal da função. A função `fireball` não precisa saber que está sendo cronometrada — essa responsabilidade fica isolada no decorador `spell_timer`.

---

### `@staticmethod`

Um método estático pertence à **classe** e não a uma instância específica. Não recebe `self` (instância) nem `cls` (classe) como primeiro argumento. É chamado diretamente na classe ou na instância.

```python
class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return len(name) >= 3 and all(c.isalpha() or c == ' ' for c in name)

# Chamada sem instanciar a classe:
MageGuild.validate_mage_name("Merlin")   # True

# Também pode ser chamado em uma instância:
guild = MageGuild()
guild.validate_mage_name("X2")           # False
```

**Diferença entre `@staticmethod` e método de instância:**

| Método de instância | `@staticmethod` |
|---|---|
| Recebe `self` automaticamente | Não recebe `self` nem `cls` |
| Acessa e modifica o estado da instância | Não acessa estado da instância ou da classe |
| Requer uma instância para ser chamado (ou acesso via classe passando instância) | Pode ser chamado diretamente na classe |
| Usado para lógica que depende dos dados do objeto | Usado para lógica utilitária relacionada à classe mas independente de estado |

---

## Resumo das funções implementadas

| Função / Método | Ferramenta principal | Descrição |
|---|---|---|
| `spell_timer(func)` | `functools.wraps` | Decorador que mede e imprime o tempo de execução da função |
| `power_validator(min_power)` | `functools.wraps` | Fábrica de decoradores que valida se o poder mínimo foi atingido antes de executar |
| `retry_spell(max_attempts)` | `functools.wraps` | Fábrica de decoradores que reexecuta a função em caso de exceção, até o limite de tentativas |
| `MageGuild.validate_mage_name` | `@staticmethod` | Método estático que valida se um nome de mago contém apenas letras/espaços e tem 3+ caracteres |
| `MageGuild.cast_spell` | `@power_validator` | Método de instância que usa o decorador de validação de poder |
