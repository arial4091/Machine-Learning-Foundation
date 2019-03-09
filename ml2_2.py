import random
import numpy as np

def sign(a):
	if a < 0:
		return -1
	else:
		return 1
def error(yans, yin):
	k = 0
	for i in range(len(yin)):
		if yans[i] != yin[i]:
			k += 1
	return (k / len(yin))
# ------------------------------------------------------------------
# ----------------read training data------------------------------
fp = open('hw2_train.dat', 'r')
line = 'str'
X = []
Y = []

while 1 :
	line = fp.readline().strip().split(' ')
	if len(line) != 10 :
		break
	tmp = []
	for i in range(9):
		tmp.append(float(line[i]))
	X.append(tmp)
	Y.append(float(line[-1]))
print(Y)
opt_dim = 0
opt_theta = 0
opt_s = 0
opt_Ein = 9999

datalen = len(X)
yin = np.zeros(datalen)
for i in range(len(X[0])):
	for j in range(datalen):
		for k in range(datalen):
			if X[k][i] >= X[j][i]:
				yin[k] = 1
				
			else:
				yin[k] = -1	
		err = error(Y, yin)
		if err < opt_Ein:
			opt_Ein = err
			opt_s = 1
			opt_theta = X[j][i]
			opt_dim = i

		for k in range(datalen):
			if X[k][i] >= X[j][i]:
				yin[k] = -1
			else:
				yin[k] = 1
		err = error(Y, yin)
		if err < opt_Ein:
			opt_Ein = err
			opt_s = -1
			opt_theta = X[j][i]
			opt_dim = i

print(opt_Ein)
print(opt_dim)
print(opt_theta)
print(opt_s)
fp.close()

fp = open('hw2_test.dat', 'r')
line = 'str'
X = []
Y = []

while 1 :
	line = fp.readline().strip().split(' ')
	if len(line) != 10 :
		break
	tmp = []
	for i in range(9):
		tmp.append(float(line[i]))
	X.append(tmp)
	Y.append(float(line[-1]))
yin = np.zeros(len(Y))
for i in range(len(X)):
	if X[i][opt_dim] >= opt_theta:
		yin[i] = 1 * opt_s
	else:
		yin[i] = -1 * opt_s
Eout = error(Y, yin)
print(Eout)