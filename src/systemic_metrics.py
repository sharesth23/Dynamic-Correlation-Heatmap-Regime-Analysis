import numpy as np

def average_correlation(corr_matrix):
    """
    Average pairwise correlation (excluding diagonal)
    """
    n = corr_matrix.shape[0]
    upper = corr_matrix.values[np.triu_indices(n, k=1)]
    return upper.mean()


def eigenvalue_concentration(corr_matrix):
    """
    Proportion of variance explained by first eigenvalue
    """
    eigenvalues = np.linalg.eigvalsh(corr_matrix)
    return eigenvalues[-1] / eigenvalues.sum()
