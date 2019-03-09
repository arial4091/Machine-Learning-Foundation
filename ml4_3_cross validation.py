# from pycoin.ecdsa import generator_secp256k1 as g

# fid = open("fintech_hw", "a")
# x, y = (4*g).pair()
# fid.write('4:\n')
# fid.write(str(hex(x)) + ' , ' + str(hex(y)) + '\n')

# x, y = (5*g).pair()
# fid.write('5:\n')
# fid.write(str(hex(x)) + ' , ' + str(hex(y)) + '\n')
import numpy as np
import random
from numpy. linalg import inv


# training data ---------------------
fp = open('hw4_train.dat', 'r')
lines = fp.readlines()
X = []
Y = []

for i in range(len(lines)):
	tmp = lines[i].strip().split(' ')
	for j in range(len(tmp)):
		tmp[j] = float(tmp[j])
	Y.append(tmp[-1])
	del tmp[-1]
	tmp.append(1.0)
	X.append(tmp.copy())
X = np.array(X)
Y = np.array(Y)

# testing data ----------------------
fp2 = open('hw4_test.dat', 'r')
lines = fp2.readlines()
sdata = []
sy = []
for i in range(len(lines)):
	tmp = lines[i].strip().split(' ')
	for j in range(len(tmp)):
		tmp[j] = float(tmp[j])
	sy.append(tmp[-1])
	del tmp[-1]
	tmp.append(1.0)
	sdata.append(tmp.copy())
sdata = np.array(sdata)
sy = np.array(sy)

# start training ------------------------
M = len(X[0])
N = len(X)
lamda = [10**i for i in range(2, -11, -1)]
# lamda = [1]
opt_lamda = 0
opt_ein = 100
for i in range(len(lamda)):
	ein = 0
	for j in range(5):
		xt = np.vstack((X[:40*j], X[40*(j+1):]))
		yt = np.hstack((Y[:40*j], Y[40*(j+1):]))
		w = 2/N * inv(2*lamda[i]/N*np.eye(M) + 2/N*xt.T.dot(xt)).dot(xt.T).dot(yt)
		tmp = np.sum(np.sign(X[40*j:40*(j+1)].dot(w)) != Y[40*j:40*(j+1)]) / 40
		ein += tmp
	ein /= 5
	if ein < opt_ein:
		opt_ein = ein
		opt_lamda = lamda[i]

print('opt_lamda :', end = ' ')
print(opt_lamda)
print('Ev :', end = ' ')
print(opt_ein)

w = 2/N * inv(2*opt_lamda/N*np.eye(M) + 2/N*X.T.dot(X)).dot(X.T).dot(Y)
tmp = np.sum(np.sign(X.dot(w)) != Y) / len(Y)
print('Ein', end=' ')
print(tmp)
tmp = np.sum(np.sign(sdata.dot(w)) != sy) / len(sy)
print('Eout', end=' ')
print(tmp)