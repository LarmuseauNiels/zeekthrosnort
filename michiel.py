import os

homeDir = os.environ['HOME']
snortAlertLocation = homeDir + '/Documents/Zeektrhusnortlogs/eternalblue_output/snort/alert'
snortAlertFile = open(snortAlertLocation,"r")

def readAlertFile(alertFile):

    counter = 0
    alert= {}
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
                    lol = line.split(None, x + 1)[x]

                    if "->" not in lol:

                        if x == 0:                        
                            alert['date'] = line.split(" ")[x]
                        elif x == 1:           
                            alert['srcPort'] = lol.split(":")[1]
                            alert['srcIp'] = lol.split(":")[0]
                        elif x == 3:
                            alert['destPort'] = lol.split(":")[1]
                            alert['destIp'] = lol.split(":")[0]

            if counter == 3:  # als het de 3e lijn is moet je dit doen
                for x in range(0, len(words)):
                    lol = line.split(None, x + 1)[x]
                    if ":" in lol:  # als er geen : staat moet je dit doen
                        
                        alert[lol.split(":")[0]] = lol.split(":")[1]
                        
                    #else:  # voor protecol

            counter += 1
        else:
            # hier begin je een nieuw object
            counter=0
            

readAlertFile(snortAlertFile)


