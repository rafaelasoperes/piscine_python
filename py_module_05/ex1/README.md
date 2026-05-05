# README — `data_stream.py` (Exercise 1)

> **Módulo:** `ex1/data_stream.py`  
> **Importações autorizadas:** `builtins`, tipos padrão, `import typing`, `import abc`

---

## Visão Geral

Este arquivo expande o Exercise 0 adicionando a classe `DataStream`, responsável por
**receber um fluxo de dados mistos** e **rotear automaticamente** cada elemento para o
processador adequado. O mecanismo central é o polimorfismo de subtipo: o `DataStream`
não conhece os tipos concretos dos processadores — ele simplesmente chama `can_process`
em cada um e delega o trabalho.

---

## Importações utilizadas

### `import typing`

O módulo `typing` é usado aqui através de seu acesso com namespace (`typing.Any`, `typing.Any`),
fornecendo suporte às **anotações de tipo** das assinaturas dos métodos.

- **`typing.Any`**: Indica que um parâmetro ou variável pode ser de qualquer tipo. Essencial
  nos métodos `can_process` e `process` das subclasses, que precisam aceitar qualquer dado
  vindo do stream antes de validá-lo internamente.

  ```python
  def can_process(self, data: typing.Any) -> bool:
      ...
  def process(self, data: typing.Any) -> None:
      ...
  ```

---

### `import abc`

O módulo `abc` fornece `ABC` e `abstractmethod` para definir a interface abstrata da classe base.

- **`abc.ABC`**: Faz de `DataProcessor` uma classe abstrata, impedindo sua instanciação direta
  e garantindo que toda subclasse concreta implemente os métodos obrigatórios.

- **`abc.abstractmethod`**: Marca os métodos `can_process`, `process` e `get_name` como
  abstratos, forçando cada processador especializado a fornecer sua própria implementação.

  ```python
  @abc.abstractmethod
  def can_process(self, data: typing.Any) -> bool:
      pass

  @abc.abstractmethod
  def process(self, data: typing.Any) -> None:
      pass

  @abc.abstractmethod
  def get_name(self) -> str:
      pass
  ```

---

## Classes implementadas

### `DataProcessor` (classe abstrata)

Classe base herdada de `abc.ABC`. Define a interface que todo processador deve respeitar.

| Método | Tipo | Descrição |
|--------|------|-----------|
| `can_process(self, data: Any) -> bool` | Abstrato | Informa se este processador aceita o dado |
| `process(self, data: Any) -> None` | Abstrato | Processa e armazena o dado internamente |
| `get_output(self) -> Any` | Concreto | Extrai o item mais antigo da fila interna |
| `get_processed_count(self) -> int` | Concreto | Retorna o total de itens processados |
| `get_remaining_count(self) -> int` | Concreto | Retorna quantos itens ainda estão na fila |
| `get_name(self) -> str` | Abstrato | Retorna o nome legível do processador |

**Atributos internos:**
- `_processed_count: int` — contador do total de itens processados desde a criação
- `_outputs: list[Any]` — fila interna dos dados processados aguardando extração

---

### `NumericProcessor(DataProcessor)`

Aceita e processa `int`, `float` e listas mistas de ambos.

- `can_process`: retorna `True` para `int`/`float` individuais ou listas contendo apenas esses tipos
- `process`: itera sobre a lista (ou adiciona o item único) e coloca cada valor em `_outputs`
- `get_name`: retorna `"Numeric Processor"`

---

### `TextProcessor(DataProcessor)`

Aceita e processa `str` e listas de strings.

- `can_process`: retorna `True` para `str` individual ou lista contendo apenas strings
- `process`: armazena cada string em `_outputs`
- `get_name`: retorna `"Text Processor"`

---

### `LogProcessor(DataProcessor)`

Aceita e processa dicionários com chaves `"log_level"` e `"log_message"`, além de listas deles.

- `_is_valid_log`: método auxiliar que verifica se um `dict` possui as chaves obrigatórias
- `can_process`: usa `_is_valid_log` para validar item único ou cada elemento de uma lista
- `process`: armazena cada dict em `_outputs`
- `get_name`: retorna `"Log Processor"`

---

### `DataStream`

Classe principal que orquestra o fluxo de dados usando **polimorfismo**.

| Método | Descrição |
|--------|-----------|
| `register_processor(proc)` | Adiciona um processador à lista interna |
| `process_stream(stream)` | Itera sobre o stream e roteia cada elemento ao processador adequado |
| `print_processor_stats()` | Imprime estatísticas de todos os processadores registrados |

**Como o roteamento funciona (polimorfismo em ação):**

```python
# DataStream não sabe o tipo concreto do processador —
# chama can_process polimorficamente em cada um:
for processor in self._processors:
    if processor.can_process(element):
        processor.process(element)
        break
```

O `DataStream` trata todos os processadores como `DataProcessor` (tipo base).
Cada chamada a `can_process` e `process` é resolvida em tempo de execução
pela implementação concreta da subclasse — isso é **polimorfismo de subtipo**.

---

## Funções built-in utilizadas

| Função | Uso |
|--------|-----|
| `isinstance(obj, type)` | Verifica o tipo do dado nos métodos `can_process` de cada processador |
| `len(collection)` | Verifica tamanho de listas em validações e em `get_remaining_count` |
| `print(...)` | Exibe erros de stream e estatísticas dos processadores |
| `isinstance(data, list)` | Distingue entre dado único e lista para iterar corretamente |

---

## Benefícios do design polimorfo

A pergunta do subject — *"Como o polimorfismo permite ao DataStream lidar com tipos diferentes
sem conhecer suas implementações específicas?"* — é respondida pela arquitetura:

1. **Extensibilidade**: adicionar um novo tipo de processador (ex: `ImageProcessor`) não requer
   nenhuma modificação no `DataStream` — basta registrá-lo.
2. **Desacoplamento**: o `DataStream` depende apenas da interface `DataProcessor`, não das classes concretas.
3. **Responsabilidade única**: cada processador sabe exatamente o que aceita e como processar,
   sem lógica condicional centralizada.

---

## Exemplo de saída esperada

```
=== Code Nexus - Data Stream ===

Initialize Data Stream...
== DataStream statistics ==
No processor found, no data

Registering Numeric Processor

Send first batch of data on stream: [...]
DataStream error - Can't process element in stream: Hello world
DataStream error - Can't process element in stream: [{'log_level': ...}]
DataStream error - Can't process element in stream: ['Hi', 'five']
== DataStream statistics ==
Numeric Processor: total 4 items processed, remaining 4 on processor

Registering other data processors

Send the same batch again
== DataStream statistics ==
Numeric Processor: total 8 items processed, remaining 8 on processor
Text Processor: total 3 items processed, remaining 3 on processor
Log Processor: total 2 items processed, remaining 2 on processor

Consume some elements from the data processors: Numeric 3, Text 2, Log 1
== DataStream statistics ==
Numeric Processor: total 8 items processed, remaining 5 on processor
Text Processor: total 3 items processed, remaining 1 on processor
Log Processor: total 2 items processed, remaining 1 on processor
```
