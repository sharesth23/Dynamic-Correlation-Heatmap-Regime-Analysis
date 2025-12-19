import pandas as pd 

def rolling_correlation(returns, window = 60):
    rolling_corr ={}

    for date in returns.index[window:]:
        corr = returns.loc[:date].tail(window).corr()
        rolling_corr[date] = corr
    return rolling_corr