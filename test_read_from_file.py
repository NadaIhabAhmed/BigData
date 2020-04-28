def count(arry_x,mim,suportA):
    count_arry=[]
    refranc   =[]
    get_index =0
    Support   =0
    for x in arry_x :       
        if (x in refranc) == 0 :
            cou = arry_x.count(x)
            if cou >= mim:
                Support=cou/len(arry_x)
                
                refranc.append(x)
                count_arry.append([[x], Support , [get_index] ] )
                suportA.append([[x], Support])
        else :
            index1 = refranc.index(x)
            count_arry[index1][2].append(get_index)
        get_index = get_index+1;    
    return count_arry


############################################

def SupportItemSet( SupportA , SupportB , total , minSupport):
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

###################################################3


def get_first(original , min_count , SupportAar):
  first_set = []
  for i in original :
    first_set.append(count(i,min_count, SupportAar))
  return first_set


def get_Item (first_set , Any_list , Total_count ,min_support):
  set_A = []
  for i in Any_list:

      for j in first_set:
          ch = j[0][0][0][0]
          count = 0

          for char in i[0][0] :           
            if char[0] < ch:
              count = count + 1
          
          if count == len(i[0][0]):
            ary = SupportItemSet(i ,j , Total_count  , min_support )
            if len(ary) != 0 :
              set_A.append(ary)

  return set_A

#####################################################
#####################################################

A=['A1','A3','A1','A3','A1','A3','A2']
B=['B2','B4','B2','B4','B2','B5','B6']
C=['C3','C5','C6','C5','C6','C1','C1']
D=['D4','D3','D4','D3','D4','D5','D5']
E=['E8','E1','E8','E1','E6','E6','E9']
F=['F5','F8','F6','F5','F6','F8','F5']

original = []

original.append(A)
original.append(B)
original.append(C)
original.append(D)
original.append(E)
original.append(F)

SupportAar = []
lows       = []

Total_count = len(A)
min_count   = int(input("please input min count "))
min_support = min_count / Total_count

first_set  = get_first(original , min_count , SupportAar)
final_list = first_set

while True: 
     temp =  get_Item (first_set , final_list , Total_count ,min_support)
     if len(temp) != 0:
        final_list = temp
        for j in final_list:
          for i in j:
            SupportAar.append([i[0],i[1]])
     else:
       break

for j in final_list:
  for i in j:
    for k in i[0]:
      index = i[0].index(k)
      X = [k]
      Y = i[0][0:index]+i[0][index+1:]
      for XY in SupportAar:
        if X == XY[0]:
          supportX = XY[1]
        elif Y == XY[0]:
          supportY = XY[1]

      lows.append([X , Y ,i[1] , supportX , supportY])
      lows.append([Y , X ,i[1] , supportX , supportY])

for i in final_list:
  for j in i:
    print(j)

for i in lows:   
    print(i)
