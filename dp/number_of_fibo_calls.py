"""

Problem name: NumberofFiboCalls
Class: SRM 352, Division Level One

Description: https://community.topcoder.com/stat?c=problem_statement&pm=10240

"""


def solve(args):
    """ This problem can be solved in O(N) just by accumulating the number of
        prints for each previous element in the sequence.
    """

    n = args

    calls = {0: [1, 0],
             1: [0, 1]}

    for i in range(2, n + 1):

        calls[i] = [sum(x) for x in zip(calls[i - 2], calls[i - 1])]

    return calls[n]


if __name__ == "__main__":

    test_cases = [(0, [1, 0]),
                  (3, [1, 2]),
                  (6, [5, 8]),
                  (22, [10946, 17711])
                  ]

    for index, case in enumerate(test_cases):
        output = solve(case[0])
        assert output == case[1], 'Case {} failed: {} != {}'.format(
            index, output, case[1])
    else:
        print('All tests OK')
