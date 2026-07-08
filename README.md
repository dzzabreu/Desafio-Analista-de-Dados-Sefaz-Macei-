# 🏛️ Desafio Analista de Dados - SEFAZ Maceió

> Análise Orçamentária de Despesas por Função e Subfunção das Capitais Brasileiras (Foco: Maceió, 2020–2024)

Este repositório contém a solução para o desafio técnico para a vaga de **Analista de Dados da SEFAZ Maceió**.

O projeto foi estruturado seguindo boas práticas de **Engenharia e Análise de Dados**, contemplando:

- Automação completa do pipeline de dados;
- Organização em camadas (Raw → Processed → Gold);
- Armazenamento otimizado com **Parquet**;
- Banco analítico local utilizando **DuckDB**;
- Consultas SQL para exploração dos dados e geração de insights.

---

# 📁 Estrutura do Projeto

```text
DESAFIO-ANALISTA-DE-DADOS-SEFAZ-MACEIO/
├── .gitignore                   # Proteção de dados brutos e ambientes virtuais
├── analise.ipynb                # Notebook com análises e consultas SQL
├── main.py                      # Pipeline principal
├── README.md
├── requirements.txt
├── data/
│   ├── gold/
│   │   └── finbra_analytics.duckdb
│   ├── processed/
│   │   └── finbra_consolidado.parquet
│   └── raw/
│       ├── dados_compactos/
│       └── dados_extraidos/
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── extract_data.py
│   ├── load_duckdb.py
│   └── merge_data.py
└── venv/
```

---

# 🛠️ Pipeline de Engenharia de Dados

O fluxo é orquestrado pelo arquivo **`main.py`**, responsável por executar cada etapa da engenharia de dados.

## 1. Extração e Padronização (`extract_data.py`)

### Processo

- Percorre automaticamente os arquivos ZIP.
- Descompacta os CSVs.
- Renomeia cada arquivo conforme seu ano de referência.

### Objetivo

Eliminar tarefas manuais e evitar sobrescritas acidentais da base histórica.

---

## 2. Limpeza e Consolidação (`merge_data.py`)

### Tratamento dos dados públicos

- Encoding: `Latin-1`
- Delimitador: `;`
- Remoção automática das linhas de metadados (`skiprows=3`)
- Conversão automática de valores monetários brasileiros para `float`

### Identificação de Funções e Subfunções

As planilhas do FINBRA misturam Funções e Subfunções em uma única coluna hierárquica.

Foi desenvolvido um algoritmo (`distingue_conta`) que:

- identifica a Função principal;
- mantém seu contexto em memória;
- propaga essa informação para as Subfunções seguintes;
- trata corretamente agrupamentos como:

```
FUxx - Demais Subfunções
```

---

## 3. Otimização com Parquet

Após a consolidação:

- todos os anos são unificados;
- gera-se uma base com mais de **50 mil registros**;
- os dados são gravados em **Parquet** utilizando compressão **Snappy**.

### Vantagens

- menor espaço em disco;
- leitura extremamente rápida;
- formato ideal para análises.

---

## 4. Banco Analítico com DuckDB (`load_duckdb.py`)

O arquivo Parquet é carregado diretamente para um banco DuckDB local.

```
data/gold/finbra_analytics.duckdb
```

### Justificativa

O DuckDB oferece:

- alta performance;
- execução vetorizada de SQL;
- simplicidade de uso;
- dispensa servidores de banco de dados.

É uma excelente solução para projetos analíticos locais.

---

# 📊 Principais Resultados da Análise

As consultas foram executadas utilizando SQL diretamente sobre o DuckDB.

## 🇧🇷 Panorama Nacional (2020)

### Saúde, Educação e Previdência

As três funções representaram juntas:

**60,23%** de todo o orçamento liquidado e pago pelas capitais brasileiras.

---

### Assistência Hospitalar

A subfunção **Assistência Hospitalar e Ambulatorial** respondeu por:

- **13,36%** do orçamento nacional

Enquanto a **Atenção Básica** representou apenas:

- **6,49%**

O resultado evidencia o forte impacto financeiro provocado pela pandemia da COVID-19.

---

### Diferenças Regionais

A análise mostrou perfis bastante distintos entre as regiões.

**Sul e Sudeste**

- maior concentração de despesas em Previdência do Regime Estatutário.

**Norte**

- maior concentração em Ensino Fundamental.

---

## 🏙️ Diagnóstico de Maceió

### Saúde

A principal subfunção de pagamento foi:

**Assistência Hospitalar e Ambulatorial**

Representando:

- **15,18%** do orçamento pago
- aproximadamente **R$ 361,41 milhões**

---

### Custo Administrativo

O principal achado do projeto foi o peso da estrutura administrativa.

Somadas:

- Administração Geral
- Administração Geral da Saúde

representam:

**27,84%** de todo o orçamento municipal.

Esse resultado indica elevada rigidez fiscal, reduzindo o espaço para investimentos em áreas finalísticas, como o Ensino Fundamental, que respondeu por apenas **7,47%** do orçamento.

---

# 🚀 Como Executar

## 1. Clone o repositório

```bash
git clone <link-do-repositorio>
cd Desafio-Analista-de-Dados-SEFAZ-Maceio
```

---

## 2. Ative o ambiente virtual

### Windows

```bash
.\venv\Scripts\activate
```

---

## 3. Instale as dependências

```bash
pip install -r requirements.txt
```

---

## 4. Execute o pipeline

```bash
python main.py
```

O pipeline irá automaticamente:

- extrair os arquivos ZIP;
- padronizar os dados;
- consolidar os anos em uma única base;
- gerar o arquivo Parquet;
- criar o banco DuckDB.

---

## 5. Abra o notebook de análise

```bash
jupyter notebook
```

Abra o arquivo:

```
analise.ipynb
```

para explorar todas as consultas SQL e as análises desenvolvidas.

---

# 🧰 Tecnologias Utilizadas

- Python
- Pandas
- DuckDB
- Parquet
- Jupyter Notebook
- SQL

---

# 📌 Autor

**Andrezza Abreu de Magalhães**

Projeto desenvolvido como solução para o desafio técnico da **SEFAZ Maceió**.