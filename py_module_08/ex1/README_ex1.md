# Exercise 1 — Loading Programs

**Arquivo:** `loading.py`
**Módulos autorizados:** `pandas`, `numpy`, `matplotlib`, `requests`, `sys`, `importlib`

---

## O que o programa faz

Verifica se as dependências necessárias estão instaladas, carrega e processa dados simulados usando NumPy e pandas, e gera uma visualização com matplotlib. Demonstra o uso de `pip` e `Poetry` para gerenciamento de pacotes.

---

## Funções e módulos utilizados

### `importlib.import_module()`

```python
module = importlib.import_module(module_name)
```

Importa um módulo **pelo nome como string**, em tempo de execução. Diferente do `import` estático, permite tentar importar um pacote e capturar o erro se ele não estiver instalado, sem que o programa quebre imediatamente ao ser iniciado. É a base da função `load_dependency()`, que detecta pacotes faltando e exibe mensagens úteis.

---

### `getattr(module, "__version__", "unknown")`

```python
version = getattr(module, "__version__", "unknown")
```

Acessa o atributo `__version__` de um módulo de forma segura. Se o atributo não existir, retorna `"unknown"` em vez de lançar um erro. Usado para exibir a versão de cada pacote instalado.

---

### `sys.exit()`

```python
sys.exit(1)
```

Encerra o programa imediatamente com um código de saída. O valor `1` indica erro. Chamado quando uma dependência obrigatória não está instalada, impedindo que o programa continue em estado inválido.

---

### `numpy.random.randint()`

```python
matrix_data = numpy.random.randint(0, 100, 1000)
```

Gera um array de 1000 números inteiros aleatórios entre 0 e 99. É o **gerador do dataset simulado** — o subject exige que o numpy seja a fonte dos dados, não listas fixas nem `range()`.

---

### `pandas.DataFrame()`

```python
data_frame = pandas.DataFrame({"matrix_value": matrix_data})
```

Cria uma estrutura de dados tabular (como uma planilha) a partir do array numpy. O pandas organiza os dados em colunas nomeadas, facilitando manipulação, filtragem e análise.

---

### `len()`

```python
print(f"Processing {len(data_frame)} data points...")
```

Retorna o número de linhas do DataFrame. Usado para confirmar a quantidade de dados sendo processados.

---

### `matplotlib.pyplot`

```python
pyplot.figure()
pyplot.plot(data_frame["matrix_value"])
pyplot.title("Matrix Data Analysis")
pyplot.xlabel("Data point")
pyplot.ylabel("Matrix value")
pyplot.savefig("matrix_analysis.png")
pyplot.close()
```

Conjunto de funções para criar visualizações:

| Função | O que faz |
|---|---|
| `figure()` | Cria uma nova figura (canvas) para o gráfico |
| `plot()` | Desenha uma linha com os dados da coluna |
| `title()` | Define o título do gráfico |
| `xlabel()` / `ylabel()` | Nomeia os eixos X e Y |
| `savefig()` | Salva o gráfico em um arquivo `.png` |
| `close()` | Libera a memória fechando a figura |

---

## Arquivos de dependência

### `requirements.txt` — para uso com pip

```
pandas
requests
matplotlib
numpy
```

Instalação:
```bash
pip install -r requirements.txt
```

### `pyproject.toml` — para uso com Poetry

```toml
[tool.poetry.dependencies]
python = "^3.10"
pandas = "*"
requests = "*"
matplotlib = "*"
numpy = "*"
```

Instalação:
```bash
poetry install
poetry run python loading.py
```

---

## Exemplo de saída

```
Loading Programs

LOADING STATUS: Loading programs...

Checking dependencies:
[OK] pandas (2.1.0) - Data manipulation ready
[OK] numpy (1.25.0) - Numerical computation ready
[OK] requests (2.31.0) - Network access ready
[OK] matplotlib (3.7.2) - Visualization ready

Analyzing Matrix data...
Processing 1000 data points...
Generating visualization...

Analysis complete!
Results saved to: matrix_analysis.png
```
