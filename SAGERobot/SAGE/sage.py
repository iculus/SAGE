'''
Created on Dec 5, 2014

@author: Michael
'''

#REMOVE BEFORE FLIGHT
SearchPath = 'D:\Dropbox\BWH2\inputs'
#SearchPath = 'Z:\ERPLAB\!!Daffner_Lab!!'
'''
print 'Show Erich and Annie defSearch/defsSearches/42, then rename that module'
from time import sleep; 
for k in range(10): print 10-k,; sleep(1);
print '\n'
'''
#REMOVE BEFORE FLIGHT

print 'Importing libraries'
import sys
import manageRawInput as S
import externalFileHandler as EFH
import findSubjects as FS
import defsearch as D
import calculations as Ca
import gc
from storeDefinitionsHere\
    import searchLists,oname,oename,\
    osname,novConversionResponseCodes,\
    nBackConvertResponseCodes,\
    nBackSearchTerms,noveltySearchTerms

if 'load' in sys.argv: LoadSaved = True
elif 'dontload' in sys.argv: LoadSaved = False
else: print 'please specify load or dontload in command line'; quit()

path,DataPath,OutPath = EFH.getDirectoriesForSaving(LoadSaved, SearchPath)  #get path info from efh/safsp

#build dictionary of subjects with path to txt files and check for and remove duplicates
print 'Building Subject Dictionary'
subjDict = FS.collectSubjectsInList(DataPath) #output is dictionary of {'subj': {'time': {'exper': ['path 1',.. , 'path n']
lookupTable, LTLabels = FS.qualifySubjects(subjDict) #output is listOtables of related subjects by category and list of categories 
treeDictionary = S.buildTree('hasAll', LTLabels, lookupTable, subjDict) #should be UI 
arguments = S.findFolders(treeDictionary)
#output is a dict {subjName: {time1: {exper1: {file1: {block1: {trial1: {key: line}}}}}}}
''' to show some testing output:
print 'subjDict\t', subjDict
print 'lookupTable\t', lookupTable
print 'LTLabels\t', LTLabels
print 'treeDictionary(hasAll)\t', treeDictionary
print 'arguments\t', arguments
'''

#Master file setup
MASTERFILE = [];MASTERERROR = [];MASTERSETTINGS = []
MASTERSETTINGS.append(['search file']);MASTERSETTINGS.append([path]);MASTERSETTINGS.append(['searched:'])

#convert search array list into formatted vector list
print 'Evaluating search file'
newSearch = EFH.distributeSearches(path)   #turn search file into search array list  
searches = EFH.makeSearch1D(newSearch)  #turn search array list into 1D list of search vectors

EFH.makeCSVHeader(searches, MASTERFILE) #generates header data specific

#evaluate search type
print 'Evaluating search type'
testNov = False; testNB = False
if path.lower().find('nov') > -1: theseSearchTerms = noveltySearchTerms; testNov = True; convert = novConversionResponseCodes
elif path.lower().find('nback') > -1: theseSearchTerms = nBackSearchTerms; testNB = True; convert = nBackConvertResponseCodes
else: print 'Experiment Not Found:'; quit()
if testNB == True: print 'Experiment: nBack'; eName = 'nback'
if testNov == True: print 'Experiment: novelty'; eName = 'novelty'
if testNB == False and testNov == False: print'Experiment not determined correctly from filename! Check filename, must include \'nov\' or \'nback\', case does not matter'; quit()

#searchThesePeople = ['07PM','11GM']
searchThesePeople = []#23NK
#searchTheseFiles = ['2-backA_L-7-1.txt','1-backA_L-11-1_block1.txt']
searchTheseFiles = []

