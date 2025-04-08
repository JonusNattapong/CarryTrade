# Carry Trade Calculator

A Python-based toolkit for analyzing and simulating carry trade strategies in the foreign exchange market.

## What is Carry Trade?

Carry Trade is a strategy traders use to profit from interest rate differentials between two currencies by buying high-interest-rate currencies and selling low-interest-rate currencies. This approach is suitable for holding long-term positions to earn returns from interest rate differences.

## Features

- Calculate carry trade returns and risks based on interest rate differentials
- Identify the best currency pairs for carry trade opportunities
- Simulate carry trade performance over time with realistic exchange rate volatility
- Visualize carry trade metrics including cumulative returns, risks, and Sharpe ratios
- Compare different currency pairs to find optimal trading opportunities

## Currency Pairs for Carry Trading

Common currency pairs for carry trading include:

- **AUD/JPY**: Australian Dollar (high interest) vs Japanese Yen (low interest)
- **NZD/JPY**: New Zealand Dollar (high interest) vs Japanese Yen (low interest)
- **TRY/EUR**: Turkish Lira (high interest) vs Euro (low interest)
- **USD/JPY**: US Dollar (medium-high interest) vs Japanese Yen (low interest)

## Getting Started

### Prerequisites

- Python 3.6+
- NumPy
- Matplotlib

### Usage

```python
# Import the calculator
from carry_trade_calculator import *

# Define currency interest rates
currency_interest_rates = {
    'AUD': 0.04,    # Australia 4.00%
    'NZD': 0.035,   # New Zealand 3.50%
    'TRY': 0.08,    # Turkey 8.00%
    'JPY': -0.001,  # Japan -0.10%
    'EUR': 0.001,   # Euro 0.10%
    'CHF': 0.002,   # Switzerland 0.20%
    'USD': 0.05     # United States 5.00%
}

# Define principal amount
principal = 100000  # 100,000 units

# Identify best carry trade pairs
best_pairs = identify_best_carry_trades(currency_interest_rates)

# Analyze carry trade metrics
metrics = analyze_carry_trade_metrics(currency_interest_rates, principal, simulation_days=180)

# Plot results
plot_carry_trade_simulation(metrics)
plot_risk_return_scatter(metrics)
```

## Risk Considerations

- **Interest Rate Change Risk**: Profit reduction if high-interest-rate countries lower their rates
- **Market Movement Risk**: High market volatility or economic news can increase Carry Trade risks
- **Exchange Rate Risk**: Sudden changes in exchange rates can offset or negate interest rate gains

## Recommended Timeframes

- **Daily (D1)**: For monitoring interest rates and long-term economic analysis
- **Weekly (W1)**: For tracking financial market changes in long-term positions

## License

[MIT](https://choosealicense.com/licenses/mit/)

## References

- [Investopedia: Carry Trade](https://www.investopedia.com/terms/c/currencycarrytrade.asp)
- [Central Bank Rates](https://www.centralbanksrates.com/)