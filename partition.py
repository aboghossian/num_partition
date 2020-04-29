from random import choice, randint, uniform, sample, seed
from math import floor, exp, inf
import sys


def read_file(filename):
    a = []
    with open(filename) as f:
        for line in f:
            a.append(int(line.strip()))
    return a


class MaxHeap():

    def __init__(self, heap=[]):
        self.size = len(heap)
        self.heap = [0] + heap
        self.root = 1
        if self.size > 1:
            self.build_heap()

    def get_parent(self, index):
        return index//2

    def get_right(self, index):
        return (2*index) + 1

    def get_left(self, index):
        return 2*index

    def swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def max_heapify(self, index):
        l = self.get_left(index)
        r = self.get_right(index)
        if l <= self.size and self.heap[l] > self.heap[index]:
            largest = l
        else:
            largest = index
        if r <= self.size and self.heap[r] > self.heap[largest]:
            largest = r
        if largest != index:
            self.swap(index, largest)
            self.max_heapify(largest)

    def build_heap(self):
        for i in range(self.size//2, 0, -1):
            self.max_heapify(i)

    def extract_max(self):
        max = self.heap[self.root]
        self.heap[self.root] = self.heap.pop(self.size)
        self.size -= 1
        self.max_heapify(self.root)
        return max

    def insert(self, v):
        self.size += 1
        self.heap.append(v)
        n = self.size
        while (n != self.root) and (self.heap[self.get_parent(n)] < self.heap[n]):
            self.swap(self.get_parent(n), n)
            n = self.get_parent(n)


def repeated_random(nums, max_iter):
    r = range(len(nums))
    s = [choice([-1, 1]) for x in r]
    res = abs(sum(x * y for x, y in zip(s, nums)))

    for i in range(max_iter):
        s_prime = [choice([-1, 1]) for x in r]
        res_prime = abs(sum(x * y for x, y in zip(s_prime, nums)))
        if res_prime <= res:
            s = s_prime
            res = res_prime
            if res == 0:
                return res
    return res


def hill_climbing(nums, max_iter):
    r = range(len(nums))
    s = [choice([-1, 1]) for x in r]
    res = abs(sum(x * y for x, y in zip(s, nums)))

    for i in range(max_iter):
        a, b = sample(r, 2)
        s_prime = s
        if uniform(0, 1) < 0.5:
            s_prime[a] = -s_prime[a]
        else :
            s_prime[a] = -s_prime[a]
            s_prime[b] = -s_prime[b]
        res_prime = abs(sum(x * y for x, y in zip(s_prime, nums)))
        if res_prime < res:
            s = s_prime
            res = res_prime
            if res == 0:
                return res
    return res


def simulated_annealing(nums, max_iter):
    r = range(len(nums))
    s = [choice([-1, 1]) for x in r]
    res = abs(sum(x * y for x, y in zip(s, nums)))
    s_best = s
    res_best = res

    for i in range(max_iter):
        a,b = sample(r, 2)
        s_prime = s
        if uniform(0, 1) < 0.5:
            s_prime[a] = -s_prime[a]
        else :
            s_prime[a] = -s_prime[a]
            s_prime[b] = -s_prime[b]
        res_prime = abs(sum(x * y for x, y in zip(s_prime, nums)))
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
            if res_best == 0:
                return res_best
    return res_best


def prepart_random(nums, max_iter):
    n = len(nums)
    p = [randint(0, n-1) for x in range(n)]
    a = [0] * n
    for i in range(n):
        a[p[i]] += nums[i]
    res = karmarkar(a)
    for i in range(max_iter):
        p = [randint(0, n-1) for x in range(n)]
        a = [0] * n
        for j in range(n):
            a[p[j]] += nums[j]
        res_prime = karmarkar(a)
        if res_prime < res:
            res = res_prime
            if res == 0:
                return res
    return res


def prepart_hill(nums, max_iter):
    n = len(nums)
    p = [randint(0, n-1) for x in range(n)]
    a = [0] * n
    for j in range(n):
        a[p[j]] += nums[j]
    res =  karmarkar(a)
    for i in range(max_iter):
        r1, r2 = randint(0, n-1), randint(0, n-1)
        while r2 == p[r1]:
            r2 = randint(0, n-1)
        a_prime, p_prime = a, p
        a_prime[p[r1]] -= nums[r1]
        p_prime[r1] = r2
        a_prime[p_prime[r1]] += nums[r1]
        res_prime = karmarkar(a_prime)
        if res_prime < res:
            res = res_prime
            a = a_prime
            p = p_prime
            if res == 0:
                return res
    return res


def prepart_annealing(nums, max_iter):
    n = len(nums)
    p = [randint(0, n-1) for x in range(n)]
    a = [0] * n
    for j in range(n):
        a[p[j]] += nums[j]
    res =  karmarkar(a)
    res_best = res
    for i in range(max_iter):
        r1, r2 = randint(0, n-1), randint(0, n-1)
        while r2 == p[r1]:
            r2 = randint(0, n-1)
        a_prime, p_prime = a, p
        a_prime[p[r1]] -= nums[r1]
        p_prime[r1] = r2
        a_prime[p_prime[r1]] += nums[r1]
        res_prime = karmarkar(a_prime)
        if res_prime < res:
            res = res_prime
            a = a_prime
            p = p_prime
            if res == 0:
                return res
        else:
            t_iter = 10**10 * (0.8 ** floor(i/300))
            prob = exp(-(res_prime - res)/t_iter)
            if uniform(0, 1) <= prob:
                res = res_prime
                p = p_prime
                a = a_prime
        if res < res_best:
            res_best = res
    return res


def karmarkar(nums):
    num_heap = MaxHeap(nums)
    large1 = num_heap.extract_max()
    large2 = num_heap.extract_max()
    while large2 != 0:
        num_heap.insert(large1 - large2)
        num_heap.insert(0)
        large1 = num_heap.extract_max()
        large2 = num_heap.extract_max()
    return large1


if __name__ == "__main__":
    flag = int(sys.argv[1])
    alg = int(sys.argv[2])
    if flag == 0:
        filename = sys.argv[3]
        numbers = read_file(filename)
    else:
        numbers = [randint(1, 10**12) for z in range(100)]

    if alg == 0:
        print(karmarkar(numbers))
    elif alg == 1:
        print(repeated_random(numbers, 25000))
    elif alg == 2:
        print(hill_climbing(numbers, 25000))
    elif alg == 3:
        print(simulated_annealing(numbers, 25000))
    elif alg == 11:
        print(prepart_random(numbers, 25000))
    elif alg == 12:
        print(prepart_hill(numbers, 25000))
    elif alg == 13:
        print(prepart_annealing(numbers, 25000))
    else:
        print("No algorithm chosen, please try again")
