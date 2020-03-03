import sys


'''输入形式 字符串和int变化'''
line = list(map(int,sys.stdin.readline().strip().split()))
LIS = 1
print(line)
LIS_max = []
prev = line[0]
curr = 0
for i in range(1,len(line)-1):
    curr = line[i]
    if curr > prev:
        LIS += 1
        prev = curr
    else:
        LIS_max.append(LIS)
        LIS = 1
        prev = curr
if line[-1] > curr:
    LIS += 1
LIS_max.append(LIS)
print(LIS_max)
