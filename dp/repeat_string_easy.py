"""

Problem name: RepeatStringEasy
Class: SRM 698, Division II Level Two

Description: https://community.topcoder.com/stat?c=problem_statement&pm=14390

"""


def solve(args):
    """ Iterate over all possible ways of splitting the string in two words

        Then, for each split, compute the maximum common substring.

        Output is the overall maximum found * 2, since the problem is asking
        for the longest square.
    """

    string = args
    best = 0

    for k in range(1, len(string)):

        first = string[:k]
        second = string[k:]

        if len(second) <= best:
            break

        mem = {}
        maximum = 0
        if len(first) > len(second):
            second, first = first, second

        for i in range(len(first)):
            for j in range(len(second)):
                if first[i] == second[j]:
                    value = mem.get((i-1, j-1), 0) + 1
                else:
                    value = max(mem.get((i-1, j), 0), mem.get((i, j-1), 0))
                mem[(i, j)] = value
                maximum = max(maximum, value)

        best = max(best, maximum)

    return 2 * best

if __name__ == "__main__":

    test_cases = [("frankfurt", 4),
                  ("single", 0),
                  ("singing", 6),
                  ("aababbababbabbbbabbabb", 18),
                  ("x", 0)
                  ]

    for index, case in enumerate(test_cases):
        output = solve(case[0])
        assert output == case[1], 'Case {} failed: {} != {}'.format(
            index, output, case[1])
    else:
        print('All tests OK')
