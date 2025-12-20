
import pandas as pd
import matplotlib.pyplot as plt

from src.data_loader import load_data
from src.correlation import rolling_correlation
from src.systemic_metrics import eigenvalue_concentration
from data.tickers import ASSETS

prices, returns = load_data(ASSETS)
rolling_corrs = rolling_correlation(returns, window=60)

pc1_series = {
    date: eigenvalue_concentration(corr)
    for date, corr in rolling_corrs.items()
}

pc1 = pd.Series(pc1_series)

pc1.plot(
    figsize=(10,5),
    title="Systemic Risk Indicator (PC1 Explained Variance)"
)

plt.savefig("paper/figures/fig_pca_systemic_risk.png", dpi=300)
plt.show()