import random
import numpy as np


'''
I am trying to label distinct regions based on
condition (here threshold pixel value).

That is rudimentary object deliniation. One needs to
label pixel by pixel and look at the neighbouring pixels too.

That's how 'depth first search (DFS)' algorithm comes to mind.

Beautiful recursive DFS which I was so proud to learn at leetcode etc.
does not work for large graphs due to the recursion depth limit.

I FIX THE RECURSION DEPTH ISSUE BY USING ITERATIVE DFS INSTEAD.
Otherwise the code is the same as 01_label_img_dfs_recursion.py

I generate only 50x50 image (numpy array) and for
different thresholds run my DFS

I label with negative integers.

Once I increase threshold, connected areas are bigger, and
less numerous, but that also increases the recursion depth.

NO errors, and should be faster as well (no numbers here).
'''


def add_neighbours(set_neighs: set, i, j, neighs, n, m):
    '''chech validity of indices and adds neighbour pixels'''
    for neigh in neighs:
        if (0 <= i+neigh[0] < n) & (0 <= j+neigh[1] < m):
            set_neighs.add(
                (i+neigh[0], j+neigh[1])
                )
    return set_neighs


def traverse(arr: np.array, i: int, j: int,
             neighs: list, th: int, label: int,
             n: int, m: int) -> None:

    to_visit = set()
    add_neighbours(to_visit, i, j, neighs, n, m)

    while to_visit:
        i, j = to_visit.pop()
        if 0 <= arr[i, j] < th:
            arr[i, j] = label
            add_neighbours(to_visit, i, j, neighs, n, m)


def label_regions(th: int, img: np.array) -> np.array:
    '''will identify and label regions with intensity lower than th'''

    arr = img.copy()
    dim1, dim2 = img.shape
    label = -1
    neighs = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    for i in range(dim1):
        for j in range(dim2):
            if 0 <= arr[i, j] < th:
                traverse(arr, i, j, neighs, th, label, dim1, dim2)
                label -= 1
    return arr


if __name__ == '__main__':
    # generate num x num matrix of random integers
    num = 50
    mat = np.array([
        random.randint(0, 10) for i in range(num**2)
        ]).reshape(num, num)
    print(mat)
    for i in range(1, 10):
        print(f'###################\n threshold is {i}\n###################')
        img = label_regions(i, mat)
        print(img)
