'''
Created on Dec 14, 2014

@author: Michael
'''

def begEnd(chunk):
    lastIndex = -2
    inchunkRange = True
    chunkRange = []
    for i in chunk:
        if i == lastIndex+1:
            if inchunkRange == False:
                chunkRange.append( lastIndex )
            inchunkRange = True
            
        else:
            inchunkRange = False
            if lastIndex >= 0: chunkRange.append( lastIndex )
        lastIndex = i
    chunkRange.append( chunk[-1] )
    return chunkRange

def makePairs(unpairedList):
    index = 0
    listPairs = []
    while index < len(unpairedList):
        try:
            pairs = (unpairedList[index],unpairedList[index+1])
            listPairs.append(pairs)
            index += 2
        except: print index, listPairs, unpairedList, quit()
    return listPairs

def findHeaders(data):  
    headerList = []
    for index, line in enumerate (data):
        if line.find('\t') == -1:
            headerList.append(index)
    startEnd = begEnd(headerList)
    startEndPairs = makePairs(startEnd)
    return startEndPairs


def findBlocks(data):
    blockList = []
    for index, line in enumerate (data):
        if line.find('\t') > -1 and line.find('\t\t') == -1:
            blockList.append(index)
    blockStartEnd = begEnd(blockList)
    blockStartEndPairs = makePairs(blockStartEnd)
    return blockStartEndPairs

def findTrials(data):
    trialList = []
    for index, line in enumerate (data):
        if line.find('\t\t') > -1:
            trialList.append(index)
    trialStartEnd = begEnd(trialList)
    trialStartEndPairs = makePairs(trialStartEnd)
    listBlockTrialData = []
    for block, pair in enumerate(trialStartEndPairs):
        trialNum = 0
        blockStart = pair[0]; blockEnd = pair[1];
        recording = False
        here = blockStart
        trialsThisBlock = []
        while here <= blockEnd:

            if data[here].find('*** LogFrame Start ***') > -1: 
                recording = True
                trialNum += 1
                trialData = []
            if data[here].find('*** LogFrame End ***') > -1: 
                recording = False
                trialsThisBlock.append(trialData)
            
            if recording == True:
                trialData.append(data[here])
            here += 1
        
        listBlockTrialData.append(trialsThisBlock)
        #for i in trialsThisBlock: print i     #if uncommented will show every trial element

    return listBlockTrialData
        
    

def findParts(inputF):  
    #generates list of header and footer range, then list of block intermission range, then makes looks at remaining chunks as blocks and finds trials based on logfrme search      
    HFSE = findHeaders(inputF)
    BSE = findBlocks(inputF)
    nestedList = findTrials(inputF) #USE: nestedList[block][trial]
    return HFSE, BSE, nestedList

def buildTree(classification, labels, table, dictionary):
    #acquire appropriate subject list
    testCase = 0
    testState = False
    for index, test in enumerate(labels):
        if test == classification:
            testCase = index
            testState = True
    if testState == False: print 'test state error'
    #build tree
    treeDict = {}
    for subject in table[testCase]:
        experDict = {}
        for times in dictionary[subject].keys():
            for exper in dictionary[subject][times].keys():
                experDict.setdefault(times, [])
                experDict[times].append(exper)
        treeDict.setdefault(subject, [])
        treeDict[subject].append(experDict)
    return treeDict

def findFolders(dictionary):
    #find the folders that actually exist
    args = []
    #REMOVE BEFORE FLIGHT
    
    #ask user for subjects and build list of argv if any, else add all to list and repopulate 
    # returns {'subj': [{'time': ['exper1', 'exper2(if pres)'], 'time2': ['exper1', 'exper2(if)']}] from list hasAll
    for subj in dictionary.keys():
        for key in dictionary[subj]:
            for TIME in key.keys():
                for exper in dictionary[subj][0][TIME]:
                    args.append([subj, TIME, exper])
    return args

