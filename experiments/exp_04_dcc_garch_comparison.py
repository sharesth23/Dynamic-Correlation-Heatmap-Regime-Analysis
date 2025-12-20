"""
Reproduces DCC-GARCH vs Rolling Correlation comparison (Figure 4)
"""

import pandas as pd
import matplotlib.pyplot as plt

from src.data_loader import load_data
from src.correlation import rolling_correlation
from src.dcc_garch import fit_dcc_garch
from src.systemic_metrics import average_correlation
from data.tickers import ASSETS

prices, returns = load_data(ASSETS)

rolling_corrs = rolling_correlation(returns, window=60)
dcc_corrs = fit_dcc_garch(returns)

rolling_avg = pd.Series({
    date: average_correlation(corr)
    for date, corr in rolling_corrs.items()
})

dcc_avg = pd.Series({
    date: average_correlation(corr)
    for date, corr in dcc_corrs.items()
})

plt.figure(figsize=(10,5))
rolling_avg.plot(label="Rolling Correlation", alpha=0.7)
dcc_avg.plot(label="DCC-GARCH Correlation", alpha=0.7)
plt.legend()
plt.title("Average Cross-Asset Correlation: Rolling vs DCC-GARCH")

plt.savefig("paper/figures/fig_dcc_vs_rolling.png", dpi=300)
plt.show()
