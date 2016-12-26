"""

Problem name: RepeatString
Class: SRM 698, Division I Level One

Description: https://community.topcoder.com/stat?c=problem_statement&pm=14391

"""

mem = {}


def edit_distance(a, b):
    """ Edit distance between a and b """

    if not a:
        return len(b)
    if not b:
        return len(a)

    if (a, b) in mem:
        return mem[(a, b)]

    if a[0] == b[0]:
        result = edit_distance(a[1:], b[1:])
        mem[(a, b)] = result

        return result

    if a[-1] == b[-1]:
        result = edit_distance(a[:-1], b[:-1])
        mem[(a, b)] = result

        return result

    remove = edit_distance(a[1:], b)
    replace = edit_distance(a[1:], b[1:])
    add = edit_distance(a, b[1:])

    result = 1 + min(remove, replace, add)

    mem[(a, b)] = result

    return result


def solve(args):
    """ The problem can be solved just by computing the minimum edit distance
        between all possible two-word splits of the word.
    """

    word = args

    if len(word) < 2:
        return len(word)

    distances = [edit_distance(word[:i], word[i:]) for i in range(1, len(word))]
    return min(distances)

if __name__ == "__main__":

    test_cases = [
                    ("aba", 1),
                    ("adam", 1),
                    ("x", 1),
                    ("aaabbbaaaccc", 3),
                    ("repeatstring", 6),
                    ("aaaaaaaaaaaaaaaaaaaa", 0)
                  ]

    for index, case in enumerate(test_cases):
        output = solve(case[0])
        assert output == case[1], 'Case {} failed: {} != {}'.format(
            index, output, case[1])
    else:
        print('All tests OK')
