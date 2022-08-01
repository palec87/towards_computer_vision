import numpy as np
import random
from collections import defaultdict as ddc
import matplotlib.pyplot as plt
from s02_label_img_dfs_iterative import label_regions


def example_matrix(size):
    mat = np.array([
            random.randint(0, 10) for i in range(size**2)
            ]).reshape(size, size)
    return mat, label_regions(6, mat)


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
    mat, label_mat = example_matrix(50)
    sizes = f_size(label_mat)
    print(mat, label_mat, sizes)
    plt.plot(list(sizes.keys()),
             list(sizes.values()), 'ob', markersize=10)
    plt.show()
    # plt.hist(sizes.keys(), sizes.values())
    # plt.show()
