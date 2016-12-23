"""

Problem name: ColorfulRoad
Class: SRM 596, Division II Level Two

Description: https://community.topcoder.com/stat?c=problem_statement&pm=12837

"""


def solve(args):
    """ The problem is solved by keeping track of the minimum cost to jump to
        each road point, from all points visited so far.

        When all points in 1, N-1 have been visited, cost[N] will be minimal
    """

    road = args

    costs = [-1] * len(road)
    costs[0] = 0

    next_part = {'R': 'G', 'G': 'B', 'B': 'R'}

    for idx in range(len(road)):
        current_cost = costs[idx]

        if current_cost == -1:
            continue

        next_color = next_part[road[idx]]

        for idx_2 in range(idx + 1, len(road)):
            if road[idx_2] != next_color:
                continue
            energy = current_cost + ((idx_2 - idx) ** 2)
            value = min(costs[idx_2], energy) if costs[idx_2] > -1 else energy
            costs[idx_2] = value

    return costs[len(road)-1]


if __name__ == "__main__":

    test_cases = [('RGGGB', 8),
                  ('RGBRGBRGB', 8),
                  ('RBBGGGRR', -1),
                  ('RBRRBGGGBBBBR', 50),
                  ('RG', 1),
                  ('RBRGBGBGGBGRGGG', 52)
                  ]

    for index, case in enumerate(test_cases):
        output = solve(case[0])
        assert output == case[1], 'Case {} failed: {} != {}'.format(
            index, output, case[1])
    else:
        print('All tests OK')
