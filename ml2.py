import random
import numpy as np
import matplotlib.pyplot as plt

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
# ----------generate training data--------------
x = np.zeros(20)
y = np.zeros(20)
noise_y = np.zeros(20)
flip = [0, 0, 0, 0, 0, 0, 0, 0, 1, 1]
yin = np.zeros(20)
Ein = []
Eout = []

for qq in range(1000):
	# print(qq)
	size_x = 0
	while size_x < 20:
		k = random.uniform(-1, 1)
		if k != 0:
			x[size_x] = k
			size_x += 1
	x.sort()
	# print(x)
	# -----------------generate label and noise----------------------
	for i in range(20):
		y[i] = sign(x[i])
		random.shuffle(flip)
		if flip[0] == 1:
			noise_y[i] = (-1 * y[i])
		else:
			noise_y[i] = y[i]
	# print(y)
	# print(noise_y)
	# -----------------training, find best method and Ein------------- 
	opt_err = 2
	opt_index = 0
	opt_s = 1
	
	for i in range(20):
		for j in range(i):
			yin[j] = -1
		for j in range(i, 20):
			yin[j] = 1
		err = error(noise_y, yin)
		if err < opt_err:
			opt_err = err
			opt_index = i

		for j in range(20):
			yin[j] *= -1
		err = error(noise_y, yin)
		if err < opt_err:
			opt_err = err
			opt_index = i
			opt_s = -1
	# print('Ein : ' + str(opt_err))
	# print('opt index : ' + str(opt_index))
	# print('opt_s : ' + str(opt_s))
	Ein.append(opt_err)

	# ---------------------generate test data and find Eout--------------
	i = 0.5 + 0.3 * opt_s * (abs(x[opt_index]) - 1)
	# print('Eout : ' + str(err))
	Eout.append(i)

# print(Ein / 5000)
# print(Eout / 5000)
times = []
for i in range(len(Ein)):
	times.append(Ein[i] - Eout[i])
plt.hist(times, bins = 100)
plt.show()