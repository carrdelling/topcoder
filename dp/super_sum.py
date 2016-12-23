"""

Problem name: ShorterSuperSum
Class: SRM 467, Division II Level One

Description: https://community.topcoder.com/stat?c=problem_statement&pm=10240

"""


mem = {}


def solve(args):
    """ Solved by using simple memoization """

    k, n = args

    return supersum(k, n)


def supersum(k, n):
    """ Actual supersum function """

    if k == 0:
        return n

    if (k, n) not in mem:
        mem[(k, n)] = sum([supersum(k - 1, nn) for nn in range(1, n + 1)])

    return mem[(k, n)]


if __name__ == "__main__":

    test_cases = [((1, 3), 6),
                  ((2, 3), 10),
                  ((4, 10), 2002),
                  ((10, 10), 167960)
                  ]

    for index, case in enumerate(test_cases):
        output = solve(case[0])
        assert output == case[1], 'Case {} failed: {} != {}'.format(
            index, output, case[1])
    else:
        print('All tests OK')
