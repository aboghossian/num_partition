from random import choice, randint, uniform
from math import floor, exp


def repeated_random(nums, max_iter):
    s = [choice([-1, 1]) for x in range len(nums)]
    res = sum(x * y for x, y in zip(s, nums))
    for i in range(max_iter):
        s_prime = [choice([-1, 1]) for x in range len(nums)]
        res_prime = sum(x * y for x, y in zip(s_prime, nums))
        if res_prime <= res:
            s = s_prime
            res = res_prime
    return res


def hill_climbing(nums, max_iter):
    s = [choice([-1, 1]) for x in range len(nums)]
    res = sum(x * y for x, y in zip(s, nums))
    for i in range(max_iter):
        a,b = (randint(0, len(s)), randint(0, len(s)))
        s_prime = s
        if a == b or uniform(0, 1) < 0.5:
            s_prime[a] = -s_prime[a]
        else :
            s_prime[a] = -s_prime[a]
            s_prime[b] = -s_prime[b]
        res_prime = sum(x * y for x, y in zip(s_prime, nums))
        if res_prime < res:
            s = s_prime
            res = res_prime
    return res


def simulated_annealing(nums, max_iter):
    s = [choice([-1, 1]) for x in range len(nums)]
    res = sum(x * y for x, y in zip(s, nums))
    s_best = s
    res_best = res
    for i in range(max_iter):
        a,b = (randint(0, len(s)), randint(0, len(s)))
        s_prime = s
        if a == b or uniform(0, 1) < 0.5:
            s_prime[a] = -s_prime[a]
        else :
            s_prime[a] = -s_prime[a]
            s_prime[b] = -s_prime[b]
        res_prime = sum(x * y for x, y in zip(s_prime, nums))
        if res_prime < res:
            s = s_prime
            res = res_prime
        else:
            t_iter = 10**10 * (0.8 ** floor(i/300))
            prob = exp(-(res_prime - res)/t_iter)
            if uniform(0, 1) <= prob:
                s = s_prime
                res = res_prime
        if res < res_best:
            s_best = s
            res_best = res
    return res_best
