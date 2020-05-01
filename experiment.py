from partition import *
from datetime import datetime

test_lists = [[randint(1, 10**12) for z in range(100)] for y in range(100)]

out_file = open("results.csv", "w")
for numbers in test_lists:
    for alg in ["karmarkar", "random", "hill", "anneal", "pre_rand", "pre_hill", "pre_anneal"]:
        if alg == "karmarkar":
            start = datetime.now()
            res = karmarkar(numbers)
            time = datetime.now() - start
        elif alg == "random":
            start = datetime.now()
            res = repeated_random(numbers, 25000)
            time = datetime.now() - start
        elif alg == "hill":
            start = datetime.now()
            res = hill_climbing(numbers, 25000)
            time = datetime.now() - start
        elif alg == "anneal":
            start = datetime.now()
            res = simulated_annealing(numbers, 25000)
            time = datetime.now() - start
        elif alg == "pre_rand":
            start = datetime.now()
            res = prepart_random(numbers, 25000)
            time = datetime.now() - start
        elif alg == "pre_hill":
            start = datetime.now()
            res = prepart_hill(numbers, 25000)
            time = datetime.now() - start
        elif alg == "pre_anneal":
            start = datetime.now()
            res = prepart_annealing(numbers, 25000)
            time = datetime.now() - start
        else:
            print("OOOOPS!!!!")
            break
        line = "{},{},{}\n".format(alg, time, res)
        print(line)
        out_file.write(line)
out_file.close()
