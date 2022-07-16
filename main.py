import matplotlib.pyplot as plt
RANGE = 100
START = -11
ROW = list()

for i in range(RANGE):
    ROW.append(START)
    if START % 2 == 0:
        START /= 2
    else:
        START = START * 3 + 1

plt.plot(list(range(1, RANGE + 1)), ROW)
plt.show()

# Why always ends with cycle?