# README — `data_pipeline.py` (Exercise 2)

> **Módulo:** `ex2/data_pipeline.py`  
> **Importações autorizadas:** `builtins`, tipos padrão, `import typing`, `import abc`

---

## Visão Geral

Este arquivo representa o **pipeline completo de dados** do Code Nexus, integrando tudo dos
exercícios anteriores e adicionando uma camada de **exportação via sistema de plugins**.
A grande novidade aqui é o uso de `typing.Protocol` para definir contratos por *duck typing*,
ao invés de herança clássica — os plugins de exportação não precisam herdar de nenhuma classe,
apenas precisam ter o método correto.

---

## Importações utilizadas

### `import typing`

- **`typing.Any`**: Usado nas assinaturas dos métodos `validate` e `ingest` da classe abstrata
  `DataProcessor`, permitindo que qualquer tipo de dado seja recebido antes da validação interna.

  ```python
  def validate(self, data: typing.Any) -> bool:
      ...
  ```

- **`typing.Protocol`**: Classe especial do módulo `typing` que define uma **interface estrutural**
  (duck typing estático). Uma classe que implementa todos os métodos de um `Protocol` é considerada
  compatível com ele — **sem precisar herdar explicitamente**.

  ```python
  class ExportPlugin(typing.Protocol):
      def process_output(self, data: list[tuple[int, str]]) -> None:
          pass
  ```

  Isso significa que `CSVExportPlugin` e `JSONExportPlugin` são automaticamente compatíveis com
  `ExportPlugin` apenas por terem o método `process_output` com a assinatura correta, sem herança.

---

### `import abc`

- **`abc.ABC`**: Torna `DataProcessor` uma classe abstrata que não pode ser instanciada diretamente.
- **`abc.abstractmethod`**: Marca `validate` e `ingest` como métodos obrigatórios para qualquer
  subclasse concreta de `DataProcessor`.

---

## Classes implementadas

### `DataProcessor` (classe abstrata)

Interface base de todos os processadores. Define estrutura comum de armazenamento e extração.

| Método | Tipo | Descrição |
|--------|------|-----------|
| `validate(self, data: Any) -> bool` | Abstrato | Verifica compatibilidade do dado |
| `ingest(self, data: Any) -> None` | Abstrato | Ingere e armazena o dado |
| `output(self) -> tuple[int, str]` | Concreto | Extrai o item mais antigo com seu rank |
| `print_stats(self) -> None` | Concreto | Imprime estatísticas do processador |

**Atributos internos:**
- `name: str` — nome do processador (recebido no `__init__`)
- `_storage: list[str]` — fila de strings armazenadas
- `_total_processed: int` — total de itens já ingeridos
- `_next_rank: int` — rank a ser atribuído ao próximo item extraído

---

### `NumericProcessor(DataProcessor)`

Aceita `int`, `float`, e listas mistas. Converte para `str` ao armazenar.

- `validate`: checa se é número individual ou lista contendo apenas números
- `ingest`: converte cada número em string e adiciona a `_storage`; lança `Exception` para dados inválidos

---

### `TextProcessor(DataProcessor)`

Aceita `str` e listas de strings. Armazena diretamente.

- `validate`: checa se é string individual ou lista contendo apenas strings
- `ingest`: adiciona cada string a `_storage`; lança `Exception` para dados inválidos

---

### `LogProcessor(DataProcessor)`

Aceita `dict[str, str]` e listas desse tipo. Converte para string formatada.

- `_is_valid_log_dict`: verifica se todas as chaves e valores do dict são strings
- `_dict_to_string`: converte um dict em string — usa formato `"LEVEL: message"` se tiver as chaves
  `log_level` e `log_message`, senão serializa todos os pares `"chave: valor"`
- `validate`: usa `_is_valid_log_dict` para validar dict único ou lista de dicts
- `ingest`: converte e armazena cada log; lança `Exception` para dados inválidos

---

### `ExportPlugin` (Protocol)

Define o **contrato de duck typing** para todos os plugins de exportação.

```python
class ExportPlugin(typing.Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass
```

