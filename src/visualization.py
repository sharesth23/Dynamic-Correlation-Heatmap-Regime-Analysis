import seaborn as sns 
import matplotlib.pyplot as plt

def plot_heatmap(corr_matrix , title , regime = None):
    plt.figure(figsize = (10,8))
    sns.heatmap(
        corr_matrix,
        annot = True ,
        cmap = "coolwarm ", 
        center = 0,
        fmt = ".2f"
    )

    if regime :
        title += f" | Regime: {regime}"

    plt.title(title)
    plt.show()
    