import numpy as np
import random
from collections import defaultdict as ddc
import matplotlib.pyplot as plt
from s02_label_img_dfs_iterative import label_regions


def example_matrix(size, th):
    mat = np.array([
            random.randint(0, 10) for i in range(size**2)
            ]).reshape(size, size)
    return mat, label_regions(th, mat)


def f_size(label_arr: np.array) -> list:
    '''
    label None assumes you want all labelled regions
    Also assumes labels are negative integers
    '''
    n, m = label_arr.shape
    ret = ddc(lambda: 0)
    for i in range(n):
        for j in range(m):
            if label_arr[i, j] >= 0:
                continue
            ret[label_arr[i, j]] += 1
    return ret


if __name__ == '__main__':
    for i in range(1, 10):
        mat, label_mat = example_matrix(50, i)
        sizes = f_size(label_mat)
        plt.hist(list(sizes.values()), bins=[1, 10, 100, 1000])
    plt.show()
