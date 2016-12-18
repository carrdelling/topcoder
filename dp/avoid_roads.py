"""

Problem name: AvoidRoads
Class: TCO '03 Semifinals 4, Division I Level One

Description: https://community.topcoder.com/stat?c=problem_statement&pm=1889

"""

from collections import defaultdict


def solve(args):
    """ Solved as follows:

        1) Store all road blocks in a dictionary

        2) Initialize borders of the map:

            2.1) NPaths in origin (0,0) is 1
            2.2) NPaths for the first row (x=0) is p[0][y] = p[0][y-1]; but if
                 there is a block, then p[0][y] = 0
            2.3) Same for the first column (y=0)

        3) Traverse the map in increasing order of rows and columns.
           NPaths = Paths from down + paths from left
           If there is a block in any of the two paths, then the relevant term
           becomes 0

        The solution is p[n][m]
    """

    n, m, blocks = args

    n += 1
    m += 1

    barriers = defaultdict(set)

    for b in blocks:
        coords = list(map(int, b.split()))
        start = tuple(coords[:2])
        end = tuple(coords[2:])
        barriers[start].add(end)
        barriers[end].add(start)

    paths = []

    for x in range(n):
        paths.append([0]*m)

    paths[0][0] = 1

    # first column
    for x in range(1, n):
        paths[x][0] = 0 if (x-1, 0) in barriers[(x, 0)] else paths[x-1][0]

    # first row
    for y in range(1, m):
        paths[0][y] = 0 if (0, y-1) in barriers[(0, y)] else paths[0][y-1]

    # the rest
    for x in range(1, n):
        for y in range(1, m):
            left_paths = 0 if (x, y-1) in barriers.get((x, y), set()) else paths[x][y-1]
            down_paths = 0 if (x-1, y) in barriers.get((x, y), set()) else paths[x-1][y]

            paths[x][y] = left_paths + down_paths

    return paths[n-1][m-1]


if __name__ == "__main__":

    test_cases = [([6, 6, ["0 0 0 1", "6 6 5 6"]], 252),
                  ([1, 1, []], 2),
                  ([35, 31, []], 6406484391866534976),
                  ([2, 2, ["0 0 1 0", "1 2 2 2", "1 1 2 1"]], 0)
                  ]

    for index, case in enumerate(test_cases):
        output = solve(case[0])
        assert output == case[1], 'Case {} failed: {} != {}'.format(
            index, output, case[1])
    else:
        print('All tests OK')
