#for sage
oname = 'results.csv';oename = 'error.csv';osname = 'settings.csv'
nBackConvertResponseCodes =  {1:'Correct-Hit', 2: 'Correct-NoResponse', 3:'Incorrect-FalseAlarm', \
                             4:'Incorrect-NoResponse', 5:'Incorrect-TooEarly', 6:'Incorrect-TooLate'}
novConversionResponseCodes = {1:'Correct-Hit',  2:'Correct-NoResponse', 3:'Incorrect-FalseAlarm', \
                             4:'Incorrect-NoResponse', 5:'Incorrect-EarlyLate'}
#                     [[name,           find,               dnf, dnf]]
noveltySearchTerms =  [['Stim Code',    'ItemCode',         'xxx','xxx'],       \
                      ['Resp Code',     'ResponseTypeMouse','xxx','xxx'],       \
                      ['React Time',    'RT',               'RTTime', '_RT'],   \
                      ['Mouse RT',      '_RT',              'xxx','xxx']]
nBackSearchTerms =    [['Stim Code',    'ItemCode',         'xxx','xxx'],       \
                      ['Resp Code',     'ResponseType',     'xxx','xxx'],       \
                      ['Resp Code2',    'RESP',             'CRESP','xxx'],     \
                      ['Accuracy',      'ACC',              'xxx','xxx'],       \
                      ['RT',            'RT',               'RTTime', 'xxx']]
searchLists = [['PRE'],['POST']]


#for subjectSearch
extension = '.txt'
omitList = ['READ'] 