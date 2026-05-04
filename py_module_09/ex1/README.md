# Exercise 1 — Alien Contact Logs

## Objetivo

Dominar a validação personalizada utilizando `@model_validator` para implementar regras de negócio complexas que dependem de múltiplos campos ao mesmo tempo.

---

## Arquivo: `alien_contact.py`

### Módulos utilizados

- `pydantic` — biblioteca de validação de dados
- `datetime` — para trabalhar com datas e horários
- `enum` — para criar enumerações tipadas
- `typing` — para anotações de tipos (`Optional`)

---

## Funções e classes autorizadas explicadas

### `BaseModel`

`BaseModel` é a classe base do Pydantic. Todo modelo herda dela para obter validação automática de campos, conversão de tipos e geração de erros detalhados.

```python
from pydantic import BaseModel

class AlienContact(BaseModel):
    contact_id: str
    signal_strength: float
```

---

### `Field`

`Field` adiciona restrições e metadados aos campos do modelo. Os principais parâmetros usados neste exercício:

| Parâmetro | Significado |
|-----------|-------------|
| `...` | Campo obrigatório |
| `default=valor` | Define valor padrão |
| `min_length=N` | Comprimento mínimo da string |
| `max_length=N` | Comprimento máximo da string |
| `ge=N` | Maior ou igual a N |
| `le=N` | Menor ou igual a N |
| `description=texto` | Descrição do campo |

```python
signal_strength: float = Field(..., ge=0.0, le=10.0, description="Intensidade do sinal (0-10)")
```

---

### `model_validator`

`@model_validator(mode='after')` é um decorador que permite criar validações personalizadas que rodam **após** o Pydantic validar cada campo individualmente. É ideal para regras que dependem de **múltiplos campos ao mesmo tempo**.

```python
from pydantic import model_validator

class AlienContact(BaseModel):
    contact_type: ContactType
    is_verified: bool

    @model_validator(mode="after")
    def validate_contact_rules(self) -> "AlienContact":
        if self.contact_type == ContactType.physical and not self.is_verified:
            raise ValueError("Contatos físicos precisam ser verificados")
        return self  # IMPORTANTE: sempre retornar self
```

**Regras implementadas com `model_validator` neste exercício:**

1. O `contact_id` deve começar com `"AC"` (Alien Contact)
2. Contatos do tipo `physical` precisam ser verificados (`is_verified=True`)
3. Contatos do tipo `telepathic` exigem pelo menos 3 testemunhas
4. Sinais fortes (`signal_strength > 7.0`) devem incluir a mensagem recebida

> **Importante:** O `@model_validator(mode='after')` substitui o `@validator` do Pydantic v1,
> que está depreciado. Use sempre a versão v2.

---

### `ValidationError`

Exceção lançada quando os dados não passam na validação. Capturada com `try/except` para exibir mensagens de erro amigáveis.

```python
from pydantic import ValidationError

try:
    AlienContact(contact_type="telepathic", witness_count=1, ...)
except ValidationError as e:
    for error in e.errors():
        print(error["msg"].replace("Value error, ", ""))
```

---

### `Enum` (ContactType)

`Enum` cria um conjunto fixo de valores válidos para um campo. Usar `str, Enum` como bases permite que o campo aceite tanto o valor string diretamente quanto o membro do enum.

```python
from enum import Enum

class ContactType(str, Enum):
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"
```

Com isso, o campo `contact_type` só aceita um desses quatro valores. Qualquer outro valor causa um `ValidationError` automaticamente.

```python
# OK
AlienContact(contact_type="radio", ...)
AlienContact(contact_type=ContactType.radio, ...)

# Erro
AlienContact(contact_type="laser", ...)
```

---

### `Optional`

`Optional[str]` indica que um campo pode ser `None`. Útil para campos opcionais como a mensagem recebida.

```python
from typing import Optional

message_received: Optional[str] = Field(default=None, max_length=500)
```

---

## Modelo criado: `AlienContact`

| Campo | Tipo | Restrições |
|-------|------|-----------|
| `contact_id` | `str` | 5 a 15 caracteres, deve começar com `"AC"` |
| `timestamp` | `datetime` | Obrigatório |
| `location` | `str` | 3 a 100 caracteres |
| `contact_type` | `ContactType` | Um dos 4 tipos do enum |
| `signal_strength` | `float` | Entre 0.0 e 10.0 |
| `duration_minutes` | `int` | Entre 1 e 1440 |
| `witness_count` | `int` | Entre 1 e 100 |
| `message_received` | `Optional[str]` | Máximo 500 caracteres |
| `is_verified` | `bool` | Padrão: `False` |

---

## Saída esperada

```
Alien Contact Log Validation
======================================
Valid contact report:
ID: AC_2024_001
Type: radio
Location: Area 51, Nevada
Signal: 8.5/10
Duration: 45 minutes
Witnesses: 5
Message: 'Greetings from Zeta Reticuli'
======================================
Expected validation error:
Telepathic contact requires at least 3 witnesses
```
