# README do módulo py_module_06

Este README explica, as funções autorizadas usadas em cada arquivo do diretório `py_module_06`.

## O que é um módulo e como funciona a importação

Em Python, um módulo é um arquivo `.py` que contém funções, classes e variáveis. Quando você usa `import`, o Python carrega esse arquivo e torna seus nomes disponíveis.

- `import módulo`: importa todo o módulo e você acessa seus símbolos usando `módulo.nome`.
- `from módulo import nome`: importa uma função, classe ou variável específica diretamente, permitindo o uso sem o prefixo do módulo.
- `import módulo as apelido`: importa o módulo inteiro com um nome curto ou personalizado.

Exemplos:
- `import elements` → usa `elements.create_fire()`.
- `from elements import create_water` → usa `create_water()` diretamente.
- `import alchemy.grimoire as g` → usa `g.light_spell_record()`.

## O papel de `__init__.py`

O arquivo `__init__.py` torna uma pasta em um pacote Python. Ele pode expor funções e nomes para que o pacote seja usado diretamente com `import alchemy`.

No pacote `alchemy`, o arquivo `__init__.py` define:
- `create_air`
- `strength_potion`
- `heal` (alias de `healing_potion`)
- `lead_to_gold`

Isso permite que `alchemy.create_air()` e `alchemy.lead_to_gold()` funcionem sem importar submódulos específicos.

## Estrutura geral

- `elements.py`: define as funções básicas para criar elementos do `alembic`.
- `alchemy/`: pacote com funções de elementos, poções, transmutação e grimoire.
- `ft_*`: arquivos de demonstração que usam importações e chamadas de função específicas.

## Arquivos de demonstração `ft_alembic_*`

### `ft_alembic_0.py`
- Função autorizada usada: `create_fire`
- Importação: `import elements`
- Uso: `elements.create_fire()`
- Explicação: chama a função definida em `elements.py` para retornar a string `"Fire element created"`.

### `ft_alembic_1.py`
- Função autorizada usada: `create_water`
- Importação: `from elements import create_water`
- Uso: `create_water()`
- Explicação: chama diretamente a função `create_water()` de `elements.py`, retornando `"Water element created"`.

### `ft_alembic_2.py`
- Função autorizada usada: `create_earth`
- Importação: `import alchemy.elements`
- Uso: `alchemy.elements.create_earth()`
- Explicação: acessa o módulo `alchemy.elements` e chama `create_earth()` para obter `"Earth element created"`.

### `ft_alembic_3.py`
- Função autorizada usada: `create_air`
- Importação: `from alchemy.elements import create_air`
- Uso: `create_air()`
- Explicação: importa diretamente `create_air()` do módulo `alchemy.elements` e retorna `"Air element created"`.

### `ft_alembic_4.py`
- Função autorizada usada: `create_air`
- Importação: `import alchemy`
- Uso principal: `alchemy.create_air()`
- Explicação: `alchemy.__init__.py` exporta `create_air`, permitindo chamá-la diretamente como `alchemy.create_air()`.
- Observação: o script também demonstra um acesso inválido ou não autorizado via `alchemy.elements.create_earth()`, que não faz parte da interface pública do pacote quando importado apenas como `import alchemy`.

### `ft_alembic_5.py`
- Função autorizada usada: `create_air`
- Importação: `from alchemy import create_air`
- Uso: `create_air()`
- Explicação: importa o símbolo `create_air` diretamente do pacote `alchemy` graças ao `__all__` e às importações em `alchemy/__init__.py`.

## Arquivos de demonstração `ft_distillation_*`

### `ft_distillation_0.py`
- Funções autorizadas usadas: `healing_potion`, `strength_potion`
- Importação: `from alchemy.potions import healing_potion, strength_potion`
- Uso: `strength_potion()` e `healing_potion()`
- Explicação: chama as funções definidas em `alchemy/potions.py`, onde `strength_potion()` combina `create_fire()` e `create_water()`, e `healing_potion()` combina `create_earth()` e `create_air()`.

