"""

Problem name: MutaliskEasy
Class: SRM 658, Division II Level Two

Description: https://community.topcoder.com/stat?c=problem_statement&pm=13782

"""
import itertools

possibilities = list(itertools.permutations([0, 1, 2]))
mem = {}


def attack(mutas):
    """ All inputs are assumed to be lists of 3 elements, sorted in decreasing
        value.

        The base case is a <= 9, b <= 3, c <= 1, that is, a single attack would
        kill all targets.

        The rest is solved just by checking all possible permutations and
        taking the minimum solution.
    """

    mutas = sorted(mutas, reverse=True)
    key = ''.join(map(str, mutas))

    if key in mem:
        return mem[key]

    if mutas[0] <= 9 and mutas[1] <= 3 and mutas[2] <= 1:
        return 1

    min_cost = 10e6
    for op in possibilities:

        new_mutas = [mutas[op[0]] - 9, mutas[op[1]] - 3, mutas[op[2]] - 1]

        cost = attack(new_mutas)
        min_cost = min(cost, min_cost)

    total_cost = 1 + min_cost
    mem[key] = total_cost

    return total_cost


def solve(args):
    """ Solved using DP + memoization """

    mutas = list(args)
    mem.clear()

    while len(mutas) < 3:
        mutas.append(0)

    return attack(mutas)


if __name__ == "__main__":

    test_cases = [((12, 10, 4), 2),
                  ((54, 18, 6), 6),
                  ((55, 60, 53), 13),
                  ((1, 1, 1), 1),
                  ((60, 40), 9),
                  (tuple([60]), 7)
                  ]

    for index, case in enumerate(test_cases):
        output = solve(case[0])
        assert output == case[1], 'Case {} failed: {} != {}'.format(
            index, output, case[1])
    else:
        print('All tests OK')
