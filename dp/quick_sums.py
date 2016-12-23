"""

Problem name: QuickSums
Class: SRM 197, Division II Level Three

Description: https://community.topcoder.com/stat?c=problem_statement&pm=10240

"""


def quick_sum(string, target, mem):
    """ Solved with recursion + memoization

        At every point, the solution for a substring S and target T is equal to
        the solution for (S[1:], T -t), where t = int(S[0])

        Base cases:

        - int(S) == T ==> Return 0
        - len(S) == 1 ==> Return -1 (Good values are catch previously)
        - T < 0 ==> Return -1 (Left part of the string is too big)

    """

    if int(string) == target:
        return 0

    if len(string) == 1 or target < 0:
        return -1

    if (string, target) in mem:
        return mem[(string, target)]

    best_cost = -1

    for i in range(1, len(string)):

        first_value = int(string[:i])

        sub_target = target - first_value
        subcost = quick_sum(string[i:], sub_target, mem)

        if subcost == -1:
            continue

        total_cost = 1 + subcost
        best_cost = min(total_cost, best_cost) if best_cost > -1 else total_cost

    mem[(string, target)] = best_cost

    return best_cost


def solve(args):

    string, target = args
    mem = {}

    return quick_sum(string, target, mem)

if __name__ == "__main__":

    test_cases = [(('99999', 45), 4),
                  (('1110', 3), 3),
                  (('0123456789', 45), 8),
                  (('99999', 100), -1),
                  (('382834', 100), 2),
                  (('9230560001', 71), 4)
                  ]

    for index, case in enumerate(test_cases):
        output = solve(case[0])
        assert output == case[1], 'Case {} failed: {} != {}'.format(
            index, output, case[1])
    else:
        print('All tests OK')
