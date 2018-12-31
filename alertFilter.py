from TimeStamp import TimeStamp

def alertsHaveSameIP(alert,compareAlert):
    result = (alert['srcIp'] == compareAlert['srcIp'] or alert['srcIp'] == compareAlert['destIp']) 
    result = result and (alert['destIp'] == compareAlert['destIp'] or alert['destIp'] == compareAlert['srcIp'])
    return result

def similarToAlert(alert, alertArray):
    for compareAlert in alertArray:
        if alert['signature'] == compareAlert['signature'] and alertsHaveSameIP(alert,compareAlert):
            ts1 = TimeStamp()
            ts1.setFromSnort(alert['date'])
            ts2 = TimeStamp()
            ts2.setFromSnort(compareAlert['date'])
            return ts1.compareTimeStamp(ts2,15)#TODO extract variable to config

def addPortsToResult(alert,result):
    for compareAlert in result:
        if alert['signature'] == compareAlert['signature'] and alertsHaveSameIP(alert,compareAlert):
            ts1 = TimeStamp()
            ts1.setFromSnort(alert['date'])
            ts2 = TimeStamp()
            ts2.setFromSnort(compareAlert['date'])
            if ts1.compareTimeStamp(ts2,15):
                compareAlert['srcPorts'].append(alert['srcPort'])
                compareAlert['destPorts'].append(alert['destPort'])
                


def filterAlerts(snortAlertObject):
    result = []
    for alert in snortAlertObject:
        if not similarToAlert(alert,result) and int(alert['priority']) < 3: #TODO extract variable to config
            alert['destPorts'] = []
            alert['destPorts'].append(alert['destPort'])
            alert['srcPorts'] = []
            alert['srcPorts'].append(alert['srcPort'])
            result.append(alert)
        else:
            addPortsToResult(alert,result)
    return result