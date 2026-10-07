# Machine Learning Quantitative Strategy

A quantitative research project that uses Machine Learning to generate market signals and compare a systematic strategy against a Buy & Hold benchmark.

The project was developed for educational and portfolio purposes, combining Python, statistics, Machine Learning and quantitative finance concepts.

## Overview

The objective is not to predict financial markets perfectly.

Instead, the project investigates whether a Machine Learning model can identify patterns in historical market data and generate signals that can be evaluated through a simple backtest.

The model classifies whether the asset is expected to have a positive return over the following five trading days.

## Methodology

The project follows these steps:

1. Generate a synthetic historical market dataset.
2. Calculate technical and statistical features.
3. Create a binary target based on future returns.
4. Split the dataset chronologically into training and testing periods.
5. Train a Random Forest classifier.
6. Generate probability-based market signals.
7. Backtest the strategy on unseen data.
8. Compare the results with a Buy & Hold benchmark.

## Features

The model uses features related to:

* Daily returns
* 5-day and 10-day returns
* Moving averages
* Price relative to moving averages
* Moving average ratio
* Momentum
* Historical volatility
* Daily price range
* Closing price position
* Volume variation
* Volume relative to its moving average

## Machine Learning Model

The project uses a `RandomForestClassifier` from scikit-learn.

The model was intentionally evaluated using a chronological train/test split instead of randomly shuffling the observations.

This approach is more appropriate for time-series experiments because future observations should not be used to train a model that is evaluated on the past.

## Backtesting

The strategy starts with a simulated capital of:

**$10,000**

A signal is generated when the model estimates at least a 55% probability of a positive future return.

The backtest evaluates:

* Total return
* Final portfolio value
* Maximum drawdown
* Sharpe ratio
* Percentage of time invested
* Number of operations

The strategy is compared with a Buy & Hold benchmark over the same testing period.

## Results

| Metric           | ML Strategy | Buy & Hold |
| ---------------- | ----------: | ---------: |
| Initial capital  |  $10,000.00 | $10,000.00 |
| Final value      |   $9,394.75 |  $8,451.87 |
| Return           |      -6.05% |    -15.48% |
| Maximum drawdown |      -8.79% |    -19.01% |
| Sharpe ratio     |       -1.47 |      -2.55 |
| Time invested    |      46.39% |       100% |
| Operations       |          13 |          — |

### Interpretation

The Machine Learning strategy did not generate a positive absolute return during the test period.

However, it performed better than the Buy & Hold benchmark in terms of capital preservation:

* Losses were reduced from **15.48% to 6.05%**.
* Maximum drawdown was reduced from **19.01% to 8.79%**.
* The strategy was invested during approximately **46%** of the testing period.

This suggests that the model's signals were more useful for controlling market exposure than for generating positive returns in this experiment.

The result should not be interpreted as evidence that the strategy would be profitable in real financial markets.

## Feature Importance

The Random Forest model also provides feature importance estimates.

The most influential variables in the experiment included:

* 5-day moving average
* 10-day moving average
* 5-day volatility
* 10-day volatility
* Moving average ratio
* 10-day return
* Price relative to the 10-day moving average
* 10-day momentum

These results provide a starting point for investigating which market characteristics contributed most to the model's decisions.

## Project Structure

```text
machine-learning/
├── data/
│   ├── market_data.csv
│   └── generate_data.py
│
├── src/
│   ├── features.py
│   ├── model.py
│   ├── train.py
│   ├── predict.py
│   └── backtest.py
│
├── tests/
│   └── test_model.py
│
└── README.md
```

## Technologies

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Git
* GitHub

## How to Run

Install the project dependencies:

```bash
pip install -r requirements.txt
```

Generate the synthetic market dataset:

```bash
python machine-learning/data/generate_data.py
```

Train and evaluate the model:

```bash
python machine-learning/src/train.py
```

Generate market signals:

```bash
python machine-learning/src/predict.py
```

Run the backtest:

```bash
python machine-learning/src/backtest.py
```

Run the tests:

```bash
python machine-learning/tests/test_model.py
```

## Limitations

This project has several important limitations.

### Synthetic data

The dataset used in this project is synthetically generated and does not represent real financial market data.

### Simplified transaction model

The backtest does not include transaction costs, slippage, taxes, liquidity constraints or other real-world trading costs.

### Simple model

Only a Random Forest classifier is used. More advanced models and validation techniques could produce different results.

### Limited sample

The experiment uses a relatively small dataset and should not be considered statistically conclusive.

### No guarantee of future performance

Historical backtests do not guarantee future results.

## Possible Improvements

Future versions could investigate:

* Real historical market data
* Walk-forward validation
* Cross-validation designed for time series
* Transaction costs and slippage
* Position sizing
* Risk management
* Additional Machine Learning algorithms
* Feature selection
* Hyperparameter optimization
* Probability calibration
* Comparison between multiple strategy thresholds

## Disclaimer

This project is an educational experiment in Machine Learning and quantitative finance.

It is not financial advice and should not be used as a basis for real investment decisions.
