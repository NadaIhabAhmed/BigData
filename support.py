def SupportCount(arry_x,mim):
    count_arry=[]
    cou=0
    for x in arry_x :
        if x not in (item[0] for item in count_arry):
            cou=arry_x.count(x)
            Support=cou/len(arry_x)
            if(Support>=mim):
                E=(x,Support)
                count_arry.append(E)
    return count_arry

# def Support(item,list):
#     count=0
#     for element in list:
#         if(element==item):
#             count=count+1
#     return count/len(list)
def FindIndex(mainList,item):
    index=[]
    count=0
    for x in mainList:
        if(x==item):
            index.append(count)
        count=count+1
    return index
def SupportTwoItemSet(firstList,secondList,minSupport):
    #get support for all items in the first list
  firstSupport=SupportCount(firstList,minSupport)

    #get support for all items in the second list
  secondSupport=SupportCount(secondList,minSupport)

    #array containing the support for two item sets from both lists
  supportArray=[]
  for firstIndex in range(len(firstSupport)):
      for secondIndex in range(len(secondSupport)):
          count=0
          for row in range(len(firstList)):
              firstItem=firstSupport[firstIndex][0]
              secondItem=secondSupport[secondIndex][0]
              if(firstList[row]==firstItem and secondList[row]==secondItem):
                  count=count+1
          support=count/len(firstList)
          if(support>=minSupport):
              firsttuple=[firstItem,secondItem]
              supportArray.append([firsttuple,support])
  return supportArray

minSupport=input("Enter minimum support required")
minSupport=float(minSupport)
f = open("E:/Chelsea/4thYear/2ndTerm/big data/project/sample.txt", "r")

#f = open("E:/Chelsea/4thYear/2ndTerm/big data/project/ticdata2000.txt", "r")
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


SupportA=SupportCount(A,minSupport)
SupportB=SupportCount(B,minSupport)
SupportC=SupportCount(C,minSupport)
SupportD=SupportCount(D,minSupport)
SupportE=SupportCount(E,minSupport)
SupportF=SupportCount(F,minSupport)
SupportG=SupportCount(G,minSupport)
SupportH=SupportCount(H,minSupport)
SupportI=SupportCount(I,minSupport)
SupportJ=SupportCount(J,minSupport)
SupportK=SupportCount(K,minSupport)
SupportL=SupportCount(L,minSupport)
print("A",SupportA)
print("B",SupportB)
Array=SupportTwoItemSet(A,B,minSupport)
print("both",Array)
# for item in A:
#     if((len(SupportA)==0) or (item not in (x[0] for x in SupportA))):
#         support=Support(item,A)
#         if(support>= minSupport):
#          SupportA.append([item,support])
# print(SupportA)
# print("new function")
# newA=SupportCount(A,minSupport)
# print(newA)
# for item in B:
#     if((len(SupportB)==0) or (item not in (x[0] for x in SupportB))):
#         support=Support(item,B)
#         if(support>= minSupport):
#          SupportB.append([item,support])
# for item in C:
#     if((len(SupportC)==0) or (item not in (x[0] for x in SupportC))):
#         support=Support(item,C)
#         if(support>= minSupport):
#          SupportC.append([item,support])
#
# for item in D:
#     if((len(SupportD)==0) or (item not in (x[0] for x in SupportD))):
#         support=Support(item,D)
#         if(support>= minSupport):
#          SupportD.append([item,support])
# for item in E:
#     if((len(SupportE)==0) or (item not in (x[0] for x in SupportE))):
#         support=Support(item,E)
#         if(support>= minSupport):
#          SupportE.append([item,support])
#
# for item in F:
#     if((len(SupportF)==0) or (item not in (x[0] for x in SupportF))):
#         support=Support(item,F)
#         if(support>= minSupport):
#          SupportF.append([item,support])
# for item in G:
#     if((len(SupportG)==0) or (item not in (x[0] for x in SupportG))):
#         support=Support(item,G)
#         if(support>= minSupport):
#          SupportG.append([item,support])
# for item in H:
#     if((len(SupportH)==0) or (item not in (x[0] for x in SupportH))):
#         support=Support(item,H)
#         if(support>= minSupport):
#          SupportH.append([item,support])
# for item in I:
#     if((len(SupportI)==0) or (item not in (x[0] for x in SupportI))):
#         support=Support(item,I)
#         if(support>= minSupport):
#          SupportI.append([item,support])
# for item in J:
#     if((len(SupportJ)==0) or (item not in (x[0] for x in SupportJ))):
#         support=Support(item,J)
#         if(support>= minSupport):
#          SupportJ.append([item,support])
# for item in K:
#     if((len(SupportK)==0) or (item not in (x[0] for x in SupportK))):
#         support=Support(item,K)
#         if(support>= minSupport):
#          SupportK.append([item,support])
# for item in L:
#     if((len(SupportL)==0) or (item not in (x[0] for x in SupportL))):
#         support=Support(item,L)
#         if(support>= minSupport):
#          SupportL.append([item,support])
