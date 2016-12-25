"""

Problem name: ThePalindrome
Class: SRM 428, Division II Level One

Description: https://community.topcoder.com/stat?c=problem_statement&pm=10182

"""


def solve(args):
    """ Simply reverse the string and find a match. When the match is found,
        continue it to the end. If the end is reached, then the matching index
        is the point at which the palindrome starts repeating.
    """

    string = args
    reverse = string[::-1]

    for c in range(len(string)):

        if string[c] == reverse[0]:

            for i in range(c+1, len(string)):
                if string[i] != reverse[i-c]:
                    break
            else:
                output = len(string) + c
                break

    return output


if __name__ == "__main__":

    test_cases = [("abab", 5),
                  ("abacaba", 7),
                  ("qwerty", 11),
                  ("abdfhdyrbdbsdfghjkllkjhgfds", 38),
                  ("nnnnoqqpnnpnnpppnopopnqnnpqqpnnnnnppnpnqnnnnnp", 91)
                  ]

    for index, case in enumerate(test_cases):
        output = solve(case[0])
        assert output == case[1], 'Case {} failed: {} != {}'.format(
            index, output, case[1])
    else:
        print('All tests OK')
