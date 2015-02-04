'''
Created on Jan 24, 2015

@author: Michael
'''

def makeSearches(theSearch):
    lists = []
    for search in theSearch:
        listt = []
        if search.find(':') > -1:    #if it is a range
            beginning,end = search.split(':')
            current = int(beginning)
            while current <= int(end):
                listt.append(current)
                current += 1
            lists.append(listt)
        else: lists.append(theSearch)
    return lists



def distributeSearches(path):
    #open path and generate list of search arrays with row name to be used in CSV output
    newSearchFile = []
    try:
        with open(path) as search:
            searchNumber = 0
            for line in search:
                rowHeader,rowEntry = line.strip().split(':',1)
                firstSearches,secondSearches = rowEntry.split()
                firstSearches = firstSearches.strip('[').strip(']'); secondSearches = secondSearches.strip('[').strip(']')
                firstSearches = firstSearches.split(','); secondSearches = secondSearches.split(',')
                        
                firstSearches = makeSearches(firstSearches); secondSearches = makeSearches(secondSearches) 
        
                pairs = []
                for oneSearchList in firstSearches:
                    for oneSearch in oneSearchList:
                        for anotherOneSearchList in secondSearches:
                            for anotherOneSearch in anotherOneSearchList:
                                pair = int(oneSearch), int(anotherOneSearch)
                                pairs.append( pair )
                newSearchFile.append([rowHeader, pairs, searchNumber])
                searchNumber += 1
        return newSearchFile
    except: print'Search File Not Accepted (ofSearches/searchFormat/distributeSearches)'; quit()

def makeSearch1D(searchList):
    searches = []
    for i in searchList: 
        for j in i[1]:
            print j
            searches += [[i[0],j,i[-1]]]    #compound list of searches to one array
            print searches
            if j[1] == 2: searches += [[i[0],(j[0],4),i[-1]]]
            if j[1] == 1:searches += [[i[0],(j[0],3),i[-1]]]
            if j[1] == 4:searches += [[i[0],(j[0],2),i[-1]]]
            if j[1] == 3:searches += [[i[0],(j[0],1),i[-1]]]
            print searches
    return searches   
