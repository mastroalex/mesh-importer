import os
import sys
import src.helpers.meshimporter as m
import src.helpers.meshwriter as w
import tkinter as tk
from tkinter import filedialog

def main(argv):
    currentPath =  os.path.dirname(__file__)
    if len(argv) < 1:
        # create a root window
        root = tk.Tk()
        root.withdraw()

        # open the file dialog box
        meshToRead = filedialog.askopenfilename()
        meshToExportPath=currentPath+'\\meshOutput\\'
        
    elif len(argv)==1:
        # read mesh path
        meshToRead = argv[0]
        meshToExportPath=currentPath+'\\meshOutput\\'

    elif len(argv)==2:
        # read mesh path and output path
        meshToRead = argv[0]
        meshToExportPath = argv[1]+'\\'

    else:
        exit(1)      
    
    with open(meshToRead) as f:
        lines = f.readlines()
    
    ids=m.findDelimiter(lines)

    #for k in ids["LastElementLine"]:
    #    print("Minus:")
    #    print(lines[k-1])
    #    print("Actual:")
    #    print(lines[k])
    
    #for lin in ids:
        # print mesh properties
    #    print(lin+": "+str(ids[lin]))

    # write .txt files
    w.writeMesh(ids,lines,meshToExportPath)


if __name__ == "__main__":
    main(sys.argv[1:])

