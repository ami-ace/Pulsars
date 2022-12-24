fh=open('/home/ambica/Desktop/decaps2/atnfnew.txt','r')
fw=open('/home/ambica/Desktop/decaps2/empty.txt','r+')
lst=['0']
lst2=[]
i=1
j=0
for line in fh:
    if i!=0 and i%6==0:
        i+=1
        continue
    line=line.rstrip()
    lst=line.split(" ")
    for element in lst:
        if element !='':
            j+=1
            if j==1 or j==2:
                lst2.append(element)
            elif j==3:
                hms=[]
                hms=element.split(":")
                hms.append('0')
                hms.append('0')
                print(hms)
                elt=15*float(hms[0])+0.25*float(hms[1])+(float(hms[2]))/240
                lst2.append(elt)
            elif j==4:
                dms=[]
                dms=element.split(":")
                dms.append('0')
                dms.append('0')
                print(dms)
                if float(dms[0])>=0:
                    elt=float(dms[0])+(float(dms[1]))/60+(float(dms[2]))/3600
                else:
                    elt=float(dms[0])-(float(dms[1]))/60-(float(dms[2]))/3600
                lst2.append(elt)
                
        
    j=0           
    #print(lst)
    #print(lst2)
    fw.write('\n'+str(lst2[1])+', '+str(lst2[2])+', '+str(lst2[3]))
    lst=[]
    lst2=[]
    i+=1