# Exercise 1 — ft_garden_data

## Descrição

Programa que organiza dados de múltiplas plantas usando uma classe `Plant`.
Introduz o conceito de **Programação Orientada a Objetos (POO)** com atributos e métodos.

---

## Funções autorizadas

### `print()`

Função nativa do Python que exibe uma mensagem no terminal.

**Sintaxe:**
```python
print(valor)
print(f"texto {variavel}")
```

**Como é usada neste exercício:**

Exibe o cabeçalho do registro e chama o método `show()` de cada planta, que internamente usa `return` para montar a string exibida pelo `print()` no loop.

```python
print("=== Garden Plant Registry ===")

for i in garden:
    print(i.show())
```

**Por que usar `print()`?**

É a forma de apresentar ao usuário os dados armazenados nos objetos da classe `Plant`. Sem `print()`, nenhuma informação apareceria no terminal.

---

## Conceitos de classe usados neste exercício

### `class Plant`

Define um modelo (molde) para criar objetos que representam plantas. Cada planta criada a partir da classe é chamada de **instância**.

```python
class Plant:
    def __init__(self, name: str, heigth: float, age: int):
        self.name = name
        self.heigth = heigth
        self.age = age
```

### `__init__()`

Método especial chamado automaticamente ao criar uma instância da classe. Inicializa os atributos do objeto.

### `show()`

Método da classe que retorna uma string formatada com os dados da planta.

```python
def show(self):
    return f"{self.name}: {self.heigth}cm, {self.age} days old"
```

### Instanciação e lista de objetos

```python
rose = Plant("Rose", 25, 30)
garden = [rose, sunflower, cactus]
```

Cada planta é criada passando os valores diretamente ao construtor. A lista `garden` permite iterar sobre todas as plantas e exibir seus dados de forma organizada.
