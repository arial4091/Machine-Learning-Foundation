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
tdata = []
ty = []
N = len(lines)
for i in range(len(lines)):
	tmp = lines[i].strip().split(' ')
	for j in range(len(tmp)):
		tmp[j] = float(tmp[j])
	ty.append(tmp[-1])
	del tmp[-1]
	tmp.append(1.0)
	tdata.append(tmp.copy())
tdata = np.array(tdata)
ty = np.array(ty)

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
M = len(tdata[0])
lamda = 10**-4
w = 2/N * inv(2*lamda/N*np.eye(M) + 2/N*tdata.T.dot(tdata)).dot(tdata.T).dot(ty)
print(w)

# Ein ----------------
err = 0
for i in range(N):
	tmp = 0.0
	for j in range(M):
		tmp += tdata[i][j] * w[j]
	# print(tmp)
	if tmp > 0 and ty[i] == -1 :
		err += 1
	if tmp <= 0 and ty[i] == 1:
		err += 1
	
print('Ein :', end = ' ')
print(err / N)

# start testing -----------------------------------------
err = 0
for i in range(len(sdata)):
	tmp = 0
	for j in range(M):
		tmp += w[j] * sdata[i][j]
	
	if tmp > 0 and sy[i] == -1:
		err += 1
	if tmp <= 0 and sy[i] == 1:
		err += 1

print('Eout :', end = ' ')
print(err/len(sdata))