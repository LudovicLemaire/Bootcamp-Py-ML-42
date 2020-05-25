import time
from loading import ft_progress

listy = range(2000)
ret = 0
for elem in ft_progress(listy):
    ret += elem
    time.sleep(0.005)
print()
print(ret)
