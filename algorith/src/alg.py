'''
Created on 20 Sep 2015

@author: some
'''
def nodes1():
    print("nodes1")
   #intM=[0, 1,2 ,2, 4, 5, 2 ,2 ,8 ,9]
    #intM=[7,1,6,0,4,7,0,1,3,0]
    #intM=[8,1,5,5,5,5,8,5,3,6]#8 1 5 5 5 5 8 5 3 6
    #intM=[3,5,6,9,3,3,3,3,5,1]
    #intM=[2,6,5,5,1,5,5,5,5,6]
    #intM=[0,9,0,0,2,2,4,2,9,2]
    #intM=[8,8,2,0,2,9,2,8,2,2]
    intM=[8,9,8,7,8,9,1,8,6,8]
    cnt=[0]*10
    for ind in range(len(intM)): 
        i=ind
        print("start: ",i,ind)
        while (i!=intM[i]):  
            
            i = intM[i]
            
            cnt[i]=cnt[i]+1
            print("inter: ",i,intM[i],cnt[intM[i]])
    print("number of nodes is ",max(cnt),cnt)
 
def nodes():
    print("nodes")
   #intM=[0, 1,2 ,2, 4, 5, 2 ,2 ,8 ,9]
    #intM=[7,1,6,0,4,7,0,1,3,0]
    #intM=[8,1,5,5,5,5,8,5,3,6]#8 1 5 5 5 5 8 5 3 6
    #intM=[3,5,6,9,3,3,3,3,5,1]
    #intM=[2,6,5,5,1,5,5,5,5,6]
    #intM=[0,9,0,0,2,2,4,2,9,2]
    #intM=[8,8,2,0,2,9,2,8,2,2]
    #intM=[0,1,2,3,4,2,6,0,2,9]
    #intM=[8,8,3,8,9,9,3,8,8,3]
    intM=[1,7,8,4,7,7,9,7,7,4]
    list=[]
    for i in range(len(intM)):
        g=[j for j in range(len(intM))if intM[i]==intM[j]]
        print (g)
        if len(g)>0 and [g,intM[i]] not in list: list.append([g,intM[i]])
    nodes=0
    for g in list:
        for k in list:
            if k!=g:
                if g[1] in k[0]:
                    nodes+=1
    print (list)

#nodes1()
nodes()