import sympy

dice1_1, dice1_2, dice1_3, dice1_4, dice1_5, dice1_6 = sympy.symbols(
    "dice1_1 dice1_2 dice1_3 dice1_4 dice1_6 dice1_6"
)
dice2_1, dice2_2, dice2_3, dice2_4, dice2_5, dice2_6 = sympy.symbols(
    "dice2_1 dice2_2 dice2_3 dice2_4 dice2_6 dice2_6"
)

solution = sympy.solve(
    [
        dice1_1 * dice2_1 - (1.0 / 11.0),
        dice1_1 * dice2_2 + dice1_2 * dice2_1 - (1.0 / 11.0),
        dice1_1 * dice2_3
        + dice1_2 * dice2_2
        + dice1_3 * dice2_1
        - (1.0 / 11.0),
        dice1_1 * dice2_4
        + dice1_2 * dice2_3
        + dice1_3 * dice2_2
        + dice1_4 * dice2_1
        - (1.0 / 11.0),
        dice1_1 * dice2_5
        + dice1_2 * dice2_4
        + dice1_3 * dice2_3
        + dice1_4 * dice2_2
        + dice1_5 * dice2_1
        - (1.0 / 11.0),
        dice1_1 * dice2_6
        + dice1_2 * dice2_5
        + dice1_3 * dice2_4
        + dice1_4 * dice2_3
        + dice1_5 * dice2_2
        + dice1_6 * dice2_1
        - (1.0 / 11.0),
        dice1_2 * dice2_6
        + dice1_3 * dice2_5
        + dice1_4 * dice2_4
        + dice1_5 * dice2_3
        + dice1_6 * dice2_2
        - (1.0 / 11.0),
        dice1_3 * dice2_6
        + dice1_4 * dice2_5
        + dice1_5 * dice2_4
        + dice1_6 * dice2_3
        - (1.0 / 11.0),
        dice1_4 * dice2_6
        + dice1_5 * dice2_5
        + dice1_6 * dice2_4
        - (1.0 / 11.0),
        dice1_5 * dice2_6 + dice1_6 * dice2_5 - (1.0 / 11.0),
        dice1_6 * dice2_6 - (1.0 / 11.0),
    ],
    [
        dice1_1,
        dice1_2,
        dice1_3,
        dice1_4,
        dice1_5,
        dice1_6,
        dice2_1,
        dice2_2,
        dice2_3,
        dice2_4,
        dice2_5,
        dice2_6,
    ],
)

print(solution)
