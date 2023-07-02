#!/bin/python3

import subprocess
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np



starting_size = 900
step_size = 100
ending_size = starting_size + 100 * step_size

sizes = [s for s in range(starting_size, ending_size + 1, step_size)]
timings = {}

num_iter = 1
for iter in range(num_iter):
    # print(f"iter {iter} ./vec {starting_size} {ending_size} {step_size} ")
    print(f"iter: {iter}", end ="\r")
    res = subprocess.run(["./vec", str(starting_size), str(ending_size), str(step_size)], capture_output=True)
    assert res.returncode == 0
    output = res.stdout.decode()
    # print(f"output <<{output}>>")
    for line in output.split("\n"):
        if not line:
            continue
        # print(f"line: [{line}]")
        size, timing = line.split(":")
        size = int(size)
        timing = float(timing)
        print(f"iter: {iter}, size {size}, timing {timing}")
        try:
            timings[size] += timing
        except:
            assert iter == 0
            timings[size] = timing
averaged = { k : v / num_iter for k, v in timings.items() }

# print(timings)
# plt.plot(timings)
# plt.show()

# plt.plot([1, 3, 4])
# plt.show()
sizes = list(averaged.keys())
values = [v for k, v in averaged.items()]

slope, intercept = np.polyfit(sizes, values, 1)
abline_values = [slope * i + intercept for i in sizes]

coeff2, coeff1, coeff0 = np.polyfit(sizes, values, 2)
cdline_values = [ coeff2 * (i ** 2) + coeff1 * i + intercept for i in sizes]


# xtick = [_ for _ in range(starting_size, ending_size + 1, (ending_size - starting_size) // 10)]
# xtick = [_ for _ in range(starting_size, ending_size + 1, (ending_size - starting_size) // 10)]
# print(averaged)
plt.plot(sizes, values, '.')
# plt.plot(sizes, abline_values, '--')
plt.plot(sizes, cdline_values, '--')
print(f"regessed to: {coeff2} n^2 + {coeff1} n + {coeff0}")
# plt.xticks(xtick)

plt.savefig('results.png')
