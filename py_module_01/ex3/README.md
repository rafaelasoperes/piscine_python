# Exercise 3 — ft_plant_factory

## Descrição

Programa que cria múltiplas plantas de forma eficiente a partir de uma lista de dados brutos,
usando o construtor da classe `Plant` para instanciar e inicializar cada objeto ao mesmo tempo.

---

## Funções autorizadas

### `print()`

Função nativa do Python que exibe uma mensagem no terminal.

**Como é usada neste exercício:**

Exibe o cabeçalho da fábrica e o resultado do método `show()` de cada planta criada.

```python
print("=== Plant Factory Output ===")

for plant in garden:
    print(plant.show())
```

---

### `range()`

Função nativa que gera uma sequência de números inteiros.

**Sintaxe:**
```python
range(início, fim)
range(fim)
```

**Como é usada neste exercício:**

Disponível para uso em loops de iteração. Neste arquivo é utilizada implicitamente por meio do `for` que percorre a lista `raw_data` e a lista `garden`.

**Por que usar `range()`?**

Permite controlar iterações numéricas quando é necessário acessar índices ou repetir operações um número fixo de vezes.

---

### `round()`

Função nativa que arredonda um número de ponto flutuante.

**Sintaxe:**
```python
round(numero, casas_decimais)
```

**Como é usada neste exercício:**

Garante que a altura da planta seja armazenada com precisão de 1 casa decimal no momento da criação do objeto.

```python
def __init__(self, name: str, height: float, age: int, grow_plant=0):
    self.height = round(height, 1)
```

**Por que usar `round()`?**

Padroniza a precisão numérica dos valores de altura logo na criação do objeto, evitando inconsistências de exibição ao longo do programa.

---

## Conceito principal: construtor com parâmetros (`__init__`)

Neste exercício, a instanciação e a inicialização acontecem **ao mesmo tempo**, passando todos os dados diretamente ao criar o objeto:

```python
raw_data = [
    ("Rose", 25.0, 30, 0),
    ("Oak", 200.0, 365, 0),
    ...
]

garden = []
for data in raw_data:
    name, height, age, grow = data
    garden.append(Plant(name, height, age, grow))
```

Isso é chamado de **fábrica de objetos** — uma forma eficiente de criar múltiplas instâncias sem repetir código de inicialização manualmente.
