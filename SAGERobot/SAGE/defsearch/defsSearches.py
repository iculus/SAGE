'''
Created on Jan 14, 2015

@author: Michael
'''

def getVarsOfInteret(whichSearchTerms, theData):
    #generate empty list of lists equivalent to number of definitions for exper type
    elist = []
    for index in whichSearchTerms:
        eset = []
        elist.append(eset)
    
    #cycle through every block and trial and find the search terms, then return a list of lists of values 
    block = 0
    while block < len(theData):              
        for index, searchTerm in enumerate(whichSearchTerms):   #iterate through each serchTerm for this experiment
            #block set is universe
            lookTracker = []
            
            trial = 0
            #maybe add a function here to accept trial requests
            while trial < len(theData[block]):
                #trial set is universe
                trialDict = {}  #dictionary for one loop through one trial should be created or replaced over the next few lines    
                for trialDat in theData[block][trial]:
                    if trialDat.find(':') > -1:   #when the : is found in the string(line of brain file) that for whatever reason is element 1 of the 
                        a,b=trialDat.replace('\t\t', '').split(':') # make two strings split at the :
                        #print a, '::', b    #temporary print two strings separated by funky character
                        
                        trialDict[a] = b    #set value for key
                
                title = searchTerm[0]; term3 = searchTerm[1]; term4 = searchTerm[2]; term5 = searchTerm[3]
                found = False
                for k in trialDict.keys():
                    if k.find(term3) > -1 and k.find(term4) == -1 and k.find(term5) == -1: 
                        lookTracker.append( trialDict[k].strip(' ') ); found = True
                if found == False: lookTracker.append('null')   
                trial += 1
            #print block, searchTerm[0], lookTracker  
            elist[index] += lookTracker                  
        block += 1
    return elist