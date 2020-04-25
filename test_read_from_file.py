def count(arry_x,mim):
    count_arry=[]
    refranc=[]
    get_index=0
    Support=0
    for x in arry_x :
        
        if  (x in refranc)==0:
            cou=arry_x.count(x)
            if cou >= mim:
                Support=cou/len(arry_x)
                
                refranc.append(x)
                count_arry.append([[x], Support , [get_index] ] )
                
        else :
            index1=refranc.index(x)
            count_arry[index1][2].append(get_index)
        get_index = get_index+1;    
    return count_arry


def SupportTwoItemSet( SupportA , SupportB , total , minSupport):
  index = []
  supportArray = []
  count = 0
  for firstIndex in SupportA:
      A = firstIndex[2]
      for secondIndex in SupportB:
          B = secondIndex[2]         
          for row in A :
              if row in B:
                 count=count+1
                 index.append(row)

          support = count/total

          if(support >= minSupport ):
              firsttuple = firstIndex[0] + secondIndex[0] 
              supportArray.append([ firsttuple , support , index ])

          index = []
          count = 0

  return supportArray



f = open("ticdata2000.txt", "r")
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

for x in f:
    #m=x[6:28]
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


   
