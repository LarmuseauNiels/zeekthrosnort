import sys
from readBro import readBroLogs 
from readSnortAlert import readAlertFile

def getArgument(argumentNumber, argumentDefinition):
    if len(sys.argv)< (argumentNumber +1):
        argumentContent = raw_input("Please input "+argumentDefinition+": ")
    else:
        argumentContent = sys.argv[argumentNumber]
    print(argumentDefinition +" set to: " + argumentContent)
    return argumentContent

def main(): # first function executed on run of script
    broLogLocation = getArgument(1, "Bro log location")
    snortAlertFileLocation =  getArgument(2, "path to Snort alert file")
    try:
        broLogsObject = readBroLogs(broLogLocation)
    except WindowsError:
        print("ERROR: cannot find the bro log path")
    except IOError:
        print("ERROR: Can not open Bro Log file.")
    try:
        snortAlertObject = readAlertFile(snortAlertFileLocation)
    except IOError:
        print("ERROR: Can not open Snort alert file")  
    #Debugging
    #print(broLogsObject)
    #print(snortAlertObject)
    

if __name__ == '__main__':
    main()