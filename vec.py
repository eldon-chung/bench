#!/bin/python3

import subprocess
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np


sizes = [(10 ** 6) * steps for steps in range(1, 101)]

# for display stuff
limited_sizes = [ (10 ** 6) * steps for steps in range(1, 102, 10) ]
ticks = [ steps for steps in range(11) ]

timings = []
for size in sizes:
    running_time : float = 0
    for s_iter in range(10 ** 7):
        print(f"running test size {size}, iter {s_iter}                                        ", end="\r")
        res = subprocess.run(["./vec", f"{size}"], capture_output=True)
        assert res.returncode == 0
        report = float(res.stdout.decode().strip("elapsed seconds:"))
        running_time += report
    timings.append(running_time / (10 ** 7))

# print(timings)
# plt.plot(timings)
# plt.show()

# plt.plot([1, 3, 4])
# plt.show()
slope, intercept = np.polyfit(sizes, timings, 1)
abline_values = [slope * i + intercept for i in sizes]

plt.plot(sizes, timings, '--')
plt.plot(sizes, abline_values, 'b')
plt.xticks(limited_sizes, ticks)

plt.savefig('results.png')
