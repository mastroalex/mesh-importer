import os
import src.helpers.meshimporter as m

def writeElements(path,elements,ids,k):
    currentPath=path+'Elements_'+str(ids["ElementNames"][k])+'.txt'
    os.makedirs(os.path.dirname(currentPath), exist_ok=True)
    f = open(currentPath, 'w')
    for i in range(len(elements)):
        f.write(" ".join(map(str, m.mapConnectivity(elements[i])))+'\n')
    f.close()

def writeIDs(path,IDs,ids,k):
    f = open(path+'ID_'+str(ids["ElementNames"][k])+'.txt', 'w')
    for i in range(1,len(IDs)):
        f.write(" ".join(map(str, IDs[i]))+'\n')
    f.close()

def writeNodes(path,nodes):
    f = open(path+'nodes.txt', 'w')
    for i in range(len(nodes)):
        f.write(" ".join(map(str, m.mapConnectivity(nodes[i])))+'\n')
    f.close()

def writeMesh(ids,lines,path):
    nodes=[]
    
    for l in range(ids["FirstNodesLine"],ids["LastNodesLine"]):    
        nodes.append(list(map(float, lines[l].split())))
    
    for k in range(ids["ElementTypes"]):
        elements=[]
        IDs=[]
        for l in range(ids["FirstElementLine"][k],ids["LastElementLine"][k]): 
            currentList=list(map(int, lines[l].split()))
            elements.append([x+1 for x in currentList])# +1 because elements in mathematica starts from 1
        writeElements(path,elements,ids,k)
       
        for l in range(ids["FirstIDLine"][k],ids["LastIDLine"][k]): 
            currentList=list(map(int, lines[l].split()))
            IDs.append([x+1 for x in currentList])# +1 because indexes in mathematica starts from 1
        writeIDs(path,IDs,ids,k)
    writeNodes(path,nodes)

    f = open(path+'meshInfo.txt', 'w')
    f.write(str(ids)+'\n')
    f.close()