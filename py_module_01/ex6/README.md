# Exercise 6 — ft_garden_analytics

## Descrição

Exercício final que integra todos os conceitos anteriores e adiciona:
**métodos estáticos**, **métodos de classe**, **classes aninhadas** (nested classes),
**cadeia de herança** e uma **função standalone** para exibir estatísticas de qualquer planta.

---

## Funções autorizadas

### `super()`

Acessa métodos e o construtor da classe pai.

**Como é usada neste exercício:**

Todas as subclasses (`Flower`, `Tree`, `Seed`) chamam `super().__init__()` e `super().show()` para reaproveitar a lógica da classe pai. A classe `TreeStats` herda de `Plant.Stats` e usa `super().display()`:

```python
class TreeStats(Plant.Stats):
    def display(self):
        super().display()           # exibe: "Stats: X grow, X age, X show"
        print(f" {self.shade_count} shade")
```

A cadeia de herança de `Seed` passa por `Flower` → `Plant`:

```python
class Seed(Flower):
    def __init__(self, name, height, age, color) -> None:
        super().__init__(name, height, age, color)
```

---

### `print()`

Exibe mensagens no terminal.

**Como é usada neste exercício:**

Usada em todos os métodos `show()`, `display()` das stats, `produce_shade()`, e nas mensagens descritivas do `main()`.

```python
print(f"Stats: {self.grow_count} grow, {self.age_count} age, "
      f"{self.show_count} show")
```

---

### `range()`

Gera sequências numéricas para loops.

**Sintaxe:**
```python
range(início, fim)
```

Disponível para uso em iterações numéricas quando necessário.

---

### `round()`

Arredonda valores de ponto flutuante.

**Como é usada neste exercício:**

Garante precisão de 1 casa decimal na altura ao inicializar e ao crescer plantas:

```python
self.height: float = round(height, 1)
self.trunk: float = round(trunk, 1)
```

---

### `staticmethod()`

Decorator que define um **método estático**: pertence à classe, mas não recebe `self` nem `cls`. Não acessa nem modifica o estado de nenhuma instância.

**Sintaxe:**
```python
@staticmethod
def nome_do_metodo(parametros):
    ...
```

**Como é usada neste exercício:**

Cria o método `is_older_than_year()` na classe `Plant`, que verifica se uma quantidade de dias supera um ano. Pode ser chamado diretamente pela classe, sem criar uma instância:

```python
@staticmethod
def is_older_than_year(days):
    return days > 365

# Uso:
Plant.is_older_than_year(30)   # False
Plant.is_older_than_year(400)  # True
```

**Por que usar `staticmethod`?**

Quando a lógica está relacionada à classe conceitualmente, mas não depende de nenhum dado de instância. Agrupa funções utilitárias dentro da classe sem exigir a criação de um objeto.

---

### `classmethod()`

Decorator que define um **método de classe**: recebe a própria classe como primeiro argumento (`cls`), em vez de uma instância (`self`). Pode criar instâncias da classe.

**Sintaxe:**
```python
@classmethod
def nome_do_metodo(cls, parametros):
    ...
```

**Como é usada neste exercício:**

Cria o método `create_anonymous()`, que instancia uma planta com valores padrão sem exigir que o chamador forneça informações:

```python
@classmethod
def create_anonymous(cls):
    return cls("Unknown plant", 0.0, 0)

# Uso:
anon = Plant.create_anonymous()
```

**Por que usar `classmethod`?**

É ideal para **fábricas alternativas** de criação de objetos. Usando `cls` em vez de `Plant` diretamente, o método funciona corretamente mesmo quando subclasses o herdam.

---

## Conceitos adicionais deste exercício

### Classe aninhada (nested class) — `Stats`

Uma classe definida dentro de outra. Organiza dados que pertencem exclusivamente àquela classe pai:

```python
class Plant:
    class Stats:
        def __init__(self) -> None:
            self.grow_count: int = 0
            self.age_count: int = 0
            self.show_count: int = 0

        def display(self):
            print(f"Stats: {self.grow_count} grow, ...")
```

Cada instância de `Plant` cria seu próprio objeto `Stats`:

```python
self.stats = self.Stats()
```

### Herança de classe aninhada — `TreeStats`

`Tree` define `TreeStats` que herda de `Plant.Stats`, adicionando o contador de sombras:

```python
class Tree(Plant):
    class TreeStats(Plant.Stats):
        def __init__(self) -> None:
            super().__init__()
            self.shade_count: int = 0
```

### Função standalone — `display_any_plant_stats()`

Função fora de qualquer classe que aceita qualquer tipo de planta e exibe suas estatísticas. Demonstra **polimorfismo**: funciona para `Flower`, `Tree`, `Seed` ou `Plant` sem distinção:

```python
def display_any_plant_stats(plant):
    print(f"[statistics for {plant.name}]")
    plant.stats.display()
```
