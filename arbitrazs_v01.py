import numpy
import string
import datetime

def lensum(list):
    a=numpy.zeros(len(list))
    for i in range(len(list)):
        a[i]=len(lines[i])-1
    return (a)

with open("David.txt") as f:
    lines = f.readlines()
    print(lines)
cnt=numpy.zeros(41)
cntsajat=numpy.zeros(41)
car=numpy.zeros(len(lines))
carsajat=numpy.zeros(len(lines))
print(len(lines))
honapok=["2015-12", "2016-01", "2016-02", "2016-03", "2016-04","2016-05","2016-06","2016-07","2016-08","2016-09",
         "2016-10", "2016-11", "2016-12", "2017-01", "2017-02", "2017-03", "2017-04", "2017-05", "2017-06", "2017-07", "2017-08",
         "2017-09", "2017-10", "2017-11", "2017-12", "2018-01", "2018-02", "2018-03", "2018-04", "2018-05", "2018-06", "2018-07", "2018-08",
         "2018-09", "2018-10", "2018-11", "2018-12", "2019-01", "2019-02", "2019-03", "2019-04"]
for i in range(len(lines)):
    for j in range(41):
        if(lines[i].startswith(honapok[j])):
            cnt[j]=cnt[j]+1
            if (lines[i+1]=="Adrián Bohner\n"):
                carsajat[i]=len(lines[i+2])-1
                cntsajat[j] = cntsajat[j] + 1
            car[i] = len(lines[i + 2]) - 1
            j=j+1
def davidprintelés():
    for i in range(41):
        print("%s \t %s" % (honapok[i], int(cnt[i])-6))
    print("Adrián üzenetek száma: %s" % (sum(cntsajat)))
    print("Összes karakter száma: %s" % (sum(car)))
    print("Adrián karakterek száma: %s" % (sum(carsajat)))
    print("Partner karakterek száma: %s" % (sum(car)-sum(carsajat)))

def printelés():
    for i in range(41):
        print("%s \t %s" % (honapok[i], (int(cnt[i])-int(cnt[0]))))
    print("Adrián üzenetek száma: %s" % (sum(cntsajat)))
    print("Összes karakter száma: %s" % (sum(car)))
    print("Adrián karakterek száma: %s" % (sum(carsajat)))
    print("Partner karakterek száma: %s" % (sum(car)-sum(carsajat)))

if (f.name=="David.txt"):
    davidprintelés()
else:
    printelés()
davidprintelés()
#hány nap szünet átlagosan?

def konvertalo(eredeti):
    konvertalt=[0,0,0]
    l=list(eredeti)
    ev=[l[0], l[1], l[2], l[3]]
    honap=[l[5], l[6]]
    nap=[l[8], l[9]]
    konvertalt[0]=int("".join(ev))
    if (l[5]==0):
        konvertalt[1]=int(l[6])
    else:
        konvertalt[1]=int("".join(honap))
    if (l[8]==0):
        konvertalt[2] = int(l[9])
    else:
        konvertalt[2]=int("".join(nap))
    return(konvertalt)

def honapvalto(honap):
    honaphosszak = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    i = 0
    ertek1 = 0
    while (i < honap):
        ertek1 = ertek1 + honaphosszak[i-1]
        i+=1
    return(ertek1)


def atvalto(kezdoev, kezdohonap, kezdonap, ev, honap, nap):
    if (kezdoev==ev):
        if(kezdohonap==honap):
            return(-honapvalto(kezdohonap)-kezdonap+honapvalto(honap)+nap-1)
        else:
            return(-honapvalto(kezdohonap) - kezdonap + honapvalto(honap) + nap-1)
    else:
        return(-honapvalto(kezdohonap) - kezdonap + honapvalto(honap) + nap+365-1)

kezdosz=input("Date to start: ")
zarosz=input("Date to end: ")
kezdo = konvertalo(kezdosz)
zaro = konvertalo(zarosz)
#print(kezdo)
#print(zaro)
datumok=[]
datumtomb=[]

for i in range(1, len(lines)):
    if (lines[i]==("\n")):
        datumok.append(lines[i+1])
for i in range(len(datumok)):
    datumtomb.append(konvertalo(datumok[i]))

differencia=[]
for i in range(1, len(datumtomb)):
    if (datumtomb[i-1][2]!= datumtomb[i][2]):
        differencia.append(atvalto(datumtomb[i-1][0],datumtomb[i-1][1],datumtomb[i-1][2],datumtomb[i][0],datumtomb[i][1],datumtomb[i][2]))
        i+=1
        #print("%s %s" % ((datumtomb[i][1]), datumtomb[i][2]), differencia)
    else:
        i+=1

valosdiff=[]
valosdatumtomb=[]
for i in range(1, len(datumtomb)):
    if (datetime.date(kezdo[0], kezdo[1], kezdo[2])<=datetime.date(datumtomb[i][0], datumtomb[i][1], datumtomb[i][2]) and
        datetime.date(zaro[0], zaro[1], zaro[2])>=datetime.date(datumtomb[i][0], datumtomb[i][1], datumtomb[i][2])):
        valosdatumtomb.append(datumtomb[i])


for i in range(1, len(valosdatumtomb)):
    if (valosdatumtomb[i-1][2]!= valosdatumtomb[i][2]):
        valosdiff.append(atvalto(valosdatumtomb[i-1][0],valosdatumtomb[i-1][1],valosdatumtomb[i-1][2],valosdatumtomb[i][0],valosdatumtomb[i][1],valosdatumtomb[i][2]))
        i+=1
        #print("%s %s" % ((datumtomb[i][1]), datumtomb[i][2]), differencia)
    else:
        i+=1
#print(valosdatumtomb)
#print(valosdiff)
atlag=numpy.mean(valosdiff)
print("Két beszélgetés között tartott szünetek átlaga napokban %s és %s között: %s" % (kezdosz, zarosz, atlag))
#print(differencia)
#print(datumtomb)
#print(atvalto(2018, 1,31, 2018, 2, 1))




#for i in range(len(datumok)):









