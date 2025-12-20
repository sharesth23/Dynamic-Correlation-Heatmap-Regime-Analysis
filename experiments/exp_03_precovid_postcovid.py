"""
Reproduces Pre-COVID vs Post-COVID correlation comparison (Figure 3)
"""

from src.data_loader import load_data
from src.visualization import plot_heatmap
from data.tickers import ASSETS

prices, returns = load_data(ASSETS)

pre_covid = returns.loc["2015-01-01":"2019-12-31"]
post_covid = returns.loc["2020-03-01":]

pre_corr = pre_covid.corr()
post_corr = post_covid.corr()

plot_heatmap(
    pre_corr,
    title="Pre-COVID Cross-Asset Correlation Structure"
)

plot_heatmap(
    post_corr,
    title="Post-COVID Cross-Asset Correlation Structure"
)
