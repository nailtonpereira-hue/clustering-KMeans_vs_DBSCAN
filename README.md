# K-Means vs DBSCAN

**Universidade Federal da Paraíba - UFPB**  
**Curso de Licenciatura em Ciência da Computação**  
**Disciplina de Inteligência Artificial – 2026-1**

---
Este projeto apresenta uma análise comparativa de dois algoritmos de agrupamento, **K-Means** e **DBSCAN**, aplicados a um dataset de **Keyboard Analytics**. O objetivo é investigar a utilização de padrões de digitação como uma forma de diferenciação de usuários, analisando a capacidade dos algoritmos em identificar grupos com características semelhantes.

## Objetivos
Comparar a capacidade de cada **algoritmo** em agrupar corretamente padrões de digitação pertencentes a diferentes indivíduos no mesmo **cluster**, investigando a viabilidade do uso de técnicas de agrupamento para a diferenciação de usuários com base em características de **Keyboard Analytics**.

## Dataset
Na aria de segurança e biometria comportamental a análise de digitação busca identificar o padrão unico de um indivíduo digitar, sua "impressão digital comportamental". Explicar quais dados vao pra tabela.

(link para assesar site )

Aqui eles disponibilizam de forma gratuita um dataset gigante com mais de 400 partesipantes e alguns resultados que usaremos como comparativos na seção de Análise de Resultados.

Colocar imagem de como a tabela é organizada

()
As instruções de como executar a coleta estará na seção Como executar o Projeto. Esperamos coletar alguns dados dos membros do grupo para teste comparativos, utilizando uma métricas diferentes de coleta de dados encontrada no artigo acima.

Imagem ilustrativa das tabelas cenafios e tabela


Explicar:
- origem da base open access;
- quais características de digitação são utilizadas;
- possibilidade de inclusão de novos dados coletados.

## Metodologia
O k-mens e dbscan são Algoritmos de agrupamento bem distintos para contextos diferentes, esperamos analisar qual deles se encaixa nesse contexto.

### Coleta de Dados
Explicar:
- como a coleta funciona;
- quais métricas são capturadas (ex.: tempo entre teclas, tempo de pressionamento);
- como executar o código de coleta;
- formato dos dados gerados.

### Pré-processamento dos Dados
Explicar:
- limpeza dos dados;
- tratamento de valores ausentes;
- normalização ou padronização;
- preparação dos dados para os algoritmos.

### K-Means
Explicar:
- funcionamento básico;
- parâmetros utilizados;
- como executar;
- critérios de avaliação.

### DBSCAN
Explicar:
- funcionamento básico;
- parâmetros utilizados (eps, min_samples);
- como executar;
- critérios de avaliação.

## Análise dos Resultados

Explicar:
- quais métricas serão utilizadas;
- comparação entre os clusters gerados;
- gráficos utilizados (se houver);
- interpretação dos resultados.

Exemplo:
- Silhouette Score;
- ARI (Adjusted Rand Index);
- comparação entre grupos encontrados e usuários reais.

## Como Executar o Projeto

## 1. Clonar o repositório

```bash
git clone <URL_DO_REPOSITORIO>
cd <NOME_DO_PROJETO>
```

---

## 2. Criar um ambiente virtual

É recomendado utilizar um ambiente virtual (`venv`) para isolar as dependências do projeto.

### Windows

```bash
python -m venv .venv
```

ou

```bash
py -m venv .venv
```

### Linux/macOS

```bash
python3 -m venv .venv
```

---

## 3. Ativar o ambiente virtual

### Windows (PowerShell)

```powershell
.\.venv\Scripts\Activate.ps1
```

### Windows (CMD)

```cmd
.\.venv\Scripts\activate.bat
```

### Linux/macOS

```bash
source .venv/bin/activate
```

Após a ativação, o terminal deverá exibir algo semelhante a:

```text
(.venv) C:\Users\usuario\projeto>
```

---

## 4. Instalar as dependências

Com o ambiente virtual ativado, execute:

```bash
pip install -r requirements.txt
```

---

## 5. Executar o projeto

Exemplo:

```bash
python app.py
```

ou

```bash
python app/app.py
```

(depende da estrutura do projeto)

---

## 6. Desativar o ambiente virtual

Quando terminar de utilizar o projeto:

```bash
deactivate
```

---

## Observações

- O ambiente virtual (`.venv`) **não deve ser enviado para o GitHub**. Adicione a pasta `.venv` ao arquivo `.gitignore`.
- Cada desenvolvedor deve criar seu próprio ambiente virtual ao clonar o projeto.
- Caso novas bibliotecas sejam instaladas, atualize o arquivo `requirements.txt` com:

```bash
pip freeze > requirements.txt
```

