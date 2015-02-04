'''
Created on Dec 5, 2014

@author: Michael
'''

import os
from storeDefinitionsHere import extension, omitList



def collectSubjectsInList(pathToData):
    #scan all folders searching for '.txt' and add path to list 
    storePathsHere = [] 
    for path, dirs, files in os.walk( pathToData ):
        for name in files:
            if name.find(extension) > -1:
                found = False
                for i in omitList:
                    if name.find(i.strip()) > -1: found = True
                if found == False:
                    storePathsHere.append( os.path.join(path, name))
    
    #find all occurances of '\'
    inheritedFS = []
    for subjIndex, paths in enumerate(storePathsHere):
        shortPath = paths[len(pathToData)+1:]
        charLocation = []
        for index, char in enumerate(shortPath):    
            if char == '\\': charLocation.append(index)
        
        #break up sting by '\'
        newStr = shortPath
        remainderStr = shortPath
        oldLoc = 0
        begin = 0
        fileStructure = []
        fileStructure.append(subjIndex)
        for loc in charLocation:
            locO = loc - oldLoc
            newStr = remainderStr[begin:locO]
            remainderStr = remainderStr[locO:]
            fileStructure.append( newStr )
            oldLoc = loc
            begin = 1
        fileStructure.append( shortPath[oldLoc+1:] )
        inheritedFS.append(fileStructure)
    
    #remove duplicate entries
    skipList = []
    temporaryList = []
    for slowIndex, slowEntry in enumerate(inheritedFS):
        if slowIndex not in skipList:
            for fastIndex, fastEntry in enumerate(inheritedFS):
                if fastEntry[-1] == slowEntry[-1] and fastIndex != slowIndex and fastEntry[1] == slowEntry[1]:
                    skipList.append(fastIndex)
    for index, entry in enumerate(inheritedFS):
        if entry[0] not in skipList:
            temporaryList.append(entry)
    
    #make filename a string  
    for entry in temporaryList:
        filePath = ''  
        for element in entry[1:]:
            filePath = filePath + '\\' + element
        entry.append(filePath)
        
    #complete the incomplete file manageRawInput (PRE/POST) by adding (none)
    toPop = []
    for index, entry in enumerate(temporaryList):
        newEntry = []
        if len(entry) < 6:
            i = 0
            while i < len(entry):
                if i == 2:
                    newEntry.append('VIOLATION')
                newEntry.append( entry[i] )
                i += 1
            temporaryList.append( newEntry )
            toPop.append(index)
    almostFinalList = []
    for index, entry in enumerate(temporaryList):
        if index not in toPop:
            almostFinalList.append(entry)
    
    #clean final list
    finalList = []
    for i in almostFinalList:
        entry = [ i[1], i[2], i[3], i[-1] ]
        finalList.append(entry)

    #make a dictionary of subjects
    subjDict = {}
    for i, entry in enumerate(finalList):
        subj = finalList[i][0]
        data =  finalList[i][1:]
        subjDict.setdefault(subj, [])
        subjDict[subj].append(data)
    
    #make a dictionary of time and replace subject data
    for thisKey in subjDict.keys():
        timeDict = {}
        for i, entry in enumerate(subjDict[thisKey]):
            timeT = entry[0]
            timeData = entry[1:]
            timeDict.setdefault(timeT, [])
            timeDict[timeT].append(timeData)
            subjDict[thisKey] = timeDict
            
    for thisKey in subjDict.keys():
        
        for thisTime in subjDict[thisKey].keys():
            exper = subjDict[thisKey][thisTime]
            experDict = {}
            for i in exper:
                
                experT = i[0]
                experDat = pathToData+i[1] #joins root with path
                experDict.setdefault(experT, [])
                experDict[experT].append(experDat)
            subjDict[thisKey][thisTime] = experDict
    return subjDict
                
def qualifySubjects(data):
    hasAll = []
    hasPre = []
    hasPost = []
    hasErr = []
    hasNov = []
    hasNBack = []
    for subj in data.keys():
        if subj not in hasAll: hasAll.append(subj)
        if 'PRE' in data[subj].keys() and subj not in hasPre: hasPre.append(subj)
        if 'POST' in data[subj].keys() and subj not in hasPost: hasPost.append(subj)    
        if 'VIOLATION' in data[subj].keys() and subj not in hasErr: hasErr.append(subj)
        for TIME in data[subj].keys():
            for exper in data[subj][TIME].keys():
                if exper == 'novelty' and subj not in hasNov: hasNov.append(subj)
                if exper == 'nback' and subj not in hasNBack: hasNBack.append(subj)

    qualify = [hasAll,hasPre,hasPost,hasErr,hasNov,hasNBack]
    labels = ['hasAll','hasPre','hasPost','hasErr','hasNov','hasNBack']
    return qualify, labels
    