import numpy as np
from collections import defaultdict as ddc
import matplotlib.pyplot as plt
from s03_create_features import f_size, example_matrix


def generate_dist(n_loops=100, mat_dim=50, th=6):
    '''
    loop over randomly generated 2D arrays filled
    with random integers in range [0:10] and
    figure out distribution of sizes of the connected
    areas.

    Connected area is formed by values < threshold value
    of the array

    dist[dict]: key is region size, value is occurence
    '''
    dist = ddc(lambda: 0)
    for i in range(n_loops):
        _, label_mat = example_matrix(mat_dim, th)
        sizes = f_size(label_mat)  # key is label, value is the size I care about
        for _, value in sizes.items():
            dist[value] += 1
    return dist


if __name__ == '__main__':
    for i in range(1, 10, 2):
        print(i)
        dist = generate_dist(n_loops=1000, mat_dim=50, th=i)
        plt.plot(list(dist.keys()), list(dist.values()), 'o',
                 markersize=4, label=f'thresh: {i}')
    x = np.linspace(0, 1000, 1001)
    plt.title('Connected areas (1000 arrays, size 50x50)')
    plt.legend()
    plt.yscale('log')
    plt.xscale('log')
    plt.xlabel('area size [pixels]')
    plt.ylabel('N Occurrences')
    plt.ylim(bottom=0.9)
    plt.savefig('figs/dist_neighbors_2d_array.png', dpi=300)
    plt.show()
