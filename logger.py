#Efficiency Tip:
# from test.test_import import PycRewritingTests
# every time you write something to a csv, it deletes everything in the csv, because of this, in order to log 
# something you must first record everything already in the csv, then write everything that used to be in the
# csv plus what you are trying to log.  If you are dealing with a csv with a lot of data, recording then re-writing 
# it all will take a lot of time.  Because of this, the most efficient way to do logging is to build up a big list
# of all the data you want to log, then logging it all at once.  Therefore you should try to always use
# logList() instead of logSingle() 

import csv
import os.path
import os

# use this to get path
# import os
#   
# full_path = os.path.realpath(__file__)
# csvPath =  os.path.dirname(full_path) + '\\NEW_CSV_MADE_BY_LOGGER.csv'

#------------------------------------------------------PUBLIC------------------------------------------------------#

#logs a list of dicts, each dict = one row, dict = {columb header: data}
#ex:
# tweetLogDictList = [{'Time/Date': '11:34pm on monday',
#                      'User_Name': '@bob',     
#                      'Tweet':     'my name is bob and this is a test'},
#                     
#                     {'Time/Date': '12:35pm on tuesday',
#                      'User_Name': '@jill',     
#                      'Tweet':     'my name is jill and im the worst'}]
def logList(dataDictList, csvPath, wantBackup = True, headerList = None, overwriteAction = 'append'):       
    csvData = buildCSVdata(dataDictList, csvPath, wantBackup, overwriteAction)
        
    write2CSV(csvData, csvPath, headerList)       


#should try not to use much, its not very efficient, same thing as logList() but one dict at a time
#ex:
# tweetLogDict = {'Time/Date': '11:47pm on saterday',
#                 'User_Name': '@sagman',     
#                 'Tweet':     'my name is sagman bardlileriownoaosnfo'}


def logSingle(dataDict, csvPath, wantBackup = True, headerList = None, overwriteAction = 'append'):
    csvData = buildCSVdata(dataDict, csvPath, wantBackup, overwriteAction)
           
    write2CSV(csvData, csvPath, headerList) 


#returns a list of dicts
#each element of the list is dict with entries like {header_name: data}
def readCSV(csvPath):
    dataDictList = []
    
    with open(csvPath, 'rt', encoding='utf8') as csvfile:
        csvReader = csv.DictReader(csvfile)
             
        for row in csvReader:
            rowDict = {}
            for header in csvReader.fieldnames:         
                #convert string to dict
                dataStr = row[header]
                rowDict[header] = dataStr
                #headerDataDict = ast.literal_eval(headerdataStr)   
            dataDictList.append(rowDict)              
    return dataDictList


def write2CSV(logDictList, csvPath, headerList = None):
    # if headerList == None, then fieldnames will be in a random order
    fieldnames = []
    if headerList == None:
        for header, data in logDictList[0].items():
            fieldnames.append(header)
    else:
        fieldnames = headerList
    
    with open(csvPath, 'wt', encoding='utf8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, lineterminator = '\n')
        writer.writeheader()
         
        #build rowDictList
        rowDictList = []
        rdlPos = 0
        for logDict in logDictList:
            for header, data in logDict.items():
                                     
                if rowDictList == [] or rdlPos > (len(rowDictList) - 1):
                    rowDictList.append({})
                rowDictList[rdlPos][header] = data
            rdlPos +=1
        #write rows
        for rowDict in rowDictList:
            try:
                writer.writerow(rowDict)
            except Exception as e:
                raise TypeError('ERROR:  HeaderList does not match headers in dataDict, probably misspelled or forgot to add key:  ' + str(e))
 
    csvfile.close()
       

def backup(csvData, csvPath):
    backupCount = 0
    sp = csvPath.split(".")
    backupPath = sp[0] + '_BACKUP_' + str(backupCount) + '.' + sp[1]
    
    while(os.path.isfile(backupPath)):
        backupCount += 1
        backupPath = sp[0] + '_BACKUP_' + str(backupCount) + '.' + sp[1]
    
    write2CSV(csvData, backupPath)
              
              
def formatsMatch(dataDict, csvData):
    #if the csv is empty, no need for a backup
    if csvData == []:
        return True
    
    for header, data in dataDict.items():
        if header not in csvData[0]:
            return False
        
    for header in csvData[0]:
        if header not in dataDict.keys():
            return False
        
    return True


#make sure data wont cause a unicode error - not efficient!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def encodeDataDict(dataDict):         
    for key, data in dataDict.items():
        if type(data) == str:
            data = data.encode('ascii', 'ignore')
    return dataDict        


def buildCSVdata(dataContainer, csvPath, wantBackup, overwriteAction):
    #dataContainer can be dataDictList for logList or dataDict for logSingle
    if   type(dataContainer) is list:
        logType = 'list'
    elif type(dataContainer) is dict:
        logType = 'single'
    
    
    if logType == 'list':
        dataDict = dataContainer[0]
    else:
        dataDict = dataContainer
        
    #check if file already exists, if not, make it
    try:#try is safer than isfile()
        #read the csv into a list of dicts (one dict for each row) 
        csvData = readCSV(csvPath)  
        
        
        #check to make sure the csv's fieldnames matches the headerList, if not, create backup before overwriting
        if not formatsMatch(dataDict, csvData):
            if wantBackup == True:
                backup(csvData, csvPath)
            csvData = []     
            
        if overwriteAction == 'overwrite':
            csvData = []
            
    except:
        csvData = []
        
        
    #encode data
    if logType == 'list':
        for dataDict in dataContainer:
            csvData.append(encodeDataDict(dataDict))
    else:
        csvData.append(encodeDataDict(dataContainer))
    
    return csvData







# print('TESTING IN LOGGER...')
# full_path = os.path.realpath(__file__)
# csvPath =  os.path.dirname(full_path) + '\\tweet_log.csv' 
# 
# wantBackup = True
# 
# headerList = ['Time/Date', 'User_Name', 'Tweet']
#  
# tweetLogDict = {'Time/Date': '11:47pm on saterday',
#                 'User_Name': '@sagmanblablatest3',     
#                 'Tweet'    : 'my name is sagman'}
#   
# tweetLogDictList = [{'Time/Date': '11:34pm on monday',
#                      'User_Name': '@bob',     
#                      'Tweet':     'my name is bob and this is a test'},
#                       
#                     {'Time/Date': '12:35pm on tuesday',
#                      'User_Name': '@jill',     
#                      'Tweet':     'my name is jill and im the worst'}] 
#            
# # logList(tweetLogDictList, csvPath, wantBackup, headerList, 'overwrite')         
# logSingle(tweetLogDict, csvPath, wantBackup, headerList)
# print('DONE TESTING IN LOGGER')

          
#         
        