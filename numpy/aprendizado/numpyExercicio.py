import numpy as np

url = 'https://raw.githubusercontent.com/allanspadini/numpy/dados/bytebank.csv'

data = np.loadtxt(url,skiprows=1,delimiter=',')

print(data.ndim)
print('-'*30)
# print(data.T)
print(np.shape(data))