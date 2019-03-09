import random
fp = open('hw1_18_train.dat', 'r')
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
print("1 : " + str(count))

fp2 = open('hw1_18_test.dat', 'r')
line = 'str'
X2 = []
Y2 = []
count = 0
# 讀好X2和Y2
while 1:
    line = fp2.readline().strip().split(' ')
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
    Y2.append(int(line[1]))
    X2.append(tmp)   
print("2 : " + str(count))

order = [i for i in range(0,len(Y))]


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
    
def check(qq, Y):
    wrong = 0
    for i in range(0, len(Y)):
        if(qq[i] != Y[i]):
            wrong += 1
    return wrong


times = []
for zz in range(0,2000):
    count = 0
    random.shuffle(order)
    w = [0 for i in range(0,5)]
    optimal_w = []
    optimal_wrong = len(Y)

    while 1:
        qq = mul(w, X)
        change = 0        
        for i in order:
            if count >= 100:
                break
            if qq[i] != Y[i]:
                change = 1
                for j in range(0,5):
                    w[j] = X[i][j] * Y[i] + w[j]
                qq = mul(w, X)
                count += 1
                tmp = check(qq, Y)
                if tmp < optimal_wrong:
                    optimal_w = w.copy()
                    optimal_wrong = tmp
        if count >= 100 or change == 0:
            break

    test_qq = mul(optimal_w, X2)
    count = check(test_qq, Y2)
    times.append(count)
    
#print(times)

avg = 0.0
for zz in range(0,2000):
    avg += times[zz]
print(avg / (2000 * len(Y2)))



    


