import os

def readAlertFile(alertFileLocation):
    alertFile = open(alertFileLocation,"r")
    counter = 0
    alert= {}
    allAlerts = []
    for line in alertFile.readlines():
        words = line.split()
        if len(line.strip()) != 0:
            if counter == 0:
                nummerTussenBrackets = line.split('[', 1)[1].split(']')[1].split(' [')[1]
                titelEersteLijn = line.split('] ')[2].split(' [')[0]
                alert['weirdnumber']=nummerTussenBrackets
                alert['title']=titelEersteLijn
            if counter == 1:
                val = line.split('[', 1)[1].split(']')[0]
                valPriority = line.split('[', 1)[1].split(']')[1].split("[")[1]
                if ":" in valPriority:  
                    alert['priority']=valPriority.split(": ")[1] 
                if ":" in val:  
                    alert['classification']=val.split(": ")[1] 
            if counter == 2:
                for x in range(0, len(words)):
                    currentTextBlob = line.split(None, x + 1)[x]
                    if "->" not in currentTextBlob:
                        if x == 0:                        
                            alert['date'] = line.split(" ")[x]
                        elif x == 1:           
                            alert['srcPort'] = currentTextBlob.split(":")[1]
                            alert['srcIp'] = currentTextBlob.split(":")[0]
                        elif x == 3:
                            alert['destPort'] = currentTextBlob.split(":")[1]
                            alert['destIp'] = currentTextBlob.split(":")[0]
            if counter == 3:  # als het de 3e lijn is moet je dit doen
                for x in range(0, len(words)):
                    currentTextBlob = line.split(None, x + 1)[x]
                    if ":" in currentTextBlob:  # als er geen : staat moet je dit doen
                        
                        alert[currentTextBlob.split(":")[0]] = currentTextBlob.split(":")[1]
                    #else:  # voor protecol

            counter += 1
        else:
            # hier begin je een nieuw object
            allAlerts.append(alert)
            alert= {}
            counter=0
    return allAlerts
