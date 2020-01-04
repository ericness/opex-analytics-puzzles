import survival_supplies


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

