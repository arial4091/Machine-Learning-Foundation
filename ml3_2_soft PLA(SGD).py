from matplotlib.pyplot as plt
import numpy as np
import random
from math import exp

eeta = 0.01
# training data ---------------------
fp = open('hw3_train.dat', 'r')
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
	tdata.append(tmp.copy())

# testing data ----------------------
fp2 = open('hw3_test.dat', 'r')
lines = fp2.readlines()
sdata = []
sy = []
for i in range(len(lines)):
	tmp = lines[i].strip().split(' ')
	for j in range(len(tmp)):
		tmp[j] = float(tmp[j])
	sy.append(tmp[-1])
	del tmp[-1]
	sdata.append(tmp.copy())

# Error function -------------------------------
def E_c(w, x, y):
	err = 0
	for i in range(len(x)):
		tmp = 0
		for j in range(len(x[0])):
			tmp += w[j] * x[i][j]
		tmp = 1 / (1 + exp(-1*tmp))
		if tmp >= 0.5 and y[i] == -1:
			err += 1
		if tmp < 0.5 and y[i] == 1:
			err += 1
	return (err/len(y))

# start training ------------------------
M = len(tdata[0])
w = [1 for i in range(M)]
wsgd = [1 for i in range(M)]
e_trad = []
e_sgd = []
t = [i for i in range(1, 2001)]

for qq in range(2000):
	if qq%100 == 0:
		print(qq)
	# traditional gradient of Ein ----------------------
	lines = [0 for i in range(M)]
	for i in range(N):
		tmp = 0
		for j in range(M):
			tmp += w[j] * tdata[i][j]
		tmp *= ty[i]
		tmp = 1 / (1 + exp(tmp))
		for j in range(M):
			lines[j] += tdata[i][j] * ty[i] * -1 * tmp
	for i in range(M):
		lines[i] /= N
		w[i] -= lines[i] * eeta

	# SGD ----------------------------------------------
	tmp = 0
	for j in range(M):
		tmp += wsgd[j] * tdata[qq%N][j]
	tmp *= ty[qq%N]
	tmp = 1 / (1 + exp(tmp))
	for j in range(M):
		lines[j] = tdata[qq%N][j] * ty[qq%N] * -1 * tmp

	for i in range(M):
		wsgd[i] -= lines[i] * eeta
	# E ---------------------------------------------- 
	e_trad.append(E_c(w, tdata, ty))
	e_sgd.append(E_c(wsgd, tdata, ty))
# print(w)

print(e_trad[-1])
print(e_sgd[-1])
plt.plot(t, e_trad, 'r-', t, e_sgd, 'g--')
plt.show()
