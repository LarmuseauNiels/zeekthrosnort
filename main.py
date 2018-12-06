import sys
from readBro import readBroLogs 
from readSnortAlert import readAlertFile
from filterAndLogics import filterAndLogics

def outputToFile(outputFile, output):
    file = open(outputFile,"w") 
    file.write(output) 
    file.close()


def getArgument(argumentNumber, argumentDefinition):
    if len(sys.argv)< (argumentNumber +1):
        argumentContent = input("Please input "+argumentDefinition+": ")
    else:
        argumentContent = sys.argv[argumentNumber]
    print(argumentDefinition +" set to: " + argumentContent)
    return argumentContent

def main(): # first function executed on run of script
    #reading arguments
    broLogLocation = getArgument(1, "Bro log folder location")
    snortAlertFileLocation = getArgument(2, "path to Snort alert file")
    outputFile = getArgument(3, "path to output file")
    #interpret input files
    try:
        broLogsObject = readBroLogs(broLogLocation)
        print("succesfully interpreted "+str(len(broLogsObject))+" Bro logs")
    except WindowsError:
        print("ERROR: cannot find the bro log path")
    except IOError:
        print("ERROR: Can not open Bro Log file.")
    try:
        snortAlertObject = readAlertFile(snortAlertFileLocation)
        print("succesfully interpreted "+str(len(snortAlertObject))+" Snort alerts")
    except IOError:
        print("ERROR: Can not open Snort alert file")  
    #debugging options:

    #print(broLogsObject)
    #print(snortAlertObject)
    
    # filtering and logics
    output = filterAndLogics(broLogsObject,snortAlertObject)#TODO

    # output to file
    outputToFile(outputFile, output)

if __name__ == '__main__':
    main()