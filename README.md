# K-Means vs DBSCAN

**Universidade Federal da Paraíba (UFPB)**  
**Curso de Licenciatura em Ciência da Computação**  
**Disciplina de Inteligência Artificial – 2026.1**

---

## Sobre o Projeto

Este projeto apresenta uma análise comparativa entre os algoritmos de agrupamento **K-Means** e **DBSCAN**, aplicados a um conjunto de dados de **Keyboard Analytics** (dinâmica de digitação).

O objetivo é investigar a capacidade desses algoritmos em identificar padrões de digitação pertencentes a diferentes usuários, avaliando a viabilidade do uso de técnicas de agrupamento na biometria comportamental.

---

## Objetivos

- Comparar o desempenho dos algoritmos **K-Means** e **DBSCAN**.
- Avaliar a capacidade de agrupar corretamente padrões de digitação de um mesmo usuário.
- Analisar a aplicação de técnicas de agrupamento na diferenciação de usuários por meio de características de **Keyboard Analytics**.

---

# Dataset

Na área de segurança e biometria comportamental, a análise da dinâmica de digitação busca identificar padrões únicos de cada indivíduo, funcionando como uma espécie de **impressão digital comportamental**.

O projeto utiliza uma base de dados pública (*Open Access*) contendo registros de mais de **400 participantes**, disponibilizada para pesquisas acadêmicas.

**Nesta seção serão apresentados:**

- origem da base de dados;
- características utilizadas na análise;
- descrição das colunas da tabela;
- imagem ilustrativa da organização do dataset;
- link para o repositório original da base de dados.

Além da base pública, o projeto permitirá a inclusão de novos dados coletados pelos integrantes do grupo, utilizando uma metodologia de coleta adaptada para este trabalho.

---

# Metodologia

Os algoritmos **K-Means** e **DBSCAN** possuem características bastante distintas e são indicados para diferentes cenários de agrupamento. Este trabalho busca avaliar qual deles apresenta melhor desempenho na identificação de padrões de digitação.

## Coleta de Dados

Descrever:

- funcionamento da coleta;
- métricas capturadas (tempo de pressionamento, tempo entre teclas, etc.);
- formato dos arquivos gerados;
- como executar o sistema de coleta.

---

## Pré-processamento

Descrever:

- limpeza dos dados;
- tratamento de valores ausentes;
- normalização ou padronização;
- preparação dos dados para os algoritmos.

---

## K-Means

Apresentar:

- funcionamento do algoritmo;
- parâmetros utilizados;
- forma de execução;
- critérios de avaliação.

---

## DBSCAN

Apresentar:

- funcionamento do algoritmo;
- parâmetros utilizados (`eps` e `min_samples`);
- forma de execução;
- critérios de avaliação.

---

# Análise dos Resultados

Nesta seção serão comparados os agrupamentos produzidos pelos algoritmos por meio de métricas quantitativas e análises visuais.

Entre as métricas utilizadas estão:

- Silhouette Score;
- Adjusted Rand Index (ARI);
- comparação entre os clusters encontrados e os usuários reais;
- gráficos e visualizações dos agrupamentos.

---

# Como Executar o Projeto

## 1. Clonar o repositório

```bash
git clone <URL_DO_REPOSITORIO>
cd <NOME_DO_PROJETO>
```

## 2. Criar e ativar o ambiente virtual

### Windows

```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### Linux/macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

## 4. Executar o projeto

```bash
python app.py
```

ou

```bash
python app/app.py
```

(dependendo da estrutura do projeto)

## Observações

- Cada usuário deve criar seu próprio ambiente virtual (`.venv`).
- A pasta `.venv` não deve ser enviada ao GitHub.
- Sempre que novas bibliotecas forem adicionadas ao projeto, atualize o arquivo `requirements.txt`:

```bash
pip freeze > requirements.txt
```

Para sair do ambiente virtual:

```bash
deactivate
```