print 'Starting search'
testSetNov = []
testSetNB = []
for searchList in searchLists: 
    #begin working on each file
    for subjArg in arguments: 
        if subjArg[0] in searchThesePeople or len(searchThesePeople) == 0:
            record = []
            subjName = subjArg[0]; timeName = subjArg[1]; experName = subjArg[2];  
            if timeName in searchList \
            and experName == eName:   #if all three objects in this entry of the list of every set of possible data 
                subjFiles = subjDict[subjName][timeName][experName] #open dictionary to the entry meeting the above requirements
                for oneFile in subjFiles:   #iterate through every relevant file
                    if oneFile.split('\\')[-1] in searchTheseFiles or len(searchTheseFiles)==0: #to run, the last element of the split filename must be in the list
                        print '\t Searching:', subjName, timeName, experName, oneFile
                        record.append([subjName,timeName,experName,oneFile])
                        ###file is universe###
                        #print oneFile   #show me the name of the file
                        data = EFH.openFile(oneFile) #open the file and get rid of extraneous and difficult characters
                        headerRange, blockRange, blockTrialData = S.findParts(data) #run through the functions relating to mapping multiple blocks with multiple trials and create data manageRawInput filled witha list of each trial line in a group trial in a gooup block
                        #blockData is all lines from one file in a list in a group trial in a group block
                        entry = [subjName, timeName, experName, oneFile.split('\\')[-1]] #because it is easy to fill the screen since the last call, print the filter rule again
                        try: varsOfInterest = D.getVarsOfInteret(theseSearchTerms, blockTrialData)   #pass event code definitions based on exper type from SDH to function along with file contents in list form
                        except: print 'ERROR:', subjName, oneFile; MASTERERROR.append([subjName,oneFile])
                        #for index, data in enumerate(varsOfInterest): pass
                        
                        #print searches
                        
                        #Search here
                        searchNumLast = -1  #for averaging function 
                        beginning = True
                        for index, search in enumerate(searches):
                            #print search,
                            #searches[-1] this is search number
                            findThisFirst = search[1][0]
                            findThisSecond = convert[search[1][1]]
                            
                            #print findThisFirst, findThisSecond
                                                        
                            #find instances where first search is true, then second
                            foundList = []
                            for index, value in enumerate(varsOfInterest[0]):
                                if int(value) == int(findThisFirst): foundList.append(index)
                            foundListTwice = []
                            for value in foundList: 
                                if varsOfInterest[1][value].find(findThisSecond) > -1: foundListTwice.append(value)
        
                            ratio,mean,median,meanLook,medianLook = Ca.doCalcs(experName,varsOfInterest, foundList, foundListTwice)
                                                    
                            #print search,findThisFirst,findThisSecond, 'ratio:',ratio,'mean:',mean,'median:',median,'meanLook:',meanLook,'medianLook:',medianLook,
                            entry += [ratio, mean, median ,meanLook, medianLook]
                            #print ratio, mean, median, meanLook, medianLook
                        MASTERFILE.append(entry)
                        #print entry                    
                            
                        ''' here is a segment to display all response codes in a set
                        #to build database of response code possibilities 
                        if testNov == True: testSetNov += varsOfInterest[1] #to see what terms are unique in response codes set of novelty
                        if testNB == True: testSetNB += varsOfInterest[1] #to see what terms are unique in response codes set of novelty
                        print '\n', set(testSetNov), '\n', set(testSetNB) #un-indent this
                        '''
                MASTERSETTINGS.append(record)             

MASTERSETTINGS.append(['subjects available:'])
MASTERSETTINGS.append(arguments)

rPath = EFH.writeCSV(OutPath, eName, oname, MASTERFILE) 
ePath = EFH.writeCSV(OutPath, eName, oename, MASTERERROR) 
sPath = EFH.writeCSV(OutPath, eName, osname, MASTERSETTINGS) 
MASTERSETTINGS.append(['Results File Loc:',rPath])
MASTERSETTINGS.append(['Error File Loc:',ePath])
MASTERSETTINGS.append(['Settings File Loc:',sPath])
       
EFH.writeCSV(OutPath, eName, osname, MASTERSETTINGS)            

print 'CSV Generated!', '\n', len(MASTERFILE), 'Results:', rPath,'\n', len(MASTERERROR), 'Errors:', ePath,'\n Settings', sPath


#import os
#os.system("start "+path)
        
gc.collect()