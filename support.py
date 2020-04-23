def count(*arry_x):
    count

def Support(item,list):
    count=0
    for element in list:
        if(element==item):
            count=count+1
    return count/len(list)
f = open("E:/Chelsea/4thYear/2ndTerm/big data/project/ticdata2000.txt", "r")
A=[]
B=[]
C=[]
D=[]
E=[]
F=[]
G=[]
H=[]
I=[]
J=[]
K=[]
L=[]
count = 0
for x in f:
    #m=x[6:28]
    count=count+1
    if(count==1):
        continue
    data = x.split("\t")
    A.append(int(data[5]))
    B.append(int(data[6]))
    C.append(int(data[7]))
    D.append(int(data[8]))
    E.append(int(data[9]))
    F.append(int(data[10]))
    G.append(int(data[11]))
    H.append(int(data[12]))
    I.append(int(data[13]))
    J.append(int(data[14]))
    K.append(int(data[15]))
    L.append(int(data[16]))
A.sort()
B.sort()
C.sort()
D.sort()
E.sort()
F.sort()
G.sort()
H.sort()
I.sort()
J.sort()
K.sort()
L.sort()
x=5
#print(x)
SupportA=[]
SupportB=[]
SupportC=[]
SupportD=[]
SupportE=[]
SupportF=[]
SupportG=[]
SupportH=[]
SupportI=[]
SupportJ=[]
SupportK=[]
SupportL=[]
for item in A:
    if((len(SupportA)==0) or (item not in (x[0] for x in SupportA))):
        support=Support(item,A)
        SupportA.append([item,support])
for item in B:
    if((len(SupportB)==0) or (item not in (x[0] for x in SupportB))):
        support=Support(item,B)
        SupportB.append([item,support])
for item in C:
    if((len(SupportC)==0) or (item not in (x[0] for x in SupportC))):
        support=Support(item,C)
        SupportC.append([item,support])

for item in D:
    if((len(SupportD)==0) or (item not in (x[0] for x in SupportD))):
        support=Support(item,D)
        SupportD.append([item,support])
for item in E:
    if((len(SupportE)==0) or (item not in (x[0] for x in SupportE))):
        support=Support(item,E)
        SupportE.append([item,support])

for item in F:
    if((len(SupportF)==0) or (item not in (x[0] for x in SupportF))):
        support=Support(item,F)
        SupportF.append([item,support])
for item in G:
    if((len(SupportG)==0) or (item not in (x[0] for x in SupportG))):
        support=Support(item,G)
        SupportG.append([item,support])
for item in H:
    if((len(SupportH)==0) or (item not in (x[0] for x in SupportH))):
        support=Support(item,H)
        SupportH.append([item,support])
for item in I:
    if((len(SupportI)==0) or (item not in (x[0] for x in SupportI))):
        support=Support(item,I)
        SupportI.append([item,support])
for item in J:
    if((len(SupportJ)==0) or (item not in (x[0] for x in SupportJ))):
        support=Support(item,J)
        SupportJ.append([item,support])
for item in K:
    if((len(SupportK)==0) or (item not in (x[0] for x in SupportK))):
        support=Support(item,K)
        SupportK.append([item,support])
for item in L:
    if((len(SupportL)==0) or (item not in (x[0] for x in SupportL))):
        support=Support(item,L)
        SupportL.append([item,support])