### `ft_distillation_1.py`
- Funções autorizadas usadas: `strength_potion`, `heal`
- Importação: `import alchemy`
- Uso: `alchemy.strength_potion()` e `alchemy.heal()`
- Explicação: `alchemy/__init__.py` exporta `strength_potion` e faz alias de `healing_potion` como `heal`, permitindo o uso direto dessas chamadas a partir do pacote.

## Arquivos de demonstração `ft_kaboom_*`

### `ft_kaboom_0.py`
- Função autorizada usada: `light_spell_record`
- Importação: `import alchemy.grimoire as g`
- Uso: `g.light_spell_record("Fantasy", "earth, air, fire")`
- Explicação: acessa o subpacote `alchemy.grimoire` e chama a função que registra feitiços leves, usando validador interno para validar ingredientes.

### `ft_kaboom_1.py`
- Função autorizada usada: `dark_spell_record`
- Importação: `import alchemy.grimoire.dark_spellbook as d`
- Uso: `d.dark_spell_record("Delirium", "bats, eyeball, arsenic")`
- Explicação: importa diretamente o módulo `dark_spellbook` e chama a função de registro de feitiços sombrios.
- Observação: o script indica que esta importação pode gerar exceção se a estrutura de importação não estiver correta.

## Arquivos de demonstração `ft_transmutation_*`

### `ft_transmutation_0.py`
- Função autorizada usada: `lead_to_gold`
- Importação: `import alchemy.transmutation.recipes`
- Uso: `alchemy.transmutation.recipes.lead_to_gold()`
- Explicação: chama a função definida em `alchemy/transmutation/recipes.py`, que combina `create_air()`, `strength_potion()` e `create_fire()`.

### `ft_transmutation_1.py`
- Função autorizada usada: `lead_to_gold`
- Importação: `import alchemy.transmutation`
- Uso: `alchemy.transmutation.lead_to_gold()`
- Explicação: acessa o módulo `alchemy.transmutation` e chama a função de transmutação.

### `ft_transmutation_2.py`
- Função autorizada usada: `lead_to_gold`
- Importação: `import alchemy`
- Uso: `alchemy.lead_to_gold()`
- Explicação: usa a função exportada pelo pacote `alchemy` via `alchemy/__init__.py`.

## Módulos e funções do pacote `alchemy`

### `alchemy/elements.py`
- `create_earth()`: retorna `"Earth element created"`
- `create_air()`: retorna `"Air element created"`

### `alchemy/potions.py`
- `healing_potion()`: combina `create_earth()` e `create_air()` e retorna uma string com os dois resultados.
- `strength_potion()`: combina `create_fire()` e `create_water()` e retorna uma string com os dois resultados.

### `alchemy/grimoire/light_spellbook.py`
- `light_spell_allowed_ingredients()`: lista de ingredientes permitidos para feitiços leves.
- `light_spell_record(spell_name, ingredients)`: valida ingredientes e retorna mensagem de aceitação ou rejeição.

### `alchemy/grimoire/dark_spellbook.py`
- `dark_spell_allowed_ingredients()`: lista de ingredientes permitidos para feitiços sombrios.
- `dark_spell_record(spell_name, ingredients)`: valida ingredientes e retorna mensagem de aceitação ou rejeição.

### `alchemy/grimoire/light_validator.py`
- `validate_ingredients(ingredients)`: compara ingredientes com a lista permitida e retorna string como `"Earth, Air and Fire - VALID"` ou `"... - INVALID"`.

### `alchemy/grimoire/dark_validator.py`
- `validate_ingredients(ingredients)`: compara ingredientes sombrios permitidos e retorna string similar ao validador leve.

### `alchemy/transmutation/recipes.py`
- `lead_to_gold()`: usa `create_air()`, `strength_potion()` e `create_fire()` para simular transmutação.

## Notas finais

- Os arquivos `ft_*` demonstram diferentes formas de importação: `import module`, `from module import name`, `import package`, `import package.module`.
- As funções autorizadas são aquelas efetivamente chamadas pelos scripts e/ou exportadas pelo pacote.
- O arquivo `ft_alembic_4.py` mostra um caso em que uma função não está disponível apenas pelo `import alchemy` padrão.
