import numpy as np
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
import scripts.s01_label_img_dfs_recursion as m


def test_int_array():
    '''
    test labeling simple array
    '''
    neighs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    mat = np.array([[1, 2, 3],
                    [2, 2, 4],
                    [7, 8, 9]])
    result = m.DFS(mat, 0, 0, neighs, th=3, label=-1, n=3, m=3)
    ass = np.array([[-1, -1, 3],
                    [-1, -1, 4],
                    [7, 8, 9]])
    assert (result - ass).all() == 0


# if __name__ == "__main__":
#     unittest.main()
