# Exercise 2 — Memory Depths

## Arquivo: `scope_mysteries.py`

Este exercício aborda **escopo léxico**, **closures** e o uso de `nonlocal` para manter estado dentro de funções aninhadas sem recorrer a variáveis globais.

---

## Funções autorizadas e explicações

### `nonlocal`

A palavra-chave `nonlocal` permite que uma função interna **leia e modifique** uma variável definida em um escopo externo (mas não global).

```python
def contador():
    count = 0

    def incrementar():
        nonlocal count   # indica que 'count' vem do escopo externo
        count += 1
        return count

    return incrementar

c = contador()
c()  # 1
c()  # 2
```

**Por que `nonlocal` é permitido mas `global` é proibido?**

| `global` | `nonlocal` |
|---|---|
| Acessa variáveis do módulo inteiro | Acessa variáveis do escopo imediatamente externo |
| Quebra a pureza funcional — qualquer parte do código pode alterar o estado | Mantém o estado **encapsulado** dentro da closure — invisível ao resto do programa |
| Dificulta testes e rastreamento de bugs | Favorece isolamento e previsibilidade |

`nonlocal` é a forma funcional de manter estado: o estado existe, mas está **preso dentro da função**, não exposto globalmente.

---

### Closures (Fechamentos)

Uma closure é uma função que **"lembra"** as variáveis do ambiente onde foi criada, mesmo depois que esse ambiente deixou de existir na pilha de execução.

```python
def fabricar_saudacao(saudacao: str):
    def saudar(nome: str) -> str:
        return f"{saudacao}, {nome}!"   # 'saudacao' é capturada do escopo externo
    return saudar

ola = fabricar_saudacao("Olá")
ola("Arthur")   # "Olá, Arthur!"
```

Aqui, `saudar` é uma closure: ela carrega consigo a variável `saudacao` mesmo após `fabricar_saudacao` ter retornado.

**Benefícios do escopo léxico:**
- Permite criar funções especializadas a partir de funções genéricas (factories).
- Encapsula estado sem precisar de classes.
- Torna o código mais modular e testável.

---

## Resumo das funções implementadas

| Função | Descrição |
|---|---|
| `mage_counter()` | Retorna uma closure que conta quantas vezes foi chamada; cada instância tem estado independente |
| `spell_accumulator(initial_power)` | Retorna uma closure que acumula valores sobre uma base inicial, usando `nonlocal` |
| `enchantment_factory(enchantment_type)` | Retorna uma função que aplica um tipo de encantamento a qualquer item; o tipo fica capturado na closure |
| `memory_vault()` | Retorna um dicionário com funções `store` e `recall` que compartilham um dicionário privado via closure |

---

## Conceitos-chave

**Como closures "lembram" o ambiente de criação?**
Quando Python cria uma função interna, ele guarda uma referência às variáveis do escopo externo na célula de closure (`__closure__`) da função. Essas referências persistem enquanto a função interna existir, independentemente de o escopo externo ter retornado.

**Diferença entre `global` e `nonlocal`:**
`global` expõe o estado ao módulo inteiro, enquanto `nonlocal` mantém o estado privado dentro da hierarquia de funções — o princípio de menor privilégio aplicado a variáveis.
