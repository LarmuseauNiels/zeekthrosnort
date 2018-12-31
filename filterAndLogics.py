import os


def outputToFile(outputFile, output):
    file = open(outputFile, "w")
    file.write(output)
    file.close()


def alertHeader(alert): #titel van de logbestanden die we aanmaken creeren vanuit een snort alert a,d,h,v string functies
    result = '-'*len(alert['title']) + "\n"
    result += alert['title'] + "\n"
    result += '-'*len(alert['title']) + "\n"
    result += str(alert['srcIp']) + ':' + str(alert['srcPort']) + " -> " + str(alert['destIp']) + ':' + str(alert['destPort']) + "\n"
    result += "Classification: " + str(alert['classification']) + "\n"
    result += "Priority: " + str(alert['priority']) + "      Date:" + str(alert['date']) + "\n"
    return result

def broLine(line):
    result = ""
    result +=  "\n" + str(line) + "\n"
    for value in line:
        if not (value == 'ts' or value == 'uid' or value ==  'id.orig_h' or value == 'id.resp_h' or value == 'id.orig_p' or value == 'id.resp_p'):
            if not line[value] == "-":
                result += value +" = " + line[value] + "\n"
        
    return result

def filterAndLogics(broLogsObject, snortAlertObject, outputFolder): #De filters die de snort objecten met de bro logs vergeljken om te kijken welke bro logs matchen met een snort alert
    newpath = outputFolder
    if not os.path.exists(newpath): # folder aanmaken als de folder nog niet bestaat
        os.makedirs(newpath)
    outputForHeaderFile = ""   #variable die uitput header.txt zal uitschrijven per snort alert       
    for idx, alert in enumerate(snortAlertObject): #overlopen snort alerts
        outputforalert = alertHeader(alert)
        manyAlerts = 0 #counter die bijhoud hoeveel bro logs er matchen met een bepaalde alert
        outputForHeaderFile += str(idx) + "  " + alert['title'] +" ( "+ alert['date']+" ) "
        outputforalert += "Other destination ports "+ str(alert['destPorts']) +"\n"
        outputforalert += "Other source prts "+ str(alert['srcPorts']) +"\n"
        for log in broLogsObject:
            try:
                # if log.upper() in alert['title'].upper() or log == "conn":
                #print("found " + str(log.upper()) + " in alert " + str(alert))
                foundsomething = False
                
                for line in broLogsObject[log]: #overlopen brologs
                    snortDest = alert['destIp']
                    snortSrc = alert['srcIp']
                    broDest = line['id.resp_h']
                    broSrc = line['id.orig_h']
                    snortDestPort = alert['destPort']
                    snortScrPort = alert['srcPort']  
                    broDestPort = line['id.resp_p']  
                    broSrcPort = line['id.orig_p']  
                    if (snortDest == broDest or snortDest == broSrc) and (snortSrc == broDest or snortSrc == broSrc): #filter op ip's
                        if (broDestPort in alert['destPorts']  or broDestPort in alert['srcPorts']) and (broSrcPort in alert['destPorts'] or broSrcPort in alert['srcPorts']): #filter op poorten
                            manyAlerts += 1
                        #if (snortDestPort == broDestPort or snortDestPort == broSrcPort) and (snortScrPort == broDestPort or snortScrPort == broSrcPort):
                            if not foundsomething:
                                outputforalert += "\n" + "-"*(10+len(log)) + "\n"
                                outputforalert += " "*5 + str(log) + " "*5 + "\n"
                                outputforalert += "-"*(10+len(log)) + "\n"
                                outputforalert += broLine(line)
                                
                                foundsomething = True
                            else:
                                outputforalert += broLine(line)
            except KeyError:
                pass
        #wegschrijven naar file.
        outputForHeaderFile += "( BroAlerts: "+str(manyAlerts) + " ) \n"
        
        outputToFile(outputFolder+"/"+str(idx)+".txt", outputforalert)
        
        outputToFile(outputFolder+"/header.txt", outputForHeaderFile)

        
