"""

Problem name: ChessMetric
Class: TCCC '03 Round 4, Division I Level One

Description: https://community.topcoder.com/stat?c=problem_statement&pm=1592

"""
from collections import defaultdict

"""
The (global) board is represented as a default dict where the keys are the x,y
coordinates of each position (this helps avoiding to check for board boundaries)

Each board square is a tuple (list) of two values: current #posibilities and
#posibilities after current move
"""
board = defaultdict(lambda: [0, 0])
n = 0


def movement(start_x, start_y, pos):
    """ Apply a movement to the board - sum pos posibilities after the move """

    # movement - king
    board[(start_x-1, start_y-1)][1] += pos
    board[(start_x-1, start_y)][1] += pos
    board[(start_x-1, start_y+1)][1] += pos

    board[(start_x, start_y-1)][1] += pos
    board[(start_x, start_y+1)][1] += pos

    board[(start_x+1, start_y-1)][1] += pos
    board[(start_x+1, start_y)][1] += pos
    board[(start_x+1, start_y+1)][1] += pos

    # movement - knight
    board[(start_x-1, start_y-2)][1] += pos
    board[(start_x+1, start_y-2)][1] += pos
    board[(start_x-1, start_y+2)][1] += pos
    board[(start_x+1, start_y+2)][1] += pos

    board[(start_x-2, start_y-1)][1] += pos
    board[(start_x+2, start_y-1)][1] += pos
    board[(start_x-2, start_y+1)][1] += pos
    board[(start_x+2, start_y+1)][1] += pos


def consolidate():
    """ Update current state of the board """

    for x in range(n):
        for y in range(n):
            board[(x, y)] = [board[(x, y)][1], board[(x, y)][1]]


def solve(args):
    """ Initialization includes setting up the board after the first movement

        Then, for each movement, all possibilities are propagated from each
        board square. After that, the board is consolidated.
    """

    global board
    global n
    board = defaultdict(lambda: [0, 0])

    n, start, end, moves = args
    s_x, s_y = start

    # first movement
    movement(s_x, s_y, 1)
    consolidate()
    moves -= 1

    # rest
    while moves > 0:

        for x in range(n):
            for y in range(n):
                movement(x, y, board[(x, y)][0])

        consolidate()

        moves -= 1

    return board[end][0]

if __name__ == "__main__":

    test_cases = [((3,(0,0),(1,0),1), 1),
                  ((3,(0,0),(1,2),1), 1),
                  ((3,(0,0),(2,2),1), 0),
                  ((3,(0,0),(0,0),2), 5),
                  ((100,(0,0),(0,99),50), 243097320072600)
                  ]

    for index, case in enumerate(test_cases):
        output = solve(case[0])
        assert output == case[1], 'Case {} failed: {} != {}'.format(
            index, output, case[1])
    else:
        print('All tests OK')
