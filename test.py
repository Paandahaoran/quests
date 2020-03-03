import numpy as np
import re
i = np.arange(1,16,1)
i = sorted(i)
i = str(i).replace(']',', ').replace('[',', ').split(', ')
i = [x for x in i if x != '']
print(sorted(i))
