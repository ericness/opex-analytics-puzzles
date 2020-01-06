import collections
import itertools
import numpy as np
import pandas as pd
import typing

LOCATIONS = collections.OrderedDict({
    'Base': 0.0,
    'F': 4.0,
    'S': 3.0,
    'B': 1.0,
    'H': 5.0,
    'D': 4.0,
    'C': 2.0,
    'T': 1.0,
    'G': 5.0,
    'P': 3.0,
    'L': 2.0,
})

DISTANCES = pd.DataFrame(
    data=np.array([
        [0.0, 4.9, 5.7, 3.4, 2.1, 2.7, 1.5, 6.2, 4.9, 3.9, 3.6],
        [4.9, 0.0, 6.0, 3.8, 3.5, 5.7, 5.7, 10.0, 9.2, 8.7, 8.1],
        [5.7, 6.0, 0.0, 2.7, 4.0, 3.4, 4.7, 5.9, 6.0, 7.2, 9.0],
        [3.4, 3.8, 2.7, 0.0, 1.4, 2.2, 3.0, 6.4, 5.8, 6.1, 7.0],
        [2.1, 3.5, 4.0, 1.4, 0.0, 2.2, 2.2, 6.5, 5.7, 5.4, 5.7],
        [2.7, 5.7, 3.4, 2.2, 2.2, 0.0, 1.4, 4.3, 3.6, 4.0, 5.7],
        [1.5, 5.7, 4.7, 3.0, 2.2, 1.4, 0.0, 4.7, 3.6, 3.2, 4.3],
        [6.2, 10.0, 5.9, 6.4, 6.5, 4.3, 4.7, 0.0, 1.6, 3.8, 7.3],
        [4.9, 9.2, 6.0, 5.8, 5.7, 3.6, 3.6, 1.6, 0.0, 2.2, 5.7],
        [3.9, 8.7, 7.2, 6.1, 5.4, 4.0, 3.2, 3.8, 2.2, 0.0, 3.5],
        [3.6, 8.1, 9.0, 7.0, 5.7, 5.7, 4.3, 7.3, 5.7, 3.5, 0.0],
    ]),
    columns=LOCATIONS.keys(),
    index=pd.Index(data=LOCATIONS.keys())
)


def generate_fixed_permutations(
    base_name: str,
    locations: typing.List[str],
    perm_length: int,
) -> typing.List[typing.List[str]]:
    """
    Generate path permutations of a specified length which always start and
    end at base_name.
    :param base_name:
        Name of base to begin from.
    :param locations:
        List of locations that can be visited.
    :param perm_length:
        Length of the trip in stops.
    :return:
        List of all possible paths of specified length.
    """
    location_perms = itertools.permutations(locations, perm_length)
    return [[base_name] + list(perm) + [base_name] for perm in location_perms]


def generate_all_permutations(
    base_name: str,
    locations: typing.List[str]
) -> typing.List[typing.List[str]]:
    """
    Generate all path permutations for a set of locations. The paths always
    begin and end at base_name.
    :param locations:
        List of locations that can be visited.
    :return:
        List of all possible paths through locations.
    """
    return [
        perm
        for perm_length in range(1, len(locations) + 1)
        for perm in generate_fixed_permutations(base_name, locations, perm_length)
    ]


def calculate_distance(
    path: typing.List[str],
    distance_matrix: pd.DataFrame
) -> float:
    """
    Calculate distance of a path based on the matrix of distances between
    points.

    :param path:
        List of locations to visit.
    :param distance_matrix:
        Matrix of distances between each pair of locations.
    :return:
        Total distance of the path.
    """
    return sum([
        distance_matrix.loc[path[i], path[i + 1]]
        for i in range(len(path) - 1)
    ])
