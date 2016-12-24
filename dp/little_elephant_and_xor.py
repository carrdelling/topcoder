"""

Problem name: LittleElephantAndXor
Class: SRM 595, Division II, Level Three

Description: https://community.topcoder.com/stat?c=problem_statement&pm=12623

"""

a, b, c = 0, 0, 0


def count_pairs(idx, bit_up_a, bit_up_b, bit_up_c, mem):
    """ Solved using DP + memoization.

        The states are each of the indexes in the binary string of the digits
        * the states of three binary flags.

        The idea is to move forward over the tree of possible binary strings
        based on if the current branch is always lower than the threshold

        The branch will be always lower of the previous binary digit was a '0'
        The branch will be lower if the current binary digit is equal or lower
        to the threshold binary digit at this level

        A pair of numbers will be valid if:

        1) current(a) < threshold(A)
        2) current(b) < threshold(B)
        3) current(a XOR b) < threshold(C)

        If the 1st condition is removed, the effect would be to accept all pairs
        where a is equal or lower than 2 ** (#binary digits of A).

        Same for the second condition (B)

        If the 3rd condition is removed, then the effect would be to acceot all
        pairs for which a <= A and b <= B, regardless of their XOR value
    """

    global a
    global b
    global c

    if idx == -1:
        return 1

    if (idx, bit_up_a, bit_up_b, bit_up_c) in mem:
        return mem[(idx, bit_up_a, bit_up_b, bit_up_c)]

    count = 0
    mask = 1 << idx

    for i, j in [(0, 0), (0, 1), (1, 0), (1, 1)]:

        k = i ^ j

        if bit_up_a:
            if not (a & mask) and i == 1:
                continue
            elif (a & mask) and i == 0:
                next_a = 0
            else:
                next_a = 1
        else:
            next_a = 0

        if bit_up_b:
            if not (b & mask) and j == 1:
                continue
            elif (b & mask) and j == 0:
                next_b = 0
            else:
                next_b = 1
        else:
            next_b = 0

        if bit_up_c:
            if not (c & mask) and k == 1:
                continue
            elif (c & mask) and k == 0:
                next_c = 0
            else:
                next_c = 1
        else:
            next_c = 0

        count += count_pairs(idx - 1, next_a, next_b, next_c, mem)

    mem[(idx, bit_up_a, bit_up_b, bit_up_c)] = count
    return count


def solve(args):
    """ Solve the problem, using memoization """

    global a
    global b
    global c

    a, b, c = args
    mem = {}

    # a tree of 30 levels should be enough (all values are < 2^30)
    sol = count_pairs(30, 1, 1, 1, mem)

    return sol


if __name__ == "__main__":

    test_cases = [((2, 2, 1), 5),
                  ((4, 7, 3), 20),
                  ((10, 10, 5), 57),
                  ((774, 477, 447), 214144),
                  ((1000000000, 1000000000, 500000000), 468566946385621507),
                  ]

    for index, case in enumerate(test_cases):
        output = solve(case[0])
        assert output == case[1], 'Case {} failed: {} != {}'.format(
            index, output, case[1])
    else:
        print('All tests OK')
