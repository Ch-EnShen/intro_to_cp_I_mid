import numpy as np
from functools import reduce
from operator import mul

#assign start and end points for each variable
ranges = ((0, 5), (0, 3), (0, 6))   #three variables, start 0 0 0, end 4 2 5
operations = reduce(mul, (p[1] - p[0] for p in ranges)) - 1 #operation times
result = [i[0] for i in ranges] #start array
pos = len(ranges) - 1   #start from the last index
increments = 0
print(result)

while increments < operations:
    if result[pos] == ranges[pos][1] - 1:
        result[pos] = ranges[pos][0]
        pos -= 1
    else:
        result[pos] += 1
        increments += 1
        pos = len(ranges) - 1 #increment the innermost loop
        print(result)