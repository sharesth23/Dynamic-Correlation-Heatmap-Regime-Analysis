import numpy as np 

def detect_regime(corr_matrix):
    equity_corr = corr_matrix.loc["SP500", "NASDAQ"]
    gold_corr = corr_matrix.loc["SP500" , "GOLD"]


    if equity_corr > 0.7 and gold_corr < 0:
        return "Risk-OFF"
    elif equity_corr < 0.3 and gold_corr > 0:
        return "Risk-ON"
    else:
        return "Neutral"    