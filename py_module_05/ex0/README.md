# README — `data_processor.py` (Exercise 0)

> **Módulo:** `ex0/data_processor.py`  
> **Importações autorizadas:** `builtins`, tipos padrão, `import typing`, `import abc`

---

## Visão Geral

Este arquivo implementa a **fundação da arquitetura de processamento de dados** do Code Nexus.
Ele define uma classe abstrata base e três classes especializadas que herdam dela, demonstrando
o uso de classes abstratas, polimorfismo e sobrescrita de métodos.

---

## Importações utilizadas

### `from abc import ABC, abstractmethod`

O módulo `abc` (Abstract Base Classes) fornece a infraestrutura para criar classes abstratas em Python.

- **`ABC`**: Classe auxiliar que torna mais simples herdar de `ABCMeta`. Uma classe que herda de `ABC`
  torna-se uma classe abstrata — ela **não pode ser instanciada diretamente**. Serve como contrato
  que obriga as subclasses a implementarem certos métodos.

  ```python
  class DataProcessor(ABC):  # DataProcessor agora é abstrata
      ...
  ```

- **`abstractmethod`**: Decorador usado para marcar um método como **abstrato**. Qualquer subclasse
  concreta que herdar de `DataProcessor` será **obrigada** a sobrescrever esses métodos, caso contrário
  o Python levantará um `TypeError` na tentativa de instanciação.

  ```python
  @abstractmethod
  def validate(self, data: Any) -> bool:
      pass

  @abstractmethod
  def ingest(self, data: Any) -> None:
      pass
  ```

---

### `from typing import Any, Union`

O módulo `typing` fornece suporte a **anotações de tipo** mais expressivas.

- **`Any`**: Tipo especial que indica que uma variável pode ser **de qualquer tipo**. É usado na
  assinatura dos métodos abstratos `validate` e `ingest` da classe base, pois o `DataProcessor`
  não conhece antecipadamente qual tipo de dado será recebido.

  ```python
  def validate(self, data: Any) -> bool:
      ...
  ```

- **`Union`**: Permite indicar que uma variável pode ser **um de vários tipos**. Usado nas assinaturas
  dos métodos `ingest` das subclasses para expressar com precisão os tipos aceitos por cada processador.

  ```python
  def ingest(self, data: Union[int, float, list[Union[int, float]]]) -> None:
      ...
  ```

---

## Classes implementadas

### `DataProcessor` (classe abstrata)

Classe base que define a **interface comum** a todos os processadores. Não pode ser instanciada diretamente.

| Método | Tipo | Descrição |
|--------|------|-----------|
| `validate(self, data: Any) -> bool` | Abstrato | Verifica se o dado pode ser processado por esta classe |
| `ingest(self, data: Any) -> None` | Abstrato | Ingere (armazena) o dado internamente |
| `output(self) -> tuple[int, str]` | Concreto | Extrai o dado mais antigo com seu índice de rank |

**Atributos internos:**
- `_data_store: list[tuple[int, str]]` — fila interna de dados processados
- `_counter: int` — contador que representa o rank de cada item ingerido

---

### `NumericProcessor(DataProcessor)`

Processa dados numéricos (`int`, `float`, ou listas mistas de ambos).
Converte os valores para `str` antes de armazenar.

- `validate`: retorna `True` se o dado for `int`, `float`, ou uma lista não-vazia contendo apenas esses tipos
- `ingest`: armazena cada número como string com seu rank; lança `ValueError` para dados inválidos

---

### `TextProcessor(DataProcessor)`

Processa dados textuais (`str` ou listas de `str`).
Armazena as strings diretamente.

- `validate`: retorna `True` se o dado for `str` ou uma lista não-vazia de strings
- `ingest`: armazena cada string com seu rank; lança `ValueError` para dados inválidos

---

### `LogProcessor(DataProcessor)`

Processa entradas de log (`dict[str, str]` ou listas desse tipo).
Converte os dicionários em strings formatadas.

- `validate`: retorna `True` se o dado for um `dict` com chaves e valores todos do tipo `str`,
  ou uma lista não-vazia desse tipo
- `ingest`: converte cada dict em string (ex: `"NOTICE: Connection to server"`) e armazena com rank;
  lança `ValueError` para dados inválidos

---

## Funções built-in utilizadas

| Função | Uso |
|--------|-----|
| `isinstance(obj, type)` | Verifica o tipo de um dado antes de processá-lo |
| `all(iterable)` | Valida que todos os elementos de uma lista satisfazem uma condição |
| `str(value)` | Converte valores numéricos em string para armazenamento |
| `print(...)` | Exibe resultados no terminal durante os testes |
| `range(n)` | Itera um número fixo de vezes nos testes de extração |

---

## Método `output` — funcionamento

```python
def output(self) -> tuple[int, str]:
    if not self._data_store:
        raise IndexError("No data to output")
    return self._data_store.pop(0)
```

- Retorna uma **tupla `(rank, valor_string)`** com o dado mais antigo (FIFO)
- Remove o item da fila interna após a extração
- Lança `IndexError` se não houver dados disponíveis
- O `rank` é um inteiro único por processador, incrementado a cada `ingest`

---

## Exemplo de saída esperada

```
=== Code Nexus - Data Processor ===

Testing Numeric Processor...
Trying to validate input '42': True
Trying to validate input 'Hello': False
Test invalid ingestion of string 'foo' without prior validation:
Got exception: Improper numeric data
Processing data: [1, 2, 3, 4, 5]
Extracting 3 values...
Numeric value 0: 1
Numeric value 1: 2
Numeric value 2: 3

Testing Text Processor...
Trying to validate input '42': False
Processing data: ['Hello', 'Nexus', 'World']
Text value 0: Hello

Testing Log Processor...
Trying to validate input 'Hello': False
Processing data: [{'level': 'NOTICE', 'msg': 'Connection to server'}, ...]
Log entry 0: NOTICE: Connection to server
Log entry 1: ERROR: Unauthorized access!!
```
