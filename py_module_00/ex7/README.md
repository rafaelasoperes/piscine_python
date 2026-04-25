# Exercício 7 - ft_seed_inventory

## Descrição

A coordenadora do jardim precisa controlar o estoque de sementes com tipos de dados precisos. Neste exercício você vai criar a função `ft_seed_inventory`, que recebe o tipo de semente, a quantidade e a unidade de medida, e exibe a mensagem de inventário correspondente.

Este exercício introduz dois conceitos importantes: **métodos de string** (funções disponíveis em textos) e **anotações de tipo** (*type hints*), obrigatórias a partir deste exercício.

## Arquivo

`ft_seed_inventory.py`

## Assinatura da função

```python
def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
```

> **Atenção:** as anotações de tipo (`: str`, `: int`, `-> None`) são **obrigatórias** neste exercício. Verifique sua tipagem com o comando `mypy ft_seed_inventory.py`.

## Exemplos de uso

```python
ft_seed_inventory("tomato", 15, "packets")
# Tomato seeds: 15 packets available

ft_seed_inventory("carrot", 8, "grams")
# Carrot seeds: 8 grams total

ft_seed_inventory("lettuce", 12, "area")
# Lettuce seeds: covers 12 square meters

ft_seed_inventory("tomato", 5, "kilos")
# Unknown unit type
```

## Lógica de decisão

| Valor de `unit` | Mensagem exibida                                  |
|-----------------|---------------------------------------------------|
| `"packets"`     | `<Tipo> seeds: <quantidade> packets available`    |
| `"grams"`       | `<Tipo> seeds: <quantidade> grams total`          |
| `"area"`        | `<Tipo> seeds: covers <quantidade> square meters` |
| qualquer outro  | `Unknown unit type`                               |

## Funções e recursos autorizados

### `print()`

A função `print()` exibe a mensagem de inventário formatada na tela.

```python
print(f"{type} seeds: {quantity} packets available")
```

Usando f-strings, você insere os valores das variáveis diretamente na mensagem com `{variavel}`.

### Métodos de string

Strings em Python possuem **métodos embutidos** — funções que podem ser chamadas diretamente sobre um texto usando a notação de ponto (`.`).

Neste exercício você deve usar o método `.capitalize()`:

#### `.capitalize()`

Retorna uma nova string com a **primeira letra em maiúsculo** e todas as demais em minúsculo.

```python
"tomato".capitalize()   # → "Tomato"
"CARROT".capitalize()   # → "Carrot"
"lETTUCE".capitalize()  # → "Lettuce"
```

Isso garante que o nome da semente seja exibido corretamente, independentemente de como foi passado como argumento.

```python
type = seed_type.capitalize()  # padroniza a capitalização antes de exibir
```

### Anotações de tipo (*type hints*)

Type hints são **anotações** que indicam qual tipo de dado cada parâmetro recebe e qual tipo a função retorna. Elas não alteram o comportamento do código, mas ajudam a documentar e verificar a corretude dos tipos.

```python
def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
#                               ^^^            ^^^         ^^^     ^^^^
#                          espera str    espera int   espera str  não retorna nada
```

- `: str` — o parâmetro deve ser uma string.
- `: int` — o parâmetro deve ser um inteiro.
- `-> None` — a função não retorna nenhum valor (apenas imprime).

Para verificar se os tipos estão corretos, use o `mypy`:
```bash
mypy ft_seed_inventory.py
```

## Observações

- Escreva **apenas** a função, não um programa principal.
- A primeira letra do tipo de semente deve sempre estar em **maiúsculo** — use `.capitalize()`.
- Para unidades desconhecidas, exiba **apenas** `Unknown unit type`, sem nenhuma outra informação.
- As anotações de tipo são **obrigatórias** neste exercício.
- Não chame a função diretamente no arquivo.
- Não escreva código fora da função.
