# Análise de Dados do ENEM

Projeto de análise estatística desenvolvido em Python para explorar o desempenho de estudantes em diferentes áreas do ENEM.

O projeto utiliza estatística descritiva, correlação de Pearson e visualização de dados para identificar padrões e relações entre as notas.

> **Observação:** os dados utilizados atualmente são sintéticos, criados para fins educacionais e de demonstração do projeto.

## Funcionalidades

* Leitura de dados a partir de arquivos CSV
* Cálculo de média
* Cálculo de mediana
* Cálculo de desvio padrão
* Cálculo da correlação de Pearson
* Comparação estatística entre as áreas
* Análise da relação entre Matemática e outras áreas
* Visualização das médias
* Histograma das notas de Matemática
* Gráfico de dispersão entre Matemática e Redação
* Testes automatizados

## Tecnologias

* Python 3
* Matplotlib
* CSV
* Estatística
* Unittest
* Git/GitHub

## Estrutura

```text
analise-enem/
├── data/
│   └── enem_sample.csv
│
├── src/
│   ├── analysis.py
│   ├── stats.py
│   └── visualization.py
│
├── tests/
│   └── test_statistics.py
│
└── README.md
```

## Como executar

A partir da raiz do repositório:

```bash
python analise-enem/src/analysis.py
```

O programa apresenta as principais estatísticas das áreas analisadas e calcula a correlação entre Matemática e as demais disciplinas.

Para gerar as visualizações:

```bash
python analise-enem/src/visualization.py
```

Serão gerados três gráficos:

1. Média das notas por área
2. Distribuição das notas de Matemática
3. Relação entre Matemática e Redação

## Testes

Para executar os testes:

```bash
python analise-enem/tests/test_statistics.py
```

O projeto possui testes para:

* Média
* Mediana
* Mediana em conjuntos pares
* Desvio padrão
* Correlação positiva
* Correlação negativa
* Validação de listas com tamanhos diferentes
* Validação de quantidade insuficiente de dados

## Estatística utilizada

A correlação de Pearson é utilizada para medir a intensidade e a direção da relação linear entre duas variáveis.

O coeficiente varia entre:

```text
-1 ≤ r ≤ 1
```

Valores próximos de:

* `1` indicam forte correlação positiva;
* `0` indicam pouca ou nenhuma relação linear;
* `-1` indicam forte correlação negativa.

É importante destacar que **correlação não implica causalidade**.

## Objetivo

O projeto foi desenvolvido para demonstrar a aplicação prática de Python, matemática e estatística na análise de dados.

Além de trabalhar com cálculos estatísticos, o projeto utiliza visualizações para transformar os resultados numéricos em informações mais fáceis de interpretar.
