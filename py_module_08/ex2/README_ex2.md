# Exercise 2 — Accessing the Mainframe

**Arquivo:** `oracle.py`
**Módulos autorizados:** `os`, `sys`, `python-dotenv`, operações de arquivo

---

## O que o programa faz

Carrega variáveis de configuração a partir de um arquivo `.env` e do ambiente do sistema, verifica se todas as configurações necessárias estão presentes e exibe o status de cada uma. Demonstra como gerenciar configurações sensíveis (senhas, chaves de API) sem hardcoding no código-fonte.

---

## Funções e módulos utilizados

### `load_dotenv()` — da biblioteca `python-dotenv`

```python
from dotenv import load_dotenv
load_dotenv()
```

Lê o arquivo `.env` no diretório atual e carrega cada linha `CHAVE=VALOR` como uma variável de ambiente do processo. Após essa chamada, `os.getenv()` consegue acessar os valores definidos no `.env`. Variáveis já definidas no ambiente do sistema **não são sobrescritas** — o sistema tem prioridade sobre o `.env`.

---

### `os.getenv()`

```python
value = os.getenv(name)
```

Lê o valor de uma variável de ambiente pelo nome. Retorna `None` se a variável não existir (não lança exceção). Usado para acessar de forma segura cada configuração: `MATRIX_MODE`, `DATABASE_URL`, `API_KEY`, `LOG_LEVEL` e `ZION_ENDPOINT`.

---

### `os.path.exists()`

```python
env_exists = os.path.exists(".env")
```

Verifica se um arquivo ou diretório existe no sistema de arquivos. Retorna `True` ou `False`. Usado para checar se o arquivo `.env` está presente e exibir o aviso correto na seção de verificação de segurança.

---

### `sys.exit()`

```python
sys.exit(1)
```

Encerra o programa com código de erro `1`. Chamado quando alguma variável de configuração obrigatória está faltando, impedindo que o sistema rode em estado incompleto ou inseguro.

---

## Variáveis de configuração

| Variável | Descrição |
|---|---|
| `MATRIX_MODE` | Modo de execução: `development` ou `production` |
| `DATABASE_URL` | String de conexão com o banco de dados |
| `API_KEY` | Chave secreta para serviços externos |
| `LOG_LEVEL` | Nível de verbosidade dos logs (ex: `DEBUG`) |
| `ZION_ENDPOINT` | URL da rede de resistência |

---

## Arquivos de configuração

### `.env.example` — modelo público (commitado no repositório)

```env
MATRIX_MODE=development
DATABASE_URL=localhost:5432/matrix
API_KEY=dev-oracle-key
LOG_LEVEL=DEBUG
ZION_ENDPOINT=https://zion.local
```

Serve como documentação: mostra quais variáveis são necessárias sem expor valores reais.

### `.env` — arquivo real (nunca commitado)

Cópia do `.env.example` com valores reais preenchidos. Deve estar listado no `.gitignore` para que nunca seja enviado ao repositório — isso protege senhas e chaves secretas de ficarem expostas publicamente.

### `.gitignore`

```
.env
```

Instrui o Git a ignorar o arquivo `.env`. É a linha de defesa que garante que segredos reais não vazem para o controle de versão.

---

## Como testar

```bash
# Sem configuração (deve mostrar avisos de variáveis faltando)
python3 oracle.py

# Com arquivo .env
cp .env.example .env
python3 oracle.py

# Sobrescrevendo via variável de ambiente (tem prioridade sobre o .env)
MATRIX_MODE=production API_KEY=secret123 python3 oracle.py
```

---

## Exemplo de saída

```
ORACLE STATUS: Reading the Matrix...

Configuration loaded:
Mode: development
Database: Connected to local instance
API Access: Authenticated
Log Level: DEBUG
Zion Network: Online

Environment security check:
[OK] No hardcoded secrets detected
[OK] .env file properly configured
[OK] Development configuration active

The Oracle sees all configurations.
```
