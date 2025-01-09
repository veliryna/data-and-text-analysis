import numpy as np
import pandas as pd

'''Array examples'''
arr1 = np.array([[1, 2, 3], [3, 2, 1], [4, 5, 4]])
arr2 = np.array([1+8j, 2-1j], dtype=complex)
arr3 = np.arange(0, 19, 3)
arr4 = np.ones(6, dtype=float)
arr5 = np.zeros((3,3), dtype=int)
arr6 = np.linspace(1, 2, 5)
arr7 = np.random.random((2, 3))
arr8 = np.random.randint(54, 86, (4, 2))
arr9 = np.empty(6)
print("Array 1: \n", arr1)
print("Array 2: ", arr2)
print("Array 3: ", arr3)
print("Array 4: ", arr4)
print("Array 5: \n", arr5)
print("Array 6: ", arr6)
print("Array 7: \n", arr7)
print("Array 8: \n", arr8)
print("Array 9: \n", arr9)

'''Indexes and subarray'''
print()
print("Second element of array 3: ", arr3[1])
print("Second last element of array 3: ", arr3[-2])
print("Middle element of 3x3 array 1: ", arr1[1, 1])
print("1-d subarray from array 6: ", arr6[1:4:1])
print("2-d subarray from array 8: \n", arr8[:2, :2])

'''Arithmetic'''
print()
sum = np.array([12, 11, 10])+np.array([1, 2, 3])
print("Adding arrays: ", sum)
subtract = np.array([23.7, -5.06])-np.array([0.08, 6.35])
print("Subtracting arrays: ", subtract)
mult = subtract*3
print("Multiplication: ", mult)
div = subtract/4
print("Division: ", div)
mod = np.mod(sum, 5)
print("Module division: ", mod)
power = np.power(mod, 4)
print("Array to power: ", power)
neg = np.negative(div)
print("Change sign method: ", neg)

а = np.arange(2, 5)
print("Reduce method (by power) for [2,3,4]: ", np.power.reduce(а))
b = np.arange(0, 7)
print("Accumulate method (by adding) for [0,1,2,3,4,5,6]: ", np.add.accumulate(b))
c = np.arange(-4, 6, 2)
d = np.arange(3, 9)
print("Outer method: \n", np.outer(c,d, out=None))


'''Petal width stats'''
data = pd.read_csv('iris.csv')
petal = np.array(data['petal_width'])
print()
print("Min value: ", np.min(petal))
print("Max value: ", np.max(petal))
print("Average value: ", np.mean(petal))
print("Variance: ", np.var(petal))
print("Standart error: ", np.std(petal))
print("Median: ", np.median(petal))
print("25-percentile: ", np.percentile(petal,25))
print("75-percentile: ", np.percentile(petal,75))

