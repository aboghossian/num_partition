from random import choice, randint, uniform


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
        if uniform(0, 1) < 0.5:
            s_prime[a] = -s_prime[a]
            s_prime[b] = -s_prime[b]
        else :
            s_prime[a] = -s_prime[a]
        res_prime = sum(x * y for x, y in zip(s_prime, nums))
        if res_prime < res:
            s = s_prime
            res = res_prime
    return res


def simulated_annealing(nums, max_iter):
    return
