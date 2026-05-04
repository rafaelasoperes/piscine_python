# Exercise 2 — Space Crew Management

## Objetivo

Dominar modelos Pydantic aninhados e relacionamentos complexos entre dados, combinando múltiplos modelos dentro de um modelo principal.

---

## Arquivo: `space_crew.py`

### Módulos utilizados

- `pydantic` — biblioteca de validação de dados
- `datetime` — para trabalhar com datas e horários
- `enum` — para criar enumerações tipadas
- `typing` — para anotações de tipos (`List`)

---

## Funções e classes autorizadas explicadas

### `BaseModel`

`BaseModel` é a classe base do Pydantic. Neste exercício, dois modelos herdam dela: `CrewMember` e `SpaceMission`. O diferencial aqui é que `SpaceMission` contém uma **lista de `CrewMember`**, demonstrando o uso de modelos aninhados.

```python
from pydantic import BaseModel

class CrewMember(BaseModel):
    name: str
    rank: Rank

class SpaceMission(BaseModel):
    mission_name: str
    crew: List[CrewMember]  # modelo aninhado
```

Quando o Pydantic valida `SpaceMission`, ele também valida automaticamente cada `CrewMember` dentro da lista `crew`. Se qualquer membro falhar na validação, o erro é propagado com a localização exata (ex: `crew -> 0 -> age`).

---

### `Field`

`Field` adiciona restrições e metadados a cada campo. Neste exercício, um uso importante é a validação do tamanho da lista de tripulantes:

```python
from pydantic import Field

crew: List[CrewMember] = Field(..., min_length=1, max_length=12,
                               description="Tripulantes (1 a 12 membros)")
```

Outros parâmetros utilizados:

| Parâmetro | Significado |
|-----------|-------------|
| `...` | Campo obrigatório |
| `default=valor` | Define valor padrão |
| `min_length=N` | Mínimo de caracteres (string) ou itens (lista) |
| `max_length=N` | Máximo de caracteres (string) ou itens (lista) |
| `ge=N` | Maior ou igual a N |
| `le=N` | Menor ou igual a N |
| `description=texto` | Descrição do campo |

---

### `model_validator`

`@model_validator(mode='after')` permite validar regras de negócio que dependem de múltiplos campos simultaneamente, rodando após todas as validações individuais dos campos.

```python
from pydantic import model_validator

class SpaceMission(BaseModel):
    mission_id: str
    duration_days: int
    crew: List[CrewMember]

    @model_validator(mode="after")
    def validate_mission_rules(self) -> "SpaceMission":
        if not self.mission_id.startswith("M"):
            raise ValueError('Mission ID must start with "M"')
        return self  # OBRIGATÓRIO: sempre retornar self
```

**Regras implementadas com `model_validator` neste exercício:**

1. O `mission_id` deve começar com `"M"`
2. A missão deve ter pelo menos um `Commander` ou `Captain` na tripulação
3. Missões longas (mais de 365 dias) exigem que pelo menos 50% da tripulação tenha 5 ou mais anos de experiência
4. Todos os tripulantes devem estar ativos (`is_active=True`)

---

### `ValidationError`

Exceção lançada quando os dados não passam na validação. Em modelos aninhados, o erro inclui a localização exata do problema dentro da estrutura.

```python
from pydantic import ValidationError

try:
    SpaceMission(crew=[CrewMember(rank="cadet", ...)], ...)
except ValidationError as e:
    for error in e.errors():
        print(error["msg"].replace("Value error, ", ""))
```

---

### `Enum` — `Rank`

Define os valores válidos de patente para um tripulante. Herdar de `str, Enum` permite usar tanto a string diretamente quanto o membro do enum.

```python
from enum import Enum

class Rank(str, Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"
```

O campo `rank` no modelo `CrewMember` só aceita um desses cinco valores:

```python
rank: Rank = Field(..., description="Patente do tripulante")
```

---

### `List` (modelos aninhados)

`List[CrewMember]` define que o campo `crew` é uma lista de objetos do tipo `CrewMember`. O Pydantic valida cada item da lista individualmente.

```python
from typing import List

crew: List[CrewMember] = Field(..., min_length=1, max_length=12)
```

**Como o Pydantic trata modelos aninhados:**

- Cada `CrewMember` na lista é validado como um modelo independente
- Se um `CrewMember` falhar, o erro indica o índice na lista (ex: `crew -> 2 -> age`)
- É possível passar dicionários no lugar de instâncias — o Pydantic os converte automaticamente

```python
# Ambas as formas funcionam:
SpaceMission(crew=[CrewMember(name="Ana", rank="captain", ...)])
SpaceMission(crew=[{"name": "Ana", "rank": "captain", ...}])
```

---

## Modelos criados

### `CrewMember`

| Campo | Tipo | Restrições |
|-------|------|-----------|
| `member_id` | `str` | 3 a 10 caracteres |
| `name` | `str` | 2 a 50 caracteres |
| `rank` | `Rank` | Um dos 5 valores do enum |
| `age` | `int` | Entre 18 e 80 |
| `specialization` | `str` | 3 a 30 caracteres |
| `years_experience` | `int` | Entre 0 e 50 |
| `is_active` | `bool` | Padrão: `True` |

### `SpaceMission`

| Campo | Tipo | Restrições |
|-------|------|-----------|
| `mission_id` | `str` | 5 a 15 caracteres, deve começar com `"M"` |
| `mission_name` | `str` | 3 a 100 caracteres |
| `destination` | `str` | 3 a 50 caracteres |
| `launch_date` | `datetime` | Obrigatório |
| `duration_days` | `int` | Entre 1 e 3650 |
| `crew` | `List[CrewMember]` | 1 a 12 membros, todos ativos |
| `mission_status` | `str` | Padrão: `"planned"` |
| `budget_millions` | `float` | Entre 1.0 e 10000.0 |

---

## Saída esperada

```
Space Mission Crew Validation
=========================================
Valid mission created:
Mission: Mars Colony Establishment
ID: M2024_MARS
Destination: Mars
Duration: 900 days
Budget: $2500.0M
Crew size: 3
Crew members:
  - Sarah Connor (commander) - Mission Command
  - John Smith (lieutenant) - Navigation
  - Alice Johnson (officer) - Engineering
=========================================
Expected validation error:
Mission must have at least one Commander or Captain
```
