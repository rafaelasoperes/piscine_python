# Exercise 5 — ft_plant_types

## Descrição

Introduz **herança** em Python: classes especializadas (`Flower`, `Tree`, `Vegetable`)
herdam os atributos e métodos da classe base `Plant`, adicionando comportamentos e
atributos próprios sem duplicar código.

---

## Funções autorizadas

### `super()`

Função nativa que permite acessar métodos e o construtor da **classe pai** (superclasse) a partir de uma classe filha.

**Sintaxe:**
```python
super().__init__(argumentos)   # chama o construtor da classe pai
super().metodo()               # chama um método da classe pai
```

**Como é usada neste exercício:**

Em todas as subclasses, `super().__init__()` é chamado para inicializar os atributos comuns herdados de `Plant`, sem reescrever esse código:

```python
class Flower(Plant):
    def __init__(self, name: str, heigth: float, age: int, color):
        super().__init__(name, heigth, age)  # inicializa name, height, days
        self.color: str = color
        self.isValid: bool = False
```

Também é usado no método `show()` das subclasses para reaproveitar a exibição base de `Plant`:

```python
def show(self):
    super().show()          # imprime: "Rose:15.0cm, 30 days old"
    print(f" Color: {self.color}")
```

**Por que usar `super()`?**

Evita duplicação de código. Sem `super()`, cada subclasse precisaria repetir toda a lógica de inicialização e exibição da classe pai, tornando o código difícil de manter.

---

### `print()`

Função nativa que exibe uma mensagem no terminal.

**Como é usada neste exercício:**

Usada diretamente nos métodos `show()` das subclasses para exibir atributos específicos de cada tipo de planta, além de mensagens descritivas no `main()`.

```python
print(f" Color: {self.color}")
print(f" Trunk diameter: {self.trunk_diameter}cm")
print(f" Harvest season: {self.harvest}")
print(f" Nutritional value: {self._nutritional}")
```

---

### `range()`

Função nativa que gera uma sequência de números inteiros.

**Sintaxe:**
```python
range(início, fim)
```

**Como é usada neste exercício:**

Usada no setter `set_nutritional()` da classe `Vegetable` para simular dias de crescimento em loop:

```python
def set_nutritional(self, value):
    i = 0
    while i < value:
        super().age()
        super().grow(2.1)
        i += 1
    self._nutritional = value
```

---

### `round()`

Função nativa que arredonda números de ponto flutuante.

**Sintaxe:**
```python
round(numero, casas_decimais)
```

**Como é usada neste exercício:**

Garante precisão de 1 casa decimal ao crescer a planta:

```python
def grow(self, value):
    self.height = round(self.height + value, 1)
```

---

## Conceito principal: Herança

A herança permite que uma classe filha reutilize tudo que a classe pai já definiu:

```
Plant
├── Flower  (+ color, bloom())
│   └── (pode ser estendida futuramente)
├── Tree    (+ trunk_diameter, produce_shade())
└── Vegetable (+ harvest, nutritional_value, set_nutritional())
```

Cada subclasse **sobrescreve** (`override`) o método `show()` para incluir seus dados extras, mas chama `super().show()` para não perder a exibição dos dados básicos da planta.
