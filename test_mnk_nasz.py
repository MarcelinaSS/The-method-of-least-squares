from modul_mnk import *
import matplotlib.pyplot as plt
import pylab
import numpy as np

yy = []
xx = []

with open ("windmil.txt","r") as file:
    dane = file.readlines()
    for line in dane:
        yy.append(float(line.split()[1]))
        xx.append(float(line.split()[0]))
    dane.append(yy)
    dane.append(xx)

print(xx)
print(yy)

res = []
bsr = []

for n in range(2,10):
    aa, bb = gen_ur_mnk(xx, yy, n)

    print(aa)
    print(bb)


    wsp = numpy.linalg.solve(aa, bb) # a0,a1,a2
    print('wsp:', wsp)

    def prawdziwe():
        li = []
        for i in xx:
            wielomian4(i,wsp)
            li.append(wielomian4(i,wsp))
        return li

    prawdziwe()
    r_kwadrat(yy,prawdziwe())
    blad(prawdziwe(),prawdziwe())

    res.append(r_kwadrat(yy,prawdziwe()))
    bsr.append(blad(yy,prawdziwe()))

    print(res)
    print(bsr)

    p = range(2, 17)
    a = min(p)
    b = max(p)
    dx = (b - a) / (len(p)+10)

    zz = [a]
    ww = [wielomian4(a, wsp)]

    for i in p:
        zz.append(zz[-1] + dx)
        ww.append(wielomian4((zz[-1]), wsp))

    print(zz)
    print(ww)
    n = str(n)
    x = zz
    y = ww
    pylab.plot(x, y)
    pylab.title('Model regresji' + " dla " + n + " stopnia wielomianu")
    plt.xlabel("prędkość wiatru[mph]")
    plt.ylabel("moc wiatraka")
    pylab.grid(True)
    # pylab.show()

    plt.plot(xx, yy, 'ro')
    plt.axis([0, 11, 0, 3])
    plt.show()


plt.show()


def wykres1():
    x = [2,3,4,5,6,7,8,9]
    y = res
    pylab.plot(x,y)
    pylab.title('Wartość współczynnika determinacji w zależności od stopnia wielomianu')
    plt.xlabel("stopień wielomianu")
    plt.ylabel("wartość współczynnika determinacji")
    pylab.grid(True)
    pylab.show()

def wykres2():
    i = [2,3,4,5,6,7,8,9]
    j = bsr
    pylab.plot(i,j)
    pylab.title('Wartość błędu średniego w zależności od stopnia wielomianu')
    plt.xlabel("stopień wielomianu")
    plt.ylabel("wartość błędu średniokwadratowego")
    pylab.grid(True)
    pylab.show()

wykres1()
wykres2()













