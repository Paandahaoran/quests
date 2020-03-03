import sys

#用 sorted函数对字符串根据asc-II排序
a = sys.stdin.readline().strip()
a_set = set(sorted(a))
print(sorted(a_set))
