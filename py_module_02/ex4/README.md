# Exercise 4 — ft_finally_block

## Descrição

Garantia de limpeza de recursos com o bloco `finally`. Em sistemas de irrigação real, é fundamental fechar válvulas e liberar conexões mesmo quando um erro ocorre no meio do processo. O bloco `finally` garante que o código de limpeza **sempre** é executado, independentemente do que aconteça no bloco `try`.

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
- Usado para simular a abertura/fechamento do sistema de irrigação e o resultado de cada planta regada.

**Exemplos:**
```python
print("Opening watering system")
print(f"Watering {plant_name}: [OK]")
print(f"Caught PlantError: {error}")
print("Closing watering system\n")
```

**Como é usada neste exercício:**

`print()` simula as operações do sistema: abertura e fechamento da válvula de irrigação, confirmação de rega bem-sucedida, mensagem de erro quando o nome da planta é inválido, e a mensagem de encerramento que aparece **sempre** — inclusive em caso de erro — demonstrando o comportamento do `finally`.

---

### `str.capitalize()`

Retorna uma cópia da string com o primeiro caractere em maiúsculo e os demais em minúsculo.

**Sintaxe:**
```python
string.capitalize()
```

**Comportamento:**
- Transforma o primeiro caractere para maiúsculo.
- Transforma todos os demais caracteres para minúsculo.
- Não modifica a string original (strings são imutáveis em Python).

**Exemplos:**
```python
"tomato".capitalize()   # retorna "Tomato"
"Tomato".capitalize()   # retorna "Tomato"
"TOMATO".capitalize()   # retorna "Tomato"
"lettuce".capitalize()  # retorna "Lettuce"
```

**Como é usada neste exercício:**

Em `water_plant()`, a string recebida é comparada com sua própria versão capitalizada. Se forem iguais, o nome está correto. Se forem diferentes, o nome não está capitalizado e um `PlantError` é lançado:

```python
if plant_name != plant_name.capitalize():
    raise PlantError(f"Invalid plant name to water: '{plant_name}'")
```

Isso valida que nomes de plantas seguem a convenção de iniciar com letra maiúscula — `"Tomato"` é válido, `"lettuce"` não é.

---

## O bloco `finally` neste exercício

O `finally` é executado **sempre**, mesmo quando o `except` chama `return`. Isso é o comportamento central que o exercício demonstra:

```python
def test_watering_system(plants: list[str]) -> None:
    print("Opening watering system")
    try:
        for plant in plants:
            water_plant(plant)
    except PlantError as error:
        print(f"Caught PlantError: {error}")
        print(".. ending tests and returning to main")
        return          # mesmo retornando aqui...
    finally:
        print("Closing watering system\n")   # ...isso sempre executa
```

**Por que isso importa?**

Em sistemas reais — conexões de banco de dados, arquivos abertos, válvulas de irrigação — se o recurso não for fechado corretamente após um erro, pode causar vazamentos de memória, dados corrompidos ou danos físicos ao equipamento.

---

## Fluxo do programa

```
Plantas válidas: ["Tomato", "Lettuce", "Carrots"]
  → Opening watering system
  → Watering Tomato: [OK]
  → Watering Lettuce: [OK]
  → Watering Carrots: [OK]
  → finally: Closing watering system  ✓

Plantas inválidas: ["Tomato", "lettuce", "Carrots"]
  → Opening watering system
  → Watering Tomato: [OK]
  → "lettuce" != "Lettuce"  →  PlantError
  → except: imprime erro e chama return
  → finally: Closing watering system  ✓  (mesmo com return!)
```

---

## Exemplo de saída esperada

```
=== Garden Watering System ===

Testing valid plants...
Opening watering system
Watering Tomato: [OK]
Watering Lettuce: [OK]
Watering Carrots: [OK]
Closing watering system

Testing invalid plants...
Opening watering system
Watering Tomato: [OK]
Caught PlantError: Invalid plant name to water: 'lettuce'
.. ending tests and returning to main
Closing watering system

Cleanup always happens, even with errors!
```
