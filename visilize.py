import os

import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

LOG_FILE = 'logs/loss.log'


def load_data(input_path):
    '''
    加载处理后的日志数据
    :return:
    '''
    data = pd.read_csv(input_path, delimiter=' ',names=['loss', 'step'], header=None)
    print(data.head())
    return data


def plot_loss():
    '''
    画loss的折线图
    '''
    data = load_data(LOG_FILE)
    ax = sns.pointplot(x="step", y='loss', data=data)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=90, ha="right",fontsize=5)
    plt.show()


if __name__ == '__main__':
    plot_loss()

