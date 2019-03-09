
import numpy as np
import random

N = 6
x = np.zeros((1000, N))
y = np.zeros((1, 1000))
y_noise = np.zeros((1, 1000))
# flip = [0,0,0,0,0,0,0,0,0,1]
squ_x = np.zeros((N, N))
xty = np.zeros((1,N))
w = np.zeros((1,N))
new_y = np.zeros((1,1000))

totalw = [0, 0, 0, 0, 0, 0]

flip = []
for i in range(900):
	flip.append(0)
for i in range(100):
	flip.append(1)


for qq in range(1):
	
	random.shuffle(flip)
	# make x ------------------------------
	for i in range(1000):
		x[i][0] = 1
		x[i][1] = random.uniform(-1, 1)
		x[i][2] = random.uniform(-1, 1)
		x[i][3] = x[i][1] * x[i][2]
		x[i][4] = x[i][1] * x[i][1]
		x[i][5] = x[i][2] * x[i][2]

	# make y ------------------------------
	for i in range(1000):
		if x[i][1]**2 + x[i][2]**2 <= 0.6:
			y[0][i] = -1
		else:
			y[0][i] = 1
		# random.shuffle(flip)
		if flip[i] == 1:
			y_noise[0][i] = -1 * y[0][i]
		else:
			y_noise[0][i] = y[0][i]

	# make inv(xT * x) -------------------------

	for i in range(N):
		for j in range(N):
			tmp = 0
			for k in range(1000):
				tmp += x[k][i] * x[k][j]
			squ_x[i][j] = tmp
	inverse = np.linalg.inv(squ_x)

	# make xT * y ------------------------------

	for i in range(N):
		tmp = 0
		for j in range(1000):
			tmp += x[j][i] * y_noise[0][j]
		xty[0][i] = tmp

	# make w -----------------------------------

	for i in range(N):
		tmp = 0
		for j in range(N):
			tmp += inverse[i][j] * xty[0][j]
		w[0][i] = tmp

	for i in range(6):
		totalw[i] += w[0][i]
	# for i in range(1000):
	# 	tmp = w[0][0]*x[i][0] + w[0][1]*x[i][1] + w[0][2]*x[i][2] + w[0][3]*x[i][3] + w[0][4]*x[i][4] + w[0][5]*x[i][5]
	# 	if tmp <= 0:
	# 		new_y[0][i] = -1
	# 	else:
	# 		new_y[0][i] = 1
	# tmp = 0
	# for i in range(1000):
	# 	if new_y[0][i] != y_noise[0][i]:
	# 		tmp += 1

for i in range(6):
	totalw[i] /= 1
# print(totalw)
# print(tmp/1000)
# print(w)

ans = 0
for qq in range(100):
	print(qq)
	for i in range(1000):
		x[i][0] = 1
		x[i][1] = random.uniform(-1, 1)
		x[i][2] = random.uniform(-1, 1)
		x[i][3] = x[i][1] * x[i][2]
		x[i][4] = x[i][1] * x[i][1]
		x[i][5] = x[i][2] * x[i][2]
	for i in range(1000):
		if x[i][1]**2 + x[i][2]**2 <= 0.6:
			y[0][i] = -1
		else:
			y[0][i] = 1
		# random.shuffle(flip)
		if flip[i] == 1:
			y_noise[0][i] = -1 * y[0][i]
		else:
			y_noise[0][i] = y[0][i]
	for i in range(1000):
		tmp = w[0][0]*x[i][0] + w[0][1]*x[i][1] + w[0][2]*x[i][2] + w[0][3]*x[i][3] + w[0][4]*x[i][4] + w[0][5]*x[i][5]
		if tmp <= 0:
			new_y[0][i] = -1
		else:
			new_y[0][i] = 1
	tmp = 0
	for i in range(1000):
		if new_y[0][i] != y_noise[0][i]:
			tmp += 1
	ans += tmp/1000
print(ans/100)