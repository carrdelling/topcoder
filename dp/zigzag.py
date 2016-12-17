"""

Problem name: ZigZag
Class: TCCC '03 Semifinals 3, Division I Level One

Description: https://community.topcoder.com/stat?c=problem_statement&pm=1259

"""


def longest_zigzag(array):
    """ For each new element in the array, check all previous states

        For each previous state, check whether the new is lower or higher than
        the value at the state. For the correct case (ties are discarded), just
        take its best length (+1) and compare it with the current best lenght.
        If it is higher, update it.

        When all previous states have been checked, create a new state for the
        current value, with two configurations: Ascending and descending (1,0)
    """

    memory = {(0, 1): 1, (0, 0): 1}
    max_length = 1

    for idx in range(1, len(array)):
        memory[(idx, 0)] = 1
        memory[(idx, 1)] = 1
        for _idx in range(0, idx):

            if array[idx] < array[_idx]:
                memory[(idx, 0)] = max(memory[(idx, 0)], memory[(_idx, 1)] + 1)
            elif array[idx] > array[_idx]:
                memory[(idx, 1)] = max(memory[(idx, 1)], memory[(_idx, 0)] + 1)

        max_length = max(max_length, memory[(idx, 0)], memory[(idx, 1)])

    return max_length


def solve(array):
    """ For less than 3 elements, just return the lenght of the array

        Else, solve the problem
    """

    if len(array) < 3:
        return len(array)

    return longest_zigzag(array)
 
if __name__ == "__main__":

    test_cases = [([1, 7, 4, 9, 2, 5], 6),
                  ([1, 17, 5, 10, 13, 15, 10, 5, 16, 8], 7),
                  ([44], 1),
                  ([1, 2, 3, 4, 5, 6, 7, 8, 9], 2),
                  ([70, 55, 13, 2, 99, 2, 80, 80, 80, 80, 100, 19, 7, 5, 5, 5,
                    1000, 32, 32], 8),
                  ([374, 40, 854, 203, 203, 156, 362, 279, 812, 955, 600, 947,
                    978, 46, 100, 953, 670, 862, 568, 188, 67, 669, 810, 704,
                    52, 861, 49, 640, 370, 908, 477, 245, 413, 109, 659, 401,
                    483, 308, 609, 120, 249, 22, 176, 279, 23, 22, 617, 462,
                    459, 244], 36)

                  ]

    for index, case in enumerate(test_cases):
        output = solve(case[0])
        assert output == case[1], 'Case {} failed: {} != {}'.format(
            index, output, case[1])
    else:
        print('All tests OK')
