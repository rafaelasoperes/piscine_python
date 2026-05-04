# Exercise 0 — ft_garden_intro

## Descrição

Programa introdutório que exibe informações sobre uma planta no jardim.
Apresenta o padrão `if __name__ == "__main__"` e o uso de variáveis simples com tipo.

---

## Funções autorizadas

### `print()`

Função nativa do Python que exibe uma mensagem no terminal (saída padrão).

**Sintaxe:**
```python
print(valor)
print(f"texto {variavel}")
```

**Como é usada neste exercício:**

Exibe o cabeçalho do jardim e os dados da planta (nome, altura e idade) formatados com f-strings.

```python
print("=== Welcome to my Garden ===")
print(f"Plant {name}")
print(f"Height: {height}cm")
print(f"Age: {age} days")
print("=== End of Program ===")
```

**Por que usar `print()`?**

É a forma padrão de comunicar resultados ao usuário via terminal. Neste exercício ela é a única saída do programa, tornando os dados das variáveis visíveis durante a execução.

---

## Conceito importante: `if __name__ == "__main__"`

Embora não seja uma função, este padrão é central no exercício.

```python
if __name__ == "__main__":
    main()
```

Quando um arquivo Python é **executado diretamente** (`python3 ft_garden_intro.py`), a variável especial `__name__` recebe o valor `"__main__"`. Se o arquivo for **importado** por outro módulo, `__name__` recebe o nome do arquivo, e o bloco dentro do `if` **não é executado**.

Isso permite separar o código que deve rodar apenas quando o arquivo é o ponto de entrada do programa, evitando efeitos colaterais ao importar o módulo em outros projetos.
