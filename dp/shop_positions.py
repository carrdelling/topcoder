"""

Problem name: ShopPositions
Class: SRM 667, Division II, Level Three

Description: https://community.topcoder.com/stat?c=problem_statement&pm=13884

"""

n, m = 0, 0
profits = []
mem = {}


def compute_profit(x, y):
    """ Compute the profit of a store given the building (x) and the number of
        stores nearby """

    y_index = x * (3*m) + y - 1
    return profits[y_index]


def get_profit(idx, left_stores):
    """ Solved with DP + memoization.

        The states are each of the buildings and the number of stores in each
        building to the left hand side.

        The base case (rightmost building) is the maximum profit for every
        possible number of stores + the stores on the previous state (0 for a
        1-building problem)

        The actual profits for all the other buildings are actually returned
        after coming back from the recursion (so this not a tail recursive
        implementation ;()
    """

    global mem

    if (idx, left_stores) in mem:
        return mem[(idx, left_stores)]

    if idx == n - 1:
        max_profit = 0
        max_stores = 0
        for i in range(1, m+1):

            all_stores = left_stores + i
            profit = i * compute_profit(idx, all_stores)

            if profit > max_profit:
                max_profit = profit
                max_stores = i

        mem[(idx, left_stores)] = max_stores, max_profit
        return max_stores, max_profit

    max_profit = -1
    max_stores = -1
    for i in range(m+1):

        right_stores, profit = get_profit(idx+1, i)
        all_stores = left_stores + i + right_stores

        if i > 0:
            profit += i * compute_profit(idx, all_stores)

        if profit > max_profit:
            max_profit = profit
            max_stores = i
    mem[(idx, left_stores)] = max_stores, max_profit
    return max_stores, max_profit


def solve(args):
    """ Solve the problem with memoization """

    global n, m
    global profits
    global mem

    mem = {}

    n, m, profits = args

    stores, profit = get_profit(0, 0)

    return profit


if __name__ == "__main__":

    test_cases = [((1, 5, [1000, 5, 4, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), 1000),
                  ((3, 1, [7, 6, 1, 10, 4, 1, 7, 6, 3]), 14),
                  ((2, 2, [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]), 24),
                  ((3, 3, [30, 28, 25, 15, 14, 10, 5, 4, 2, 50, 40, 30, 28,
                           17, 13, 8, 6, 3, 45, 26, 14, 14, 13, 13, 2, 1, 1]), 127),
                 ]

    for index, case in enumerate(test_cases):
        output = solve(case[0])
        assert output == case[1], 'Case {} failed: {} != {}'.format(
            index, output, case[1])
    else:
        print('All tests OK')
