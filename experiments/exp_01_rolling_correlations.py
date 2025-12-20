from src.data_loader import load_data
from src.correlation import rolling_correlation
from src.visualization import plot_heatmap
from data.tickers import ASSETS

prices, returns = load_data(ASSETS)
rolling_corrs = rolling_correlation(returns, window=60)

# Select representative calm & stress dates
dates = list(rolling_corrs.keys())
calm_date = dates[200]
stress_date = dates[-1]

plot_heatmap(
    rolling_corrs[calm_date],
    title="Rolling Correlation Heatmap (Calm Regime)"
)

plot_heatmap(
    rolling_corrs[stress_date],
    title="Rolling Correlation Heatmap (Stress Regime)"
)