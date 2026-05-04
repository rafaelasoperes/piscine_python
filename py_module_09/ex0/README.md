# Exercise 0 — Space Station Data

## Objetivo

Aprender a criar modelos Pydantic básicos utilizando `BaseModel` e validação com `Field`.

---

## Arquivo: `space_station.py`

### Módulos utilizados

- `pydantic` — biblioteca de validação de dados
- `datetime` — para trabalhar com datas e horários
- `typing` — para anotações de tipos (`Optional`)

---

## Funções e classes autorizadas explicadas

### `BaseModel`

`BaseModel` é a classe base do Pydantic. Todo modelo de dados é criado herdando dela.
Ao herdar de `BaseModel`, a classe ganha validação automática dos campos declarados, conversão de tipos compatíveis e geração de mensagens de erro detalhadas.

```python
from pydantic import BaseModel

class SpaceStation(BaseModel):
    name: str
    crew_size: int
```

Quando você instancia um modelo, o Pydantic valida cada campo automaticamente:

```python
station = SpaceStation(name="ISS", crew_size=6)  # OK
station = SpaceStation(name="ISS", crew_size="seis")  # Erro de validação
```

---

### `Field`

`Field` permite adicionar restrições, descrições e valores padrão aos campos do modelo.
É importado de `pydantic` e utilizado como valor padrão de um atributo.

```python
from pydantic import Field

crew_size: int = Field(..., ge=1, le=20, description="Número de tripulantes (1-20)")
```

Os principais parâmetros do `Field` utilizados neste exercício:

| Parâmetro | Significado |
|-----------|-------------|
| `...` | Campo obrigatório (sem valor padrão) |
| `default=valor` | Define um valor padrão para o campo |
| `min_length=N` | Comprimento mínimo de uma string |
| `max_length=N` | Comprimento máximo de uma string |
| `ge=N` | Maior ou igual a N (*greater than or equal*) |
| `le=N` | Menor ou igual a N (*less than or equal*) |
| `description=texto` | Descrição do campo (documentação) |

---

### `ValidationError`

`ValidationError` é a exceção lançada pelo Pydantic quando os dados fornecidos não passam na validação. Ela é importada de `pydantic` e deve ser capturada com `try/except`.

```python
from pydantic import ValidationError

try:
    SpaceStation(crew_size=50, ...)  # crew_size máximo é 20
except ValidationError as e:
    for error in e.errors():
        print(error["msg"])  # Exibe a mensagem de erro de cada campo inválido
```

O método `.errors()` retorna uma lista de dicionários, onde cada item contém:
- `"loc"` — localização do campo com erro
- `"msg"` — mensagem descritiva do erro
- `"type"` — tipo do erro

---

### `Optional`

`Optional[str]` indica que um campo pode ser do tipo especificado **ou** `None`. Vem do módulo `typing` e é útil para campos que nem sempre terão valor.

```python
from typing import Optional

notes: Optional[str] = Field(default=None, max_length=200)
```

---

### Conversão automática de tipos

O Pydantic converte automaticamente tipos compatíveis. Por exemplo, uma string no formato ISO 8601 é convertida para `datetime`:

```python
last_maintenance: datetime = Field(...)

# Funciona com string:
SpaceStation(last_maintenance="2024-01-15T08:30:00", ...)

# Funciona com objeto datetime:
from datetime import datetime
SpaceStation(last_maintenance=datetime(2024, 1, 15, 8, 30, 0), ...)
```

---

## Modelo criado: `SpaceStation`

| Campo | Tipo | Restrições |
|-------|------|-----------|
| `station_id` | `str` | 3 a 10 caracteres |
| `name` | `str` | 1 a 50 caracteres |
| `crew_size` | `int` | Entre 1 e 20 |
| `power_level` | `float` | Entre 0.0 e 100.0 |
| `oxygen_level` | `float` | Entre 0.0 e 100.0 |
| `last_maintenance` | `datetime` | Obrigatório |
| `is_operational` | `bool` | Padrão: `True` |
| `notes` | `Optional[str]` | Máximo 200 caracteres |

---

## Saída esperada

```
Space Station Data Validation
========================================
Valid station created:
ID: ISS001
Name: International Space Station
Crew: 6 people
Power: 85.5%
Oxygen: 92.3%
Status: Operational
========================================
Expected validation error:
Input should be less than or equal to 20
```
