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

O projeto utiliza uma base de dados pública da CMU School of Computer Science disponibilizada para pesquisas acadêmicas. Os dados foram obtidos do **CMU Keystroke Benchmark Dataset**, disponível em: <https://www.cs.cmu.edu/~keystroke/>.

O conjunto de dados contém **35 colunas** colunas representando cada tecla da senha **.tie5Roanl**, sendo:

| Coluna | Descrição |
|--------|-----------|
| `subject` | Identificador do participante. |
| `sessionIndex` | Índice da sessão de coleta. |
| `rep` | Número da repetição da senha digitada. |
| `H.<tecla>` | Tempo em que a tecla permaneceu pressionada (*Hold Time*). |
| `DD.<tecla1>.<tecla2>` | Intervalo entre pressionar a primeira e a segunda tecla (*Down-Down*). |
| `UD.<tecla1>.<tecla2>` | Intervalo entre soltar a primeira tecla e pressionar a segunda (*Up-Down*). |

### Exemplo de registro

| subject | sessionIndex | rep | H.period | DD.period.t | UD.period.t | H.t | ... | H.Return |
|---------|-------------:|----:|---------:|------------:|------------:|----:|-----|---------:|
| s002 | 1 | 1 | 0.1491 | 0.3979 | 0.2488 | 0.1069 | ... | 0.0742 |
---

# Metodologia

Os algoritmos **K-Means** e **DBSCAN** possuem características bastante distintas e são indicados para diferentes cenários de agrupamento. Este trabalho busca avaliar qual deles apresenta melhor desempenho na identificação de padrões de digitação.

## Pré-processamento

Antes do treinamento dos modelos, foi realizado o pré-processamento do conjunto de dados com o objetivo de garantir a qualidade e a consistência das informações utilizadas.

As etapas realizadas foram:

- **Remoção de valores ausentes:** foram descartadas todas as linhas que continham pelo menos um valor ausente (`NaN`).
- **Remoção de colunas de identificação:** as colunas `subject`, `sessionIndex` e `rep` foram removidas por serem apenas identificadores dos participantes e das sessões, não contribuindo para o aprendizado dos modelos.
- **Tratamento de valores negativos:** registros com valores negativos em atributos que representam tempos de pressionamento (`H`) ou intervalos entre pressionamentos (`DD`) podem indicar inconsistências na coleta e devem ser removidos. Já valores negativos em atributos `UD` (Up-Down) foram mantidos, pois podem representar a sobreposição natural entre teclas durante a digitação.
- **Remoção de registros duplicados:** caso existam amostras duplicadas, elas são removidas para evitar redundância no conjunto de dados.
- **Padronização dos atributos:** os atributos numéricos são padronizados utilizando o **StandardScaler**, tornando-os comparáveis e adequados para algoritmos sensíveis à escala dos dados.

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
caso apareça o erro:
```bash
.\.venv\Scripts\Activate.ps1 : ...
No linha:1 caractere:1
+ .\.venv\Scripts\Activate.ps1
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : ErrodeSegurança: (:) [], PSSecurityException
    + FullyQualifiedErrorId : UnauthorizedAccess
```
utilise
```bash
Scope Process -ExecutionPolicy Bypass
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
python -m app.app
```

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

