"""

Problem name: Flower Garden
Class: TCCC '04 Round 1, Division I Level Two

Description: https://community.topcoder.com/stat?c=problem_statement&pm=1918

"""


def clash(flower1, flower2):
    """ Test if two flowers will class at any point of their life [bloom, wilt]

        (A classic test for interval interception, with start: x[1] and end x[2)
    """

    return flower1[1] <= flower2[2] and flower2[1] <= flower1[2]


def solve(args):
    """ Sort the flowers by increasing height. Then add then to the garden from
        the back, moving forward as far as possible without clashing with
        another flower already planted.

        Nb, this is not a DP solution!
    """

    flowers = list(zip(*args))
    flowers.sort()

    garden = []

    for flower in flowers:

        place = len(garden)
        while place > 0:
            if clash(garden[place-1], flower):
                break
            place -= 1

        garden.insert(place, flower)

    return [f[0] for f in garden]


if __name__ == "__main__":

    test_cases = [(([5, 4, 3, 2, 1],
                    [1, 1, 1, 1, 1],
                    [365, 365, 365, 365, 365]),[1, 2, 3, 4, 5]),
                  (([5, 4, 3, 2, 1],
                    [1, 5, 10, 15, 20],
                    [4, 9, 14, 19, 24]),[5, 4, 3, 2, 1]),
                  (([5, 4, 3, 2, 1],
                    [1, 5, 10, 15, 20],
                    [5, 10, 15, 20, 25]),[1, 2, 3, 4, 5]),
                  (([5, 4, 3, 2, 1],
                    [1, 5, 10, 15, 20],
                    [5, 10, 14, 20, 25]),[3, 4, 5, 1, 2]),
                  (([1, 2, 3, 4, 5, 6],
                    [1, 3, 1, 3, 1, 3],
                    [2, 4, 2, 4, 2, 4]), [2, 4, 6, 1, 3, 5]),
                  (([3, 2, 5, 4],
                    [1, 2, 11, 10],
                    [4, 3, 12, 13]), [4, 5, 2, 3])
                  ]

    for index, case in enumerate(test_cases):
        output = solve(case[0])
        assert output == case[1], 'Case {} failed: {} != {}'.format(
            index, output, case[1])
    else:
        print('All tests OK')
