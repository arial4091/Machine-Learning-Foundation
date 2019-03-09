import random
import matplotlib.pyplot as plt
fp = open('hw1_7_train.dat', 'r')
line = 'str'
X = []
Y = []
count = 0
# 讀好X和Y
while 1:
    line = fp.readline().strip().split(' ')
    count += 1
    if len(line) != 4:
        break
    tmp = []
    tmp.append(1)
    tmp.append(float(line[0]))
    tmp.append(float(line[1]))
    tmp.append(float(line[2]))
    line = line[-1].split('\t')
    tmp.append(float(line[0]))
    Y.append(int(line[1]))
    X.append(tmp)
#print("1 : " + str(count))

def mul(W, X):
    qq = []
    for j in range(0, len(X)):
        tmp = 0
        for k in range(0, 5):
            tmp += W[k] * X[j][k]
        if tmp > 0:
            qq.append(1)
        else:
            qq.append(-1)
    return qq


order = [i for i in range(0,len(Y))]
times = []
for zz in range(0,1126):
    count = 0
    random.shuffle(order)
    w = [0 for i in range(0,5)]

    while 1:
        qq = mul(w, X)
        change = 0        
        for i in order:            
            if qq[i] != Y[i]:
                change = 1
                for j in range(0,5):
                    w[j] = X[i][j] * Y[i] + w[j]
                qq = mul(w, X)
                count += 1
                
        if change == 0:
            break
    times.append(count)

    
    
#print(times)

avg = 0.0
for zz in range(0,1126):
    avg += times[zz]
print(avg / 1126 )

plt.hist(times)
plt.show()