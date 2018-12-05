import os

def readBroLog(log):
    logFields = []
    broPackets = []
    for line in log:
        broPacket = {}
        if line.startswith("#fields"):
            logFields = line.split('\t')
            del logFields[0]
            logFields[len(logFields) -1] = logFields[len(logFields) -1].strip("\n") 
        if not(line.startswith("#")):
            logValues = line.split('\t')
            for i in range(0, (len(logFields) -1)) :
                broPacket[logFields[i]] = logValues[i]
            broPackets.append(broPacket)
    return (broPackets)
                        
def readBroLogs(broLogsLocation):
    broLogsAsObjects = {}
    for file in os.listdir(broLogsLocation):
        if file.endswith(".log"):
            with open(broLogsLocation + "/" + file) as f:
                broLogsAsObjects[(file.strip('.log'))] = (readBroLog(f))
    return broLogsAsObjects
