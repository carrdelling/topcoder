"""

Problem name: BadNeighbors
Class: TCCC '04 Round 4, Division I Level One

Description: https://community.topcoder.com/stat?c=problem_statement&pm=2402

"""


def get_donations(values):
    """ Acumulate the best possible donation sum at any point in the array.

        This is simply max(best(i-3), best(i-2)) + donation(i)

        with best(0) = values[0]
             best(1) = values[1]
             best(2) = values[0] + values[2]
    """

    best_values = {0: values[0], 1: values[1], 2: values[0] + values[2]}

    for idx in range(3, len(values)):

        current = values[idx] + max(best_values[idx - 3], best_values[idx - 2])

        best_values[idx] = current

    return best_values[len(values) - 1]


def solve(array):
    """ Return max value if problem length is 3 or less (trivial)

        Else, solve the problem twice, once for the whole array except the last
        element; and once for the whole array except the first element. Then,
        return the maximum of both solutions.

        (this is due to the fact that the first and the last elements are
        considered neighbors)
    """

    if len(array) > 3:
        return max(get_donations(array[1:]), get_donations(array[:-1]))
    else:
        return max(array)


if __name__ == "__main__":

    test_cases = [([10, 3, 2, 5, 7, 8], 19),
                  ([11, 15], 15),
                  ([7, 7, 7, 7, 7, 7, 7], 21),
                  ([1, 2, 3, 4, 5, 1, 2, 3, 4, 5], 16),
                  ([94, 40, 49, 65, 21, 21, 106, 80, 92, 81, 679, 4, 61, 6, 237,
                    12, 72, 74, 29, 95, 265, 35, 47, 1, 61, 397, 52, 72, 37, 51,
                    1, 81, 45, 435, 7, 36, 57, 86, 81, 72], 2926)
                  ]

    for index, case in enumerate(test_cases):
        output = solve(case[0])
        assert output == case[1], 'Case {} failed: {} != {}'.format(
            index, output, case[1])
    else:
        print('All tests OK')
