import matplotlib.pyplot as plt
import seaborn as sns

def plot_count(df, column_name):
    sns.countplot(x=column_name, data=df)
    plt.show()
