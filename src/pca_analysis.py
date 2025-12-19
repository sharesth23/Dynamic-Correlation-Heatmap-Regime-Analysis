import numpy as np 
from sklearn.decomposition import PCA
import pandas as pd

def correlation_pca(corr_matrix):
    pca = PCA()
    pca.fit(corr_matrix)
    explain_variance = pca.explained_variance_ratio_
    return explain_variance