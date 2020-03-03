import sys

line_1 = sys.stdin.readline()
line_2 = sys.stdin.readline()

set_1 = {}
set_2 = {}

length_s = min(len(line_1),len(line_2))
length_l = max(len(line_1),len(line_2))

for i in range(0,length_s):

    set_1 += line_1[i]
    set_2 += line_2[i]
