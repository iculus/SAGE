'''
Created on Dec 10, 2014

@author: Michael
'''

#open file, read contents to list, close file
def openFile(filename):
    tempFileLoc = []
    try: 
        with open(filename, 'r') as fileO:
            for line in fileO:
                line2 = (line.\
                                   replace('\xff', '')\
                                   .replace('\xfe', '')\
                                   .replace('\x00', '')\
                                   .replace('\n', '')\
                                   .replace('\r', '')\
                                   )
                tempFileLoc.append(line2.rstrip())  #to remove end of line whitespace
                
        fileO.close()
    except: 
        print 'Something did not work while cleaning in external file handler file open task'
    return tempFileLoc

#test = openFile('D:/Dropbox/BWH2/Data/ERP/12TK/PRE/nback/1-backA_L-12-1.txt')
testbroke = openFile('D:/Dropbox/BWH2/Data/ERP/12TK/PRE/nback/2-backA_L-12-1.txt')
