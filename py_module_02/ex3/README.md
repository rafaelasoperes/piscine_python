# Exercise 3 — ft_custom_errors

## Descrição

Criação de tipos de erro personalizados para o sistema de jardim. Quando os erros do Python não são específicos o suficiente para descrever um problema de domínio, é possível criar suas próprias classes de exceção, tornando o código mais expressivo e fácil de depurar.

---

## Funções autorizadas

### `print()`

Exibe uma mensagem no terminal (saída padrão).

**Sintaxe:**
```python
print(valor)
print(f"Texto {variavel}")
```

**Comportamento:**
- Aceita qualquer tipo de dado e exibe como texto.
- Com f-strings, permite inserir variáveis e expressões diretamente na mensagem.

**Exemplos:**
```python
print("Testing PlantError...")
print(f"Caught PlantError: {error}")
print(f"Caught GardenError: {error}")
```

**Como é usada neste exercício:**

`print()` é usada em `test_custom_errors()` para indicar qual tipo de erro está sendo testado e exibir a mensagem capturada em cada bloco `except`, demonstrando que tanto os erros específicos (`PlantError`, `WaterError`) quanto o erro base (`GardenError`) são capturados corretamente.

---

## Conceitos centrais deste exercício

### Criação de exceções personalizadas

Uma exceção personalizada é uma classe que herda de `Exception` (ou de outra exceção). O método `__init__` recebe uma mensagem e a repassa para a classe pai com `super().__init__()`:

```python
class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)
```

O parâmetro `message` com valor padrão garante que a exceção pode ser lançada sem argumento e ainda terá uma mensagem significativa.

### Hierarquia de exceções

`PlantError` e `WaterError` herdam de `GardenError`, que por sua vez herda de `Exception`. Isso cria uma hierarquia:

```
Exception
└── GardenError
    ├── PlantError
    └── WaterError
```

**Benefício:** capturar `GardenError` captura automaticamente `PlantError` e `WaterError`, pois elas são subclasses. Isso permite tratar erros de forma granular ou agrupada conforme a necessidade.

### `raise` para lançar exceções personalizadas

```python
raise PlantError("The tomato plant is wilting!")
raise WaterError("Not enough water in the tank!")
```

### `except` com tipos específicos ou base

```python
except PlantError as error:   # captura apenas PlantError
except WaterError as error:   # captura apenas WaterError
except GardenError as error:  # captura PlantError E WaterError
```

---

## Quando criar seus próprios tipos de erro?

Crie exceções personalizadas quando:
- O erro representa um problema específico do domínio da aplicação (jardim, finanças, etc.)
- Você precisa que diferentes partes do código reajam de forma diferente a erros distintos
- As mensagens de erro padrão do Python não são suficientemente descritivas para o contexto

---

## Exemplo de saída esperada

```
=== Custom Garden Errors Demo ===

Testing PlantError...
Caught PlantError: The tomato plant is wilting!

Testing WaterError...
Caught WaterError: Not enough water in the tank!

Testing catching all garden errors...
Caught GardenError: The tomato plant is wilting!
Caught GardenError: Not enough water in the tank!

All custom error types work correctly!
```
