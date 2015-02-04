'''
Created on Jan 16, 2015

@author: Michael
'''
def calculRatio(listOne, listTwo):
    denom = len(listOne)
    numerat = len(listTwo)
    if denom > 0: ratio = float(numerat)/denom
    else: ratio = 0
    return ratio

def calculMean(checkThese, setToTest):
    testList = []
    for value in checkThese: 
        if setToTest[value] == 'null': setToTest[value] = 0
        testList.append(int(setToTest[value]))
    numerat = float(sum(testList)); denom = float(len(testList))
    if denom > 0: mean = numerat/denom
    if denom == 0: mean = 0
    return testList, mean

def calculMedian(listToCalc):
    if len(listToCalc)%2 == 1 and len(listToCalc) > 0: MEDIAN = sorted(listToCalc)[len(listToCalc)/2]
    elif len(listToCalc)%2 == 0 and len(listToCalc) > 0: MEDIAN = ( sorted(listToCalc)[len(listToCalc)/2-1] + sorted(listToCalc)[len(listToCalc)/2 ])/2
    else: MEDIAN = 0
    return MEDIAN         

def doCalcs(nameE,varList, foundList, foundListTwice):
    rtVar = varList[-1]; rtLookVar = varList[-2]
    #calc Ratio
    ratio = calculRatio(foundList, foundListTwice)#; print 'RATIO', ratio,
    if nameE == 'nback':
        #calc meanRT
        meanRTList, meanRT = calculMean(foundListTwice, rtVar)#; print 'MEAN nback:', meanRT,
        #calc medianRT
        median = calculMedian(meanRTList)#; print 'MEDIAN nback:', median
        #b/c this field should be empty for this experiment
        meanRTLook = 'null'; medianLook = 'null'
    #calculate extra for novelty
    #mouse rt and mean and media look time
    if nameE == 'novelty':
        #MOUSE calc meanRT
        meanRTList, meanRT = calculMean(foundListTwice, rtVar)#; print 'MEAN nov mouse:', meanRT,
        #MOUSE calc medianRT
        median = calculMedian(meanRTList)#; print 'MEDIAN nov mouse:', median,
        #LOOK calc meanRT
        meanRTList, meanRTLook = calculMean(foundListTwice, rtLookVar)#; print 'MEAN look:', meanRTLook,
        #LOOK calc medianRT
        medianLook = calculMedian(meanRTList)#; print 'MEDIAN look:', medianLook
    return ratio, meanRT,median,meanRTLook,medianLook,               