import os
import src.helpers.meshimporter as m
import src.helpers.meshwriter as w

def main():
    
    fileName='\data\meshFull.mphtxt'
    path =  os.path.dirname(__file__)

    with open(path+fileName) as f:
        lines = f.readlines()
    
    ids=m.findDelimiter(lines)

    print(lines[ids["FirstNodesLine"]])
    print(ids)    

    w.writeMesh(ids,lines,path)


if __name__ == "__main__":
    main()

