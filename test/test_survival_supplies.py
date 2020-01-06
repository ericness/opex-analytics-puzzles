import numpy as np
import pandas as pd
import survival_supplies

TEST_DISTANCES = pd.DataFrame(
    data=np.array([
        [0.0, 2.0, 3.0],
        [2.0, 0.0, 4.0],
        [3.0, 4.0, 0.0],

    ]),
    columns=['a', 'b', 'c'],
    index=['a', 'b', 'c'],
)



def test_generate_fixed_permutations():
    """Should generate trips of fixed length"""
    result = survival_supplies.generate_fixed_permutations(
        'a', ['b', 'c', 'd'], 2
    )
    assert result == [
        ['a', 'b', 'c', 'a'],
        ['a', 'b', 'd', 'a'],
        ['a', 'c', 'b', 'a'],
        ['a', 'c', 'd', 'a'],
        ['a', 'd', 'b', 'a'],
        ['a', 'd', 'c', 'a'],
    ]


def test_generate_all_permutations():
    """Should generate all possible trips"""
    result = survival_supplies.generate_all_permutations(
        'a', ['b', 'c', 'd']
    )
    assert result == [
        ['a', 'b', 'a'],
        ['a', 'c', 'a'],
        ['a', 'd', 'a'],
        ['a', 'b', 'c', 'a'],
        ['a', 'b', 'd', 'a'],
        ['a', 'c', 'b', 'a'],
        ['a', 'c', 'd', 'a'],
        ['a', 'd', 'b', 'a'],
        ['a', 'd', 'c', 'a'],
        ['a', 'b', 'c', 'd', 'a'],
        ['a', 'b', 'd', 'c', 'a'],
        ['a', 'c', 'b', 'd', 'a'],
        ['a', 'c', 'd', 'b', 'a'],
        ['a', 'd', 'b', 'c', 'a'],
        ['a', 'd', 'c', 'b', 'a'],
    ]


def test_calculate_distance():
    """Should calculate distance of path"""
    test_path = ['a', 'b', 'c', 'a']
    result = survival_supplies.calculate_distance(test_path, TEST_DISTANCES)
    assert result == 9.0
