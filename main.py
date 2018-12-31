debug = True
import sys
from readBro import readBroLogs 
from readSnortAlert import readAlertFile
from filterAndLogics import filterAndLogics
from alertFilter import filterAlerts




def getArgument(argumentNumber, argumentDefinition):
    if len(sys.argv)< (argumentNumber +1):
        argumentContent = input("Please input "+argumentDefinition+": ")
    else:
        argumentContent = sys.argv[argumentNumber]
    print("INFO: " + argumentDefinition +" set to: " + argumentContent)
    return argumentContent

def main(): #error handling
    #reading arguments
    broLogLocation = getArgument(1, "Bro log folder location")
    snortAlertFileLocation = getArgument(2, "path to Snort alert file")
    outputFolder = getArgument(3, "path to output folder")
    #interpret input files
    try:
        broLogsObject = readBroLogs(broLogLocation)
        print("SUCCES: interpreted "+str(len(broLogsObject))+" Bro logs")
    except WindowsError:
        print("ERROR: cannot find the bro log path")
    except IOError:
        print("ERROR: Can not open Bro Log file.")
    except IndexError:
        print("ERROR: broLog file doesn't follow standart")

    try:
        snortAlertObject = readAlertFile(snortAlertFileLocation)
        print("SUCCES: interpreted "+str(len(snortAlertObject))+" Snort alerts")
    except IOError:
        print("ERROR: Can not open Snort alert file")  

    # filtering and logics
    try:
        filterAndLogics(broLogsObject,snortAlertObject,outputFolder)
        print("SUCCES: filtered input")
    except UnboundLocalError:
        print("ERROR: Can not filter without all objects")
    except KeyError:
        print("ERROR: Objects created from logs are the wrong format")

    # output to file

def debugger(): #error handling
    broLogLocation = getArgument(1, "Bro log folder location")
    snortAlertFileLocation = getArgument(2, "path to Snort alert file")
    outputFolder = getArgument(3, "path to output folder")
    broLogsObject = readBroLogs(broLogLocation)
    print("SUCCES: interpreted "+str(len(broLogsObject))+" Bro logs")
    snortAlertObject = readAlertFile(snortAlertFileLocation)
    print("SUCCES: interpreted "+str(len(snortAlertObject))+" Snort alerts")
    #print(broLogsObject)
    #print(snortAlertObject)

    snortAlertObject = filterAlerts(snortAlertObject)
    print("SUCCES: Filtered duplicate alerts, "+ str(len(snortAlertObject)) + " alerts left")

    filterAndLogics(broLogsObject,snortAlertObject,outputFolder)
    print("SUCCES: filtered input")

    


if __name__ == '__main__':
    if debug:
        debugger()
    else:
        main()