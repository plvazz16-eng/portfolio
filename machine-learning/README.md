# Estratégia Quantitativa com Machine Learning

Projeto de pesquisa quantitativa que utiliza **Machine Learning** para gerar sinais de mercado e comparar uma estratégia sistemática com uma referência de **Buy & Hold**.

O projeto foi desenvolvido para fins educacionais e de portfólio, combinando **Python, estatística, Machine Learning e conceitos de finanças quantitativas**.

## Visão geral

O objetivo não é prever o mercado financeiro de forma perfeita.

Em vez disso, o projeto investiga se um modelo de Machine Learning consegue identificar padrões em dados históricos de mercado e gerar sinais que possam ser avaliados por meio de um **backtest**.

O modelo classifica se o ativo terá um retorno positivo nos cinco pregões seguintes.

## Metodologia

O projeto segue as seguintes etapas:

1. Geração de um conjunto de dados sintético de mercado.
2. Cálculo de indicadores técnicos e estatísticos.
3. Criação de uma variável-alvo baseada nos retornos futuros.
4. Divisão cronológica dos dados entre treinamento e teste.
5. Treinamento de um modelo Random Forest.
6. Geração de sinais de mercado baseados em probabilidades.
7. Realização de um backtest utilizando dados não utilizados no treinamento.
8. Comparação dos resultados com uma estratégia Buy & Hold.

## Variáveis utilizadas

O modelo utiliza variáveis relacionadas a:

* Retornos diários
* Retornos de 5 e 10 dias
* Médias móveis
* Preço em relação às médias móveis
* Relação entre médias móveis
* Momentum
* Volatilidade histórica
* Amplitude diária dos preços
* Posição do fechamento dentro da amplitude diária
* Variação do volume
* Volume em relação à sua média móvel

## Modelo de Machine Learning

O projeto utiliza um `RandomForestClassifier` da biblioteca Scikit-learn.

A divisão entre treinamento e teste é feita cronologicamente, sem embaralhar as observações.

Essa abordagem é mais adequada para experimentos

