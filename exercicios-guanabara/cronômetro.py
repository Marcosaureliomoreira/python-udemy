

from time import sleep

'''cronometroMil = 0
cronometroSeg = 0
print(cronometroMil, cronometroSeg)
while True:
    for cronometroMil in range(0, 100):
        if cronometroMil == 99:
            cronometroSeg += 1
            print(cronometroSeg, end='')
            sleep(1)'''


import time, sys

for i in range(0, 10):
    sys.stdout.write("\r{}".format(i))
    sys.stdout.flush()
    time.sleep(1)

print("\nFim")