Qualquer classe que implemente `process_output` com essa assinatura será
aceita como `ExportPlugin` — sem herança necessária. Isso é o **duck typing estrutural**.

---

### `CSVExportPlugin`

Plugin de exportação em formato CSV. Não herda de nada, apenas implementa `process_output`.

- Recebe uma lista de tuplas `(rank, valor)` e monta uma string com os valores separados por vírgula
- Imprime `"CSV Output:"` seguido da string gerada manualmente (sem importar `csv`)

```python
# Exemplo de saída:
# CSV Output:
# 3.14,-1,2.71
```

---

### `JSONExportPlugin`

Plugin de exportação em formato JSON. Também não herda de nada.

- `_escape_json`: método auxiliar que escapa manualmente `\` e `"` dentro das strings de valor
- `process_output`: monta um objeto JSON com chaves no formato `"item_<rank>"` e valores como strings
- Imprime `"JSON Output:"` seguido do JSON gerado manualmente (sem importar `json`)

```python
# Exemplo de saída:
# JSON Output:
# {"item_3": "42", "item_4": "21", "item_5": "32"}
```

---

### `DataStream`

Orquestra entrada e saída do pipeline completo.

| Método | Descrição |
|--------|-----------|
| `register_processor(proc)` | Registra um processador no pipeline |
| `process_stream(stream)` | Roteia cada elemento do stream ao processador correto |
| `print_processors_stats()` | Exibe estatísticas de todos os processadores |
| `output_pipeline(nb, plugin)` | Extrai `nb` itens de cada processador e exporta via plugin |

**Funcionamento de `output_pipeline`:**

```python
def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
    for processor in self._processors:
        extracted = []
        for _ in range(nb):
            try:
                extracted.append(processor.output())
            except Exception:
                break
        plugin.process_output(extracted)
```

Para cada processador registrado, tenta extrair até `nb` itens. Se o processador não tiver
itens suficientes, para antes. Os itens coletados são então passados ao plugin escolhido.
O `plugin` pode ser qualquer objeto compatível com `ExportPlugin` — **sem verificação de herança**.

---

## Funções built-in utilizadas

| Função | Uso |
|--------|-----|
| `isinstance(obj, type)` | Validação de tipo em `validate` de cada processador |
| `all(iterable)` | Verifica que todos os elementos de uma lista satisfazem a condição de tipo |
| `str(value)` | Converte números em strings para armazenamento no `NumericProcessor` |
| `print(...)` | Exibe saídas dos plugins, erros de stream e estatísticas |
| `len(collection)` | Verifica tamanho das listas internas |

---

## Duck Typing vs Herança — diferença chave

| Aspecto | Herança (`ABC`) | Duck Typing (`Protocol`) |
|--------|-----------------|--------------------------|
| Usado em | `DataProcessor` e subclasses | `ExportPlugin` e plugins |
| Verificação | Em tempo de definição da classe | Estrutural — em tempo de uso |
| Precisa herdar? | Sim | Não |
| Flexibilidade | Menor (acoplamento explícito) | Maior (qualquer classe compatível) |

---

## Exemplo de saída esperada

```
=== Code Nexus - Data Pipeline ===

Initialize Data Stream...
== DataStream statistics ==
No processor found, no data

Registering Processors

Send first batch of data on stream: [...]
== DataStream statistics ==
Numeric Processor: total 4 items processed, remaining 4 on processor
Text Processor: total 3 items processed, remaining 3 on processor
Log Processor: total 2 items processed, remaining 2 on processor

Send 3 processed data from each processor to a CSV plugin:
CSV Output:
3.14,-1,2.71
CSV Output:
Hello world,Hi,five
CSV Output:
WARNING: Telnet access! Use ssh instead,INFO: User wil is connected

Send 5 processed data from each processor to a JSON plugin:
JSON Output:
{"item_3": "42", "item_4": "21", "item_5": "32", "item_6": "42", "item_7": "64"}
JSON Output:
{"item_3": "I love AI", "item_4": "LLMs are wonderful", "item_5": "Stay healthy", "item_6": "World hello"}
JSON Output:
{"item_2": "ERROR: 500 server crash", "item_3": "NOTICE: Certificate expires in 10 days"}
```
