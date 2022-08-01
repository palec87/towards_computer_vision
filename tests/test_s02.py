import numpy as np
import pytest
import scripts.s02_label_img_dfs_iterative as m


@pytest.mark.parametrize('mat, ass', [
    (np.array([[1, 2, 3], [2, 2, 4], [7, 8, 9]]),
     np.array([[-1, -1, 3], [-1, -1, 4], [7, 8, 9]])
     ),
    (np.array([[1, 1, 3], [2, 5, 4], [7, 1, 2]]),
     np.array([[-1, -1, 3], [-1, 5, 4], [7, -2, -2]])
     )
    ])
def test_int_array(mat, ass):
    '''
    test labeling simple array
    '''
    result = m.label_regions(th=3, img=mat)
    assert (result - ass).all() == 0
