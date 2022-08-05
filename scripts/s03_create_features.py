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


def f_size(label_arr: np.array) -> dict:
    """returns sizes (N pixels) of labelled area.
    Assumes labels are neg. int

    Args:
        label_arr (np.array): array, where some areas are
            labelled

    Returns:
        dict: key is label, value is n pixels
    """
    n, m = label_arr.shape
    sizes = ddc(lambda: 0)
    coords = ddc(lambda: [])
    for i in range(n):
        for j in range(m):
            if label_arr[i, j] >= 0:
                continue
            sizes[label_arr[i, j]] += 1
            coords[label_arr[i, j]].append((i, j))
    return sizes, coords


def fractal_dim(arr, label='all', area_size_th=1000):
    '''box counting algo
    calculates actually Minkowski-Bouligand dimension
    '''
    sizes, indices = f_size(arr)
    h = dict()
    for label, idx_arr in indices.items():
        if sizes[label] > area_size_th:
            h[label] = get_histogram(idx_arr)
    return h


def calc_frac_dim_from_hist(h):
    fractals = []
    for _, key in enumerate(h):
        x_axis = []
        n_non_empty = []

        for hist in h[key]:
            x_axis.append(
                (hist[1][1] - hist[1][0])
            )
            n_non_empty.append(
                np.sum(hist[0] > 0)
            )
        coeffs = np.polyfit(np.log10(x_axis),
                            np.log10(n_non_empty),
                            1)
        fractals.append((x_axis, n_non_empty, coeffs))
    return fractals


def plot_fractals(fractals, save=False):
    for i, fractal in enumerate(fractals):
        x_axis, non_empty, coeffs = fractal
        plt.plot(
            np.log10(x_axis),
            np.log10(non_empty), 'o',
            markersize=3, color='C'+str(i))
        plt.plot(
            np.log10(x_axis),
            np.polyval(coeffs, np.log10(x_axis)),
            color='C'+str(i),
            label=-np.round(coeffs[0], 2))

    if save:
        plt.savefig('figs/fractals.png', dpi=300)
    plt.legend()
    plt.show()


def area_edge_idx(idx_array: np.array) -> tuple:
    xmin, xmax, ymin, ymax = 1e9, 0, 1e9, 0
    for idx in idx_array:
        ymin = min(idx[0], ymin)
        ymax = max(idx[0], ymax)
        xmin = min(idx[1], xmin)
        xmax = max(idx[1], xmax)
    return (ymin, ymax+1, xmin, xmax+1)


def get_histogram(idx_arr: np.array):
    # log scale
    edges = area_edge_idx(idx_arr)
    max_range = min(edges[1]-edges[0], edges[3]-edges[2])
    hist_list = []
    bin_sizes = np.logspace(
                    0.1, np.log10(max_range), num=5,
                    endpoint=False, base=10)
    bin_sizes = list(map(int, bin_sizes))
    for bin_size in bin_sizes:
        x = np.array([k[0] for k in idx_arr])
        y = np.array([k[1] for k in idx_arr])
        hist_list.append(
            np.histogram2d(x, y,
                           bins=(
                                np.arange(edges[0], edges[1], bin_size),
                                np.arange(edges[2], edges[3], bin_size)),
                           ),
                        )
    return hist_list


def filter_areas_size(sizes: dict, threshold: int) -> dict:
    return dict([item for item in sizes.items() if item.value > threshold])


def box_count(label_arr, box_size):
    ''' apply squares of given size'''
    pass


if __name__ == '__main__':
    # demo for the f_size
    # for i in range(1, 10):
    #     mat, label_mat = example_matrix(50, i)
    #     sizes = f_size(label_mat)
    #     plt.hist(list(sizes.values()), bins=[1, 10, 100, 1000])
    # plt.show()

    # demo for fractal dim
    mat, label_mat = example_matrix(50, 6)
    h = fractal_dim(label_mat, area_size_th=20)
    fdims = calc_frac_dim_from_hist(h)
    plot_fractals(fdims)

    # col_counter = 0
    # for i, key in enumerate(h):
    #     # here I need to count number of non-empty fields.
    #     x_axis = []
    #     n_non_empty = []

    #     for hist in h[key]:
    #         x_axis.append(
    #             (hist[1][1] - hist[1][0])
    #         )
    #         n_non_empty.append(
    #             np.sum(hist[0] > 0)
    #         )
    #     plt.plot(np.log10(x_axis),
    #              np.log10(n_non_empty), 'o',
    #              markersize=3, color='C'+str(col_counter))
    #     coeffs = np.polyfit(np.log10(x_axis), np.log10(n_non_empty), 1)
    #     plt.plot(np.log10(x_axis),
    #              np.polyval(coeffs, np.log10(x_axis)),
    #              color='C'+str(col_counter),
    #              label=-np.round(coeffs[0], 2))
    #     col_counter += 1
    # plt.legend()
    # plt.show()
