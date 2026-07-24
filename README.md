# K-Means vs DBSCAN

**Universidade Federal da Paraíba - UFPB**  
**Curso de Licenciatura em Ciência da Computação**  
**Disciplina de Inteligência Artificial – 2026-1**

---
Este projeto apresenta uma análise comparativa de dois algoritmos de agrupamento, **K-Means** e **DBSCAN**, aplicados a um dataset de **Keyboard Analytics**. O objetivo é investigar a utilização de padrões de digitação como uma forma de diferenciação de usuários, analisando a capacidade dos algoritmos em identificar grupos com características semelhantes.

## Objetivos
Comparar a capacidade de cada **algoritmo** em agrupar corretamente padrões de digitação pertencentes a diferentes indivíduos no mesmo **cluster**, investigando a viabilidade do uso de técnicas de agrupamento para a diferenciação de usuários com base em características de **Keyboard Analytics**.

## Dataset
Na aria de segurança e biometria comportamental a análise de digitação busca identificar o padrão unico de um indivíduo digitar, sua "impressão digital comportamental".
Utilizaremos um site famoso nessa aria de pesquisa (), aqui eles disponibilizam de forma gratuita um dataset gigante com mais de 400 partesipantes e alguns resultados que usaremos como comparativos na seção de Análise de Resultados.

Colocar imagem de como a tabela é organizada


Esperamos coletar alguns dados dos membros do grupo para teste comparativos, utilizando uma métricas diferentes de coleta de dados encontrada neste artigo (), as instruções de como executar a coleta estará na seção Como executar o Projeto.

Imagem ilustrativa das tabelas cenafios e tabela


Explicar:
- origem da base open access;
- quais características de digitação são utilizadas;
- possibilidade de inclusão de novos dados coletados.

## Metodologia

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

Passo a passo:

1. Instalar dependências:
```bash
pip install -r requirements.txt



