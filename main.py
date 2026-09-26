import matplotlib.pyplot as plt
import math
import random
import numpy as np


def main():
    ra = range(0, 300)
    rnormal = np.random.normal(1.0, 1, 100)
    r = list(ra)
    data = []
    data2 = []
    data3 = []
    data4 = []
    data_sum = []
    data_ist = []
    hist = []

    p = []
    ig = []
    d = []

    integral = 0
    lastdelta = 0

    for x in r:
        r[x] *= 0.1

    for x in r:
        data.append(math.sin(x)+1)

    for x in r:
        data2.append(math.sin(1.1*x)+1)

    for x in r:
        data3.append(math.sin(2.3*x)+1)

    for x in r:
        data4.append(0.1*math.sin(34*x)+1)

    for i in ra:
        data_sum.append(data[i]+data2[i]+data3[i]+data4[i])

    data_ist = data_sum.copy()

    for i in range(0, 100):
        data_ist[i+100] = data_sum[i+100]*rnormal[i]

    #for i in range(25, 150):
    #    data_ist[i] = data_sum[i]-1

    #for i in range(150, 275):
   #     data_ist[i] = data_sum[i]+1

    for i in ra:
        soll = data_sum[i]
        ist = data_ist[i]

        delta = (soll-ist)/soll
        p.append(delta)

        integral = integral*0.99 + delta*(10*5)

        ig.append(integral+1)

        derivative = delta - lastdelta

        d.append(derivative+2)

        lastdelta = delta

    summe = 0

    for i in ra:
        summe += data_sum[i]-data_ist[i]

        hist.append(data_ist[i]/data_sum[i])

    aaa = 0

    for i in hist:
        aaa += ((i-1)**2)/300

    aaa = math.sqrt(aaa)


    print('summe: ' + str(summe))
    print('integral: ' + str(integral))
    print('standardabweichung: ' + str(aaa))


    fig, ax = plt.subplots()
    #ax.plot(r, data)
    #ax.plot(r, data2)
    #ax.plot(r, data3)
    #ax.plot(r, data4)
    ax.plot(r, data_sum)
    ax.plot(r, data_ist)

    ax.plot(r, p)
    ax.plot(r, ig)
    ax.plot(r, d)

    ax.set(xlabel='time (s)', ylabel='voltage (mV)', title='About as simple as it gets, folks')
    ax.grid()

    fig.savefig("p.png")
    plt.show()

    plt.close(fig)

    plt.hist(hist, density=True, bins=30)
    plt.savefig("hist.png")
    plt.show()



if __name__ == '__main__':
    main()
