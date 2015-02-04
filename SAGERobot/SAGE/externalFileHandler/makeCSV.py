'''
Created on Feb 3, 2015

@author: Michael
'''
import csv

def makeCSVHeader(searches, MASTERFILE):
    #build header of CSV
    row = ['subjName', 'sessionName', 'experName', 'file']
    calcs = ['ratio','mean','median','meanLook','medianLook']
    for i in searches: 
        for j in calcs:
            row += [[i[0], i[1], j]]
    MASTERFILE.append(row)
    return MASTERFILE

def writeCSV(p,e,o,toWrite): 
    path = p + '/' + e + o
    with open(path, 'wb') as csvFile:
        writefunc = csv.writer(csvFile, delimiter='^', quotechar = '|', quoting=csv.QUOTE_MINIMAL)
        if len(toWrite) > 0:
            for i in toWrite: 
                writefunc.writerow( i )
        else: writefunc.writerow('nothing to record')
    return path