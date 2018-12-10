from TimeStamp import TimeStamp

def filterAndLogics(broLogsObject,snortAlertObject):
    
    output = str(broLogsObject) + " Snort Alert: " + str(snortAlertObject)
    #DEBUGGING
    timestamp1 = TimeStamp()
    timestamp1.setFromUnix(1492363369)#broLogsObject["conn"][0]['ts']
    print(int(round(float(1492363369))))
    timestamp2 = TimeStamp()
    timestamp2.setFromSnort(snortAlertObject[0]['date'])
    
    
    print(timestamp1.toString())
    print(timestamp2.toString())
    print(timestamp2.getSecDistance(timestamp1))



  
    print(snortAlertObject)


    return output