import os

def writeElements(path,elements,ids,k):
    f = open(path+'\\Elements_'+str(ids["ElementNames"][k])+'.txt', 'w')
    for i in range(1,len(elements)):
        f.write(", ".join(map(str, elements[i]))+'\n')
    f.close()

def writeIDs(path,IDs,ids,k):
    f = open(path+'\\ID_'+str(ids["ElementNames"][k])+'.txt', 'w')
    for i in range(1,len(IDs)):
        f.write(", ".join(map(str, IDs[i]))+'\n')
    f.close()

def findDelimiter(lines):
    # loop over the different properties described by a dictionary
    # complete the different step for ids{}
    # return ids
    breaker=[]
    ids={}
    ids["ElementNames"]=[]
    ids["ElementNumber"]=[]
    ids["FirstElementLine"]=[]
    ids["LastElementLine"]=[]
    ids["ElementTypes"]=0
    ids["FirstIDLine"]=[]
    ids["LastIDLine"]=[]
    for i in range(len(lines)):
        if "sdim" in lines[i]:
            ids["Dimensions"]=extractDigit(lines[i])
        if "Mesh vertex coordinates" in lines[i]:
            ids["FirstNodesLine"]=i+1#element start following line
        if "#" in lines[i]:
            breaker.append(i)
        if "# number of element types" in lines[i]:
            ids["ElementTypes"]=extractDigit(lines[i])
  
        if "# Type" in lines[i]:
            for k in range(ids["ElementTypes"]):
                #print(extractDigit(lines[i].replace("#","")))
                if extractDigit(lines[i].replace("#",""))==k:
                   for j in range(8):
                        if "# type name" in lines[i+j]:
                           ids["ElementNames"].append(elementName(lines[i+j]))
                        if "# number of elements" in lines[i+j]:
                           ids["ElementNumber"].append(extractDigit(lines[i+j]))
                        if "# Elements" in lines[i+j]:
                           ids["FirstElementLine"].append(i+j+1)#+1 because element start the next line
        if "# Geometric entity indices" in lines[i]:
            ids["FirstIDLine"].append(i+1)

    for k in range(len(ids["FirstIDLine"])):
        ids["LastIDLine"].append(findLastLineOfInterest(breaker,ids["FirstIDLine"][k]))

    lastNode=findLastLineOfInterest(breaker,ids["FirstNodesLine"])
    ids["LastNodesLine"]=lastNode      
    
    for k in range(ids["ElementTypes"]):
        ids["LastElementLine"].append(findLastLineOfInterest(breaker,ids["FirstElementLine"][k]))
        if ids["LastIDLine"][k]==-1:
            ids["LastIDLine"][k]=len(lines)

    return ids

def elementName(string):
    if "vtx" in string:
        return "Vertex"
    elif "edg2" in string:
        return "L2"
    elif "tri2" in string:
        return "T2"
    elif "tet2" in string:
        return "O2"
    ## need to be completed
    else:
        return ""


def extractDigit(string):
    num=""
    for s in string.split():
                if s.isdigit():
                    num=int(s)
    return num


def writeNodes(path,nodes):
    f = open(path+'\\nodes.txt', 'w')
    for i in range(1,len(nodes)):
        f.write(", ".join(map(str, nodes[i]))+'\n')
    f.close()

def findLastLineOfInterest(breaker,firstLine):
    value=[]
    for i in breaker:
        if i > firstLine:
            value.append(i)
    if value:
        breakLine=min(value)
    else:
        breakLine=0
    return breakLine-1
