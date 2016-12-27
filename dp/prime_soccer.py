"""

Problem name: PrimeSoccer
Class: SRM 422, Division I Level One

Description: https://community.topcoder.com/stat?c=problem_statement&pm=10240

"""


import math
import numpy as np


def is_prime(a):
    """ Check (in O(N)) whether a is prime or not """

    if a < 2:
        return False

    for i in range(2, int(math.sqrt(a)) +1):
        if a % i == 0:
            return False

    return True


def get_distribution(skill, rounds, dist):
    """ Computes the full distribution of possible scores given a number of
        rounds left and a skill value for the team
    """

    if rounds == 0:
        return dist

    dist[19-rounds] = dist[18-rounds] * skill

    for score in sorted(dist, reverse=True)[1:-1]:
        prob = (dist[score] * (1.0 - skill)) + (dist[score-1] * skill)
        dist[score] = prob

    dist[0] *= (1.0 - skill)

    return get_distribution(skill, rounds - 1, dist)


def prime_score(skill):
    """ Compute the probability that a team reaches a prime result given its
        skill score
    """

    dist = {0: 1.0 - skill, 1: skill}
    dist = get_distribution(skill, 17, dist)

    prime = 0.0
    composite = 0.0

    for score in dist:
        if is_prime(score):
            prime += dist[score]
        else:
            composite += dist[score]

    return prime / (prime + composite)


def solve(args):
    """ Compute the prime probability for each team skill, and aggregate them
    """

    team_a, team_b = args

    prime_a = prime_score(team_a / 100)
    prime_b = prime_score(team_b / 100)

    return prime_a + ((1.0 - prime_a) * prime_b)

if __name__ == "__main__":

    test_cases = [((50, 50), 0.5265618908306351),
                  ((100, 100), 0.0),
                  ((12, 89), 0.6772047168840167)
                  ]

    for index, case in enumerate(test_cases):
        output = solve(case[0])
        assert np.isclose(output, case[1]), 'Case {} failed: {} != {}'.format(
            index, output, case[1])
    else:
        print('All tests OK')
