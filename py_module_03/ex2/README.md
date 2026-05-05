# Exercise 2 — Position Tracker

**Arquivo:** `ft_coordinate_system.py`

---

## Funções autorizadas e explicações

### `import math` / `math.sqrt()`

O módulo `math` fornece funções matemáticas. `math.sqrt()` calcula a **raiz quadrada** de um número, sendo essencial para a fórmula da distância euclidiana.

```python
import math

resultado = math.sqrt(16)   # 4.0
resultado = math.sqrt(2)    # 1.4142135623730951
```

A distância euclidiana entre dois pontos 3D usa `math.sqrt()` assim:

```python
dist = math.sqrt(
    (x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2
)
```

---

### `input()`

`input()` pausa o programa e aguarda que o usuário **digite algo e pressione Enter**. O valor digitado é sempre retornado como uma **string**.

```python
texto = input("Digite algo: ")
# O usuário digita: 1.0,2.5,3.0
# texto == '1.0,2.5,3.0'
```

Neste exercício é usado em um loop para pedir as coordenadas repetidamente até que sejam válidas.

---

### `round()`

`round()` arredonda um número para um determinado número de casas decimais.

```python
round(3.14159, 2)    # 3.14
round(4.03112, 4)    # 4.0311
```

Usado para exibir as distâncias com 4 casas decimais.

---

### `print()`

Exibe textos e valores no terminal.

```python
print(f"Got a first tuple: {pos1}")
print(f"Distance to center: {round(dist_center, 4)}")
```

---

### Bloco `try / except ValueError`

Permite capturar o erro de conversão quando o usuário digita algo que não pode ser convertido para `float`, sem travar o programa.

```python
try:
    valor = float("abc")   # lança ValueError
except ValueError as e:
    print(f"Error on parameter 'abc': {e}")
    raise   # re-lança para que o loop externo reinicie a pergunta
```

---

## Conceito: Distância Euclidiana

A distância euclidiana é a medida da linha reta entre dois pontos no espaço. É a extensão 3D do **Teorema de Pitágoras**:

```
distância = √( (x2-x1)² + (y2-y1)² + (z2-z1)² )
```

Para a distância até o centro (0, 0, 0):

```
distância = √( x² + y² + z² )
```

---

## Fluxo do programa

1. Chama `get_player_pos()` para obter o primeiro conjunto de coordenadas.
2. Exibe a tupla e cada coordenada individualmente.
3. Calcula a distância até o centro (0, 0, 0) com `math.sqrt()`.
4. Chama `get_player_pos()` novamente para o segundo conjunto.
5. Calcula e exibe a distância entre os dois pontos.

### Sobre as Tuplas

As coordenadas são armazenadas em **tuplas** — estruturas imutáveis e ordenadas. Uma vez criadas, seus valores não podem ser alterados, o que garante que as coordenadas capturadas permaneçam intactas durante os cálculos.

```python
pos1 = (1.0, 2.5, 3.0)
x = pos1[0]   # 1.0
y = pos1[1]   # 2.5
z = pos1[2]   # 3.0
```
