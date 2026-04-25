# Exercício 1 - ft_garden_name

## Descrição

Neste exercício você vai criar uma função chamada `ft_garden_name` que pede ao usuário o nome de um jardim e, em seguida, exibe esse nome junto a uma mensagem de status fixa.

Este exercício introduz a leitura de dados digitados pelo usuário, combinando entrada (`input`) e saída (`print`) em uma mesma função.

## Arquivo

`ft_garden_name.py`

## Assinatura da função

```python
def ft_garden_name():
```

## Exemplo de uso

```
Enter garden name: Community Garden
Garden: Community Garden
Status: Growing well!
```

## Funções autorizadas

### `input()`

A função `input()` serve para **ler dados digitados pelo usuário** no terminal. Ela pausa a execução do programa e espera que o usuário escreva algo e pressione Enter.

```python
name = input("Enter garden name: ")  # exibe o texto e aguarda a digitação
```

Características importantes:

- O argumento passado para `input()` é o **texto que aparece como instrução** para o usuário (chamado de *prompt*).
- O valor retornado é **sempre uma string** (`str`), independentemente do que o usuário digitar.
- O valor digitado fica armazenado na variável atribuída e pode ser usado depois.

### `print()`

A função `print()` exibe informações na tela. Neste exercício ela é usada para mostrar o nome do jardim e a mensagem de status.

```python
print(f"Garden: {name}")   # exibe o nome capturado pelo input()
print("Status: Growing well!")  # mensagem fixa, sempre igual
```

- Textos entre aspas são exibidos literalmente.
- Usando f-strings (`f"..."`), você pode inserir o valor de variáveis diretamente no texto com `{variavel}`.

## Observações

- Escreva **apenas** a função, não um programa principal.
- A mensagem `"Status: Growing well!"` é **fixa** e deve ser exibida exatamente como mostrada, independentemente do nome digitado.
- Não chame a função diretamente no arquivo.
- Não escreva código fora da função.
