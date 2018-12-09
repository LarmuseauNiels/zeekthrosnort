from datetime import *

def timeConvertTimeStampFromUnix(input):
    dt = datetime.fromtimestamp(int(round(float(input)))) 
    return {"month": dt.month, "day": dt.day, "hour": dt.hour}
    print(str(dt.month) )

    
def filterAndLogics(broLogsObject,snortAlertObject):
    
    output = str(broLogsObject) + " Snort Alert: " + str(snortAlertObject)
    #DEBUGGING
    timeConvertTimeStampFromUnix(broLogsObject["conn"][0]['ts'])
    #print(broLogsObject)

  
    print(broLogsObject["conn"][0])


    return output