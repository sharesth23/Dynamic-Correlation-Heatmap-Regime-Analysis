from data.tickers import ASSETS 
from src.data_loader import load_data 
from src.correlation import rolling_correlation
from src.visualization import plot_heatmap
from src.regime import detect_regime
from src.pca_analysis import correlation_pca


pca_series = {}

for date, corr in rolling_corrs.items():
    pca_var = correlation_pca(corr)
    pca_series[date] = pca_var[0]  # PC1

import pandas as pd
pca_df = pd.Series(pca_series)

pca_df.plot(
    title="Systemic Risk Indicator (PC1 Explained Variance)",
    figsize=(10,5)
)


prices, returns = load_data(ASSETS)

dates = list(rolling_corrs.keys())
calm_date = dates[100]
stress_date = dates[-1]

for date , label in zip([calm_date , stress_date] , ["Calm Market", "Recent/Stress"] ):
    corr = rolling_corrs[date]
    regime = detect_regime(corr)
    plot_heatmap( corr , f"{label} Correlation heatmap ",  regime)



pre_covid = returns.loc["2015-01-01":"2019-12-31"]
post_covid = returns.loc["2020-03-01":]

pre_corr = pre_covid.corr()
post_corr = post_covid.corr()

plot_heatmap(pre_corr, "Pre-COVID Correlation Heatmap", regime="Normal Regime")
plot_heatmap(post_corr, "Post-COVID Correlation Heatmap", regime="High Correlation Regime")

    