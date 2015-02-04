'''
Created on Feb 3, 2015

@author: Michael
'''
import pickle; import os.path;

def getDirectoriesForSaving(LoadSaved, SearchPath):
    if os.path.isfile('filelocs.p') == False or LoadSaved == False:
        import Tkinter;import tkFileDialog
        print 'Select file'
        root = Tkinter.Tk()
        root.withdraw()
        path = tkFileDialog.askopenfilename(initialdir = SearchPath, parent = root, title = 'Open Search File')
        DataPath = tkFileDialog.askdirectory(initialdir = SearchPath, parent = root, title = 'Select Root Subject Directory')
        OutPath = tkFileDialog.askdirectory(initialdir = SearchPath, parent = root, title = 'Select Root OUTPUT Directory')
        fileLocations = (path,DataPath,OutPath) #vector to hold file paths
        pickle.dump(fileLocations, open('filelocs.p', 'wb'))
    else: 
        fileLocations = pickle.load(open('filelocs.p', 'rb'))
        path = fileLocations[0]; DataPath = fileLocations[1]; OutPath = fileLocations[2]
    return path, DataPath, OutPath