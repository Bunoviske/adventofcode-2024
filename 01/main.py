import sys
sys.path.append('..')

import numpy as np
from utils.load_input import load_input

df = load_input("example.csv")
df = load_input("input.csv")

list1 = df[0].values.tolist()
list2 = df[1].values.tolist()

list1.sort()
list2.sort()

### part 1

arr1 = np.array(list1, dtype='int32')
arr2 = np.array(list2, dtype='int32')

result = np.sum(np.absolute(arr1 - arr2))
print(result)

### part 2

unique, counts = np.unique(arr1, return_counts=True)
arr1_counts = dict(zip(unique, counts))

unique, counts = np.unique(arr2, return_counts=True)
arr2_counts = dict(zip(unique, counts))

score = 0
for number, counts in arr1_counts.items():
     score += number * counts * (arr2_counts[number] if number in arr2_counts else 0)
    
print(score)