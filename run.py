from data.tickers import ASSETS 
from src.data_loader import load_data 
from src.correlation import rolling_correlation
from src.visualization import plot_heatmap
from src.regime import detect_regime


prices, returns = load_data(ASSETS)

dates = list(rolling_corrs.keys())
calm_date = dates[100]
stress_date = dates[-1]

for date , label in zip([calm_date , stress_date] , ["Calm Market", "Recent/Stress"] ):
    corr = rolling_corrs[date]
    regime = detect_regime(corr)
    plot_heatmap( corr , f"{label} Correlation heatmap ",  regime)
    