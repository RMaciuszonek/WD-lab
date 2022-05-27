import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


def p1():
    sns.set(rc={'figure.figsize': (8, 8)})
    sns.lineplot(x=[1, 2, 3, 4], y=[1, 4, 9, 16], label='linia nr1', color='red', marker='o', linestyle=':')
    sns.lineplot(x=[1, 2, 3, 4], y=[2, 5, 10, 17], label='linia nr2', color='green', marker='^', linestyle=':')
    plt.xlabel('oś x')
    plt.ylabel('oś y')
    plt.title('Wykres liniowy')
    plt.show()


def p2():
    s = pd.Series(np.random.randn(1000))
    s = s.cumsum()
    sns.set()
    wykres = sns.relplot(kind='line', data=s, label='linia')
    wykres.fig.set_size_inches(8, 6)
    wykres.fig.suptitle('Wukres liniowy losowych danych')
    wykres.set_xlabels('indeksy')
    wykres.set_ylabels('wartości')
    wykres.add_legend()
    wykres.figure.subplots_adjust(left=0.1, right=0.9, bottom=0.1, top=0.9)
    plt.show()


def p3():
    sns.set()
    df = pd.read_csv('datasets/iris.data', header=0, sep=',', decimal='.')
    print(df)
    wykres = sns.lineplot(data=df, x=df.index, y=df.iloc[:, 0], hue='class')
    wykres.set_xlabel('indeksy')
    wykres.set_title('Wukres liniowy danych z Iris dataset')
    wykres.legend(title='Rodzaj kwiatu')
    plt.show()



def lab11seaborn():
    p1()
    p2()
    p3()
    # p4()


if __name__ == '__main__':
    lab11seaborn()
