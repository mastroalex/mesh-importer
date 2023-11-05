import os

def findDelimiter(lines):
    # define usefull properties
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
        # read mesh dimension
        if "sdim" in lines[i]:
            ids["Dimensions"]=extractDigit(lines[i])
        # find first node row
        if "Mesh vertex coordinates" in lines[i]:
            ids["FirstNodesLine"]=i+1# nodes start next row (+1)
        # all '#' symbol correspond to a section break
        if "#" in lines[i]:
            breaker.append(i)
        if "# number of element types" in lines[i]:
            ids["ElementTypes"]=extractDigit(lines[i])

        # each element type section contains the same structure:
        # Each row like '# Type k' marks the starting point for the kth section
        # Each section contains:
        # - Element name
        # - Number of element
        # - Several row for all the elements
        # marked by the corresponding string

        if "# Type" in lines[i]:
            for k in range(ids["ElementTypes"]):
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

    # findLastLineOfInterest() helps to find the last row for the elements list
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
    # extract number from complex strings including text and number
    num=""
    for s in string.split():
                if s.isdigit():
                    num=int(s)
    return num


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
