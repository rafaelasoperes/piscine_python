# Exercise 2 — ft_plant_growth

## Descrição

Simulador de crescimento de plantas ao longo de uma semana.
A classe `Plant` ganha métodos `grow()` e `age()` para modificar o estado do objeto ao longo do tempo.

---

## Funções autorizadas

### `print()`

Função nativa do Python que exibe uma mensagem no terminal.

**Como é usada neste exercício:**

Exibe o estado diário da planta durante a simulação e o resumo de crescimento ao final da semana.

```python
print("=== Garden Plant Growth ===")
print(rose.get_info())

for day in range(1, 8):
    rose.grow()
    rose.age()
    print(f"=== Day {day} ===")
    print(rose.get_info())

print(f"Growth this week: {growth_total}cm")
```

---

### `range()`

Função nativa que gera uma sequência de números inteiros.

**Sintaxe:**
```python
range(início, fim)        # início incluso, fim excluso
range(fim)                # começa em 0
range(início, fim, passo) # com passo definido
```

**Como é usada neste exercício:**

Controla o loop de 7 dias da simulação, gerando os valores de 1 a 7 (inclusive).

```python
for day in range(1, 8):
    rose.grow()
    rose.age()
```

**Por que usar `range()`?**

Permite repetir um bloco de código um número definido de vezes sem precisar escrever cada iteração manualmente. É a forma padrão de criar loops contados em Python.

---

### `round()`

Função nativa que arredonda um número de ponto flutuante para um número definido de casas decimais.

**Sintaxe:**
```python
round(numero, casas_decimais)
```

**Como é usada neste exercício:**

Arredonda a altura da planta para 1 casa decimal ao exibir e ao calcular o crescimento total da semana.

```python
def get_info(self):
    return f"{self.name}: {round(self.height, 1)} cm, {self.days} days old"

growth_total = round(rose.height - rose.initial_height, 1)
```

**Por que usar `round()`?**

Operações com ponto flutuante em Python podem gerar resultados com muitas casas decimais imprecisas (ex: `0.30000000004`). O `round()` garante uma apresentação limpa e legível dos valores numéricos.
