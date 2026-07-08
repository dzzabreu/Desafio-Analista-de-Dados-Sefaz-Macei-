# Desafio Analista de Dados - SEFAZ Maceió 🏛️
> Análise Orçamentária de Despesas por Função e Subfunção das Capitais Brasileiras (Foco: Maceió, 2020-2024).

Este repositório contém a solução para o desafio analítico da SEFAZ Maceió. O projeto foi estruturado utilizando as melhores práticas de Engenharia e Análise de Dados, garantindo automação, governança de dados locais, alta performance com arquivos colunares e queries analíticas de nível governamental.

---

## 📁 Estrutura do Projeto (Árvore de Diretórios)

A arquitetura do projeto segue uma divisão conceitual baseada em camadas de dados (Raw, Processed e Gold), mantendo os scripts de processamento isolados em módulos:

```text
DESAFIO-ANALISTA-DE-Dados-SEFAZ-MACEIÓ/
├── .gitignore                   # Proteção de dados brutos e ambientes virtuais
├── analise.ipynb                # Notebook com as queries SQL e análises finais
├── main.py                      # Maestro centralizador do pipeline de engenharia
├── README.md                    # Documentação do projeto
├── requirements.txt             # Dependências rígidas do projeto
├── data/                        # Repositório de dados locais em camadas
│   ├── gold/
│   │   └── finbra_analytics.duckdb    # Banco analítico otimizado pronto para consultas
│   ├── processed/
│   │   └── finbra_consolidado.parquet # Base de dados unificada e comprimida (Snappy)
│   └── raw/
│       ├── dados_compactos/     # Arquivos ZIP originais baixados
│       └── dados_extraidos/     # Arquivos CSV extraídos sem modificação
├── src/                         # Scripts modulares de engenharia de dados
│   ├── __init__.py
│   ├── config.py                # Mapeamento centralizado de caminhos do projeto
│   ├── extract_data.py          # Automação de descompactação e padronização por ano
│   ├── load_duckdb.py           # Script de carga e modelagem no banco DuckDB
│   └── merge_data.py            # Consolidação, limpeza e engenharia de recursos (Pandas)
└── venv/                        # Ambiente virtual Python isolado

## 🛠️ Pipeline de Engenharia de Dados & Decisões Técnicas

O fluxo de dados é gerenciado ponta a ponta pelo maestro `main.py`, que executa os módulos da pasta `src/` na ordem correta:

### 1. Extração e Padronização (`extract_data.py`)
* **Processo:** Varre a pasta de compactados, descompacta os arquivos ZIP e aplica uma renomeação dinâmica nos arquivos CSV resultantes com base no ano de referência.
* **Justificativa:** Elimina processos manuais suscetíveis a erros e blinda a base histórica contra sobreposições acidentais de arquivos.

### 2. Higienização e Fusão Histórica (`merge_data.py`)
* **Tratamento de Dados Públicos:** Configuração de encoding `Latin-1`, delimitador `;` e descarte automático de linhas de metadados (`skiprows=3`). Converte as strings monetárias no formato brasileiro (ex: `1.000,00`) diretamente para ponto flutuante (`float`) usando as propriedades nativas do Pandas.
* **Algoritmo Stateful Scan (`distingue_conta`):** As tabelas originais misturam Funções e Subfunções em uma única coluna hierárquica baseada em posições e indentação. Desenvolveu-se uma lógica baseada em estado de memória que identifica a "Função Mãe" e propaga seu contexto para as subfunções seguintes, tratando inclusive casos complexos de agrupamentos agregadores (ex: `FUxx - Demais Subfunções`).

### 3. Otimização com Formato Parquet (`merge_data.py`)
* **Armazenamento Otimizado:** Os dados de todos os anos foram unificados (gerando mais de 50 mil linhas) e salvos no formato colunar Parquet com compressão `snappy` dentro da pasta `data/processed/`.
* **Justificativa:** O Parquet reduz drasticamente o consumo de espaço em disco se comparado a um arquivo CSV bruto e otimiza a leitura colunar das queries analíticas.

### 4. Banco Analítico Embarcado (`load_duckdb.py`)
* **Carga de Dados:** O arquivo Parquet processado é ingerido diretamente em um banco analítico DuckDB salvo localmente (`data/gold/finbra_analytics.duckdb`).
* **Justificativa:** O DuckDB funciona como um "SQLite para Analytics", executando queries SQL vetorizadas em altíssima velocidade sem a complexidade de gerenciar um servidor de banco de dados pesado (como PostgreSQL).

## 📊 Principais Conclusões da Análise Fiscal (Passo 4)

As análises foram executadas diretamente no `analise.ipynb` utilizando a interface SQL do DuckDB sobre os dados estruturados de 2020. Os resultados revelam dados críticos sobre o panorama nacional e o município de Maceió:

### 1. O Cenário Nacional e o Impacto da Crise Sanitária
* **O Trio de Ferro:** As funções **Saúde, Educação e Previdência Social** abocanharam juntas **60,23%** de todo o orçamento liquidado e pago por todas as capitais do país em 2020.
* **Foco no Gargalo de Urgência:** No detalhamento por subfunção, a **Assistência Hospitalar e Ambulatorial** consumiu o dobro de recursos da Atenção Básica (13,36% contra 6,49% do total nacional). Isso quantifica o esforço financeiro que as capitais tiveram para abrir leitos de UTI e UPAs no ápice da pandemia.
* **Desigualdade Demográfica:** A análise regional revelou que as capitais do Sul e Sudeste têm sua maior despesa concentrada na Previdência do Regime Estatutário (custo do envelhecimento funcional), enquanto a região Norte direciona a maior parte dos seus recursos ao Ensino Fundamental (reflexo de uma população mais jovem).

### 2. O Diagnóstico Orçamentário de Maceió
* **Pressão na Saúde:** Alinhada ao comportamento da região Nordeste, a principal subfunção de pagamento em Maceió foi a **Assistência Hospitalar e Ambulatorial**, representando **15,18%** de todo o orçamento pago do município (R$ 361,41 milhões).
* **O Peso do "Custo Máquina":** O achado mais crítico do projeto reside na atividade-meio. Somadas, a **Administração Geral do Município** (14,36%) e a **Administração Geral da Saúde** (13,48%) consomem impressionantes **27,84%** do orçamento total pago. Isso evidencia que a estrutura burocrática e operacional da capital possui um custo muito elevado, gerando uma forte rigidez fiscal que reduz a capacidade de investimentos em pontas cruciais, como o Ensino Fundamental (que registrou apenas 7,47% do orçamento municipal).

---

## 🚀 Como Executar o Projeto

1. **Clone o repositório:**
  ```bash
  git clone <link-do-seu-repositorio>
  cd Desafio-Analista-de-Dados-Sefaz-Macei-

2. **Ative o ambiente virtual e garanta as dependências:**
  ```bash
  # No Windows
  .\venv\Scripts\activate

  # Atualize e instale os pacotes necessários
  pip install -r requirements.txt

3. **Execute o pipeline completo de Engenharia de Dados:**
  ```bash
  python main.py

  # Este comando executará automaticamente a extração na pasta raw, fará o merge dos dados via Pandas aplicando as regras de negócio, gerará o arquivo Parquet na camada processed e estruturará o banco DuckDB na camada gold.

4. **Abra o ambiente para explorar as análises:**
  ```bash
  jupyter notebook
