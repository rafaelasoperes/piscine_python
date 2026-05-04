# Exercise 1 — Higher Realm

## Arquivo: `higher_magic.py`

Este exercício explora o conceito de **funções de ordem superior** (*higher-order functions*): funções que recebem outras funções como argumento e/ou retornam novas funções. Também aborda o uso correto de `Callable` e da função built-in `callable()`.

---

## Funções autorizadas e explicações

### `Callable` (de `collections.abc`)

`Callable` é um tipo usado em **anotações de tipo** para indicar que um parâmetro ou retorno é uma função (ou qualquer objeto que possa ser chamado com `()`).

```python
from collections.abc import Callable

def aplicar(func: Callable, valor: int) -> int:
    return func(valor)
```

**Por que usar `collections.abc` e não `typing`?**
A partir do Python 3.9+, `typing.Callable` foi marcado como obsoleto em favor de `collections.abc.Callable`, que é a implementação real da interface. O módulo `typing` apenas re-exportava o tipo — usar `collections.abc` é mais correto e direto.

---

### `callable(objeto)`

Função built-in que retorna `True` se o objeto pode ser chamado como uma função (possui o método `__call__`), e `False` caso contrário.

```python
callable(len)        # True — len é uma função
callable(42)         # False — inteiros não são chamáveis
callable(lambda: 1)  # True — lambdas são chamáveis

class Mago:
    def __call__(self):
        return "invocado!"

callable(Mago())     # True — instância com __call__
```

É útil para validar dinamicamente se um argumento recebido é realmente uma função antes de invocá-lo.

---

### Funções de ordem superior (Higher-Order Functions)

Uma função de ordem superior é qualquer função que:
- **Recebe** uma ou mais funções como argumento, e/ou
- **Retorna** uma função como resultado.

Isso é possível porque em Python **funções são cidadãos de primeira classe**: podem ser atribuídas a variáveis, passadas como argumentos e retornadas de outras funções, exatamente como inteiros ou strings.

```python
# Função que recebe outra função
def aplicar_dobro(func: Callable, x: int) -> int:
    return func(x * 2)

# Função que retorna outra função
def multiplicador(n: int) -> Callable:
    def multiplicar(x: int) -> int:
        return x * n
    return multiplicar

vezes3 = multiplicador(3)
vezes3(10)  # 30
```

---

## Resumo das funções implementadas

| Função | Descrição |
|---|---|
| `spell_combiner(spell1, spell2)` | Retorna uma nova função que executa dois feitiços e devolve uma tupla com ambos os resultados |
| `power_amplifier(base_spell, multiplier)` | Retorna um novo feitiço que multiplica o poder antes de lançar |
| `conditional_caster(condition, spell)` | Retorna um feitiço que só é lançado se a condição for verdadeira; caso contrário retorna `"Spell fizzled"` |
| `spell_sequence(spells)` | Retorna uma função que executa todos os feitiços da lista em ordem e devolve uma lista de resultados |

---

## Conceitos-chave

**Como funções de ordem superior promovem reuso de código?**
Ao separar *o que fazer* (a lógica do feitiço) de *como modificar o comportamento* (amplificar, combinar, condicionar), é possível criar modificadores genéricos que funcionam com qualquer feitiço, sem precisar reescrever código.

**O que torna funções "cidadãos de primeira classe" em Python?**
O fato de que funções são objetos como qualquer outro: podem ser armazenadas em variáveis, passadas como argumentos, retornadas de outras funções e guardadas em estruturas de dados como listas e dicionários.
