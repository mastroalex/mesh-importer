import os
import src.helpers.meshimporter as m


def writeMesh(ids,lines,path):
    nodes=[]
    
    for l in range(ids["FirstNodesLine"],ids["LastNodesLine"]):    
        nodes.append(list(map(float, lines[l].split())))
    
    for k in range(ids["ElementTypes"]):
        elements=[]
        IDs=[]
        for l in range(ids["FirstElementLine"][k],ids["LastElementLine"][k]):    
            currentList=list(map(int, lines[l].split()))
            elements.append([x+1 for x in currentList])
        m.writeElements(path,elements,ids,k)
       
        for l in range(ids["FirstIDLine"][k],ids["LastIDLine"][k]): 
            IDs.append(list(map(int, lines[l].split())))
        m.writeIDs(path,IDs,ids,k)
    m.writeNodes(path,nodes)

    f = open(path+'\\meshInfo.txt', 'w')
    f.write(str(ids)+'\n')
    f.close()