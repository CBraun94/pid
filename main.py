import matplotlib.pyplot as plt
import math
import random
import numpy as np

ext = '.png'


def plot(x, y, xlabel='x', ylabel='y', title='title', filename=None):
    fig, ax = plt.subplots()

    for i in y:
        ax.plot(x, i['data'], label=i['title'], linewidth=1)

    ax.set(xlabel=xlabel, ylabel=ylabel, title=title)
    ax.grid()

    leg = plt.legend()
    # get the individual lines inside legend and set line width
    for line in leg.get_lines():
        line.set_linewidth(1)

    if filename is not None:
        fig.savefig(filename)
    #plt.show()

    plt.close(fig)


def main():
    ra = range(0, 100)
    rnormal = np.random.normal(0.8, 0.05, 30)
    rnormal2 = []
    r = list(ra)
    data = []
    data2 = []
    data3 = []
    data4 = []
    data5 = []
    data_sum = []
    data_ist = []
    hist = []

    p = []
    ig = []
    d = []

    integral = 0
    lastdelta = 0

    for i in rnormal:
        rnormal2.append(1+(1-i))

    for x in r:
        r[x] *= 0.1

    for x in r:
        data.append(math.sin(x)*1.5)

    for x in r:
        data2.append(math.sin(1.1*x)*1.5)

    for x in r:
        data3.append(math.sin(2.3*x)*1.5)

    for x in r:
        data4.append(0.1*math.sin(34*x)*1.5)

    for x in r:
        data5.append((x % 1)*1)

    for i in ra:
        data_sum.append(5+data[i]+data2[i]+data3[i]+data4[i]+data5[i])

    data_ist = data_sum.copy()

    for i in range(0, 30):
        data_ist[i+10] = data_sum[i+10]*rnormal[i]

    for i in range(0, 30):
        data_ist[i+60] = data_sum[i+40]*rnormal2[i]

    #for i in range(25, 150):
    #    data_ist[i] = data_sum[i]-1

    #for i in range(150, 275):
   #     data_ist[i] = data_sum[i]+1

    for i in ra:
        soll = data_sum[i]
        ist = data_ist[i]

        delta = (soll-ist)/soll
        p.append(delta)

        integral = integral*0.99 + delta*(10*0.01)

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
        aaa += ((i-1)**2)/400

    aaa = math.sqrt(aaa)


    print('summe: ' + str(summe))
    print('integral: ' + str(integral))
    print('standardabweichung: ' + str(aaa))

    bbb = []

    bbb.append({'data': data_sum, 'title': 'soll'})
    bbb.append({'data': data_ist, 'title': 'ist'})

    bbb.append({'data': p, 'title': 'p'})
    bbb.append({'data': ig, 'title': 'i'})
    bbb.append({'data': d, 'title': 'd'})

    plot(x=r, y=bbb, xlabel='time', ylabel='y', title='plot', filename='plot'+ext)

    #plot(x=r, y=data_sum, xlabel='time', ylabel='y', title='soll', filename='soll'+ext)
    #plot(x=r, y=data_ist, xlabel='time', ylabel='y', title='ist', filename='ist'+ext)
   # plot(x=r, y=p, xlabel='time', ylabel='y', title='p', filename='p'+ext)
    #plot(x=r, y=ig, xlabel='time', ylabel='y', title='i', filename='i'+ext)
    #plot(x=r, y=d, xlabel='time', ylabel='y', title='d', filename='d'+ext)
    #plot(x=r, y=[data_sum, data_ist], xlabel='time', ylabel='y', title='title', filename='soll.png')

    plt.hist(hist, density=True, bins=30)
    plt.savefig("hist.png")
    #plt.show()



if __name__ == '__main__':
    main()
