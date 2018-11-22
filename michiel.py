class Alert(object):
    id = ""
    title = ""
    priority = 0
    classification = ""
    date=""
    srcIp=""
    srcPort=""
    destIp=""
    destPort=""
    
    # michiel

    Protocol=""
    TTL=""
    TOS=""
    PackedID=""
    IpLen=0
    DgmLen=0
    Seq=""
    Ack=""
    Win=""
    TcpLen=0

    def __init__():
        
                
    


import os

homeDir = os.environ['HOME']
snortAlertLocation = homeDir + '/Documents/Zeektrhusnortlogs/eternalblue_output/snort/alert'
snortAlertFile = open(snortAlertLocation,"r")

def readAlertFile(alertFile):
    for line in alertFile.readlines():
         if len(line.strip()) != 0:
         #
        else:
            #hier begin je een nieuw object
            break

readAlertFile(snortAlertFile)