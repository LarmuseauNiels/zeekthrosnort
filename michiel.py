#file moet in C:/Users/michiel.jonkmans/PycharmProjects/untitled staan




# f = open('Logs/dns.log','rt')
# content = f.read()
# f.close()
# print(content)

#-------------------------------------------------------------
#Filteren en naar file schrijven van 1 log file die je kan uitlezen

# infile = r"dns.log"
# f1= open("Alerts.log","w+")
# important = []
# keep_phrases = ["2.1.168.192.in-addr.arpa",
#               "ml.buymeaslut.com",
#               "44720"]
#
# with open(infile) as f:
#     f = f.readlines()
#
# for line in f:
#     for phrase in keep_phrases:
#         if phrase in line:
#             f1.write(line)
#             break

#-------------------------------------------------------------

import os
location = os.getcwd()
f1= open("Alerts.log","w+")
keep_phrases = ["1492355944.546234"]
for file in os.listdir(location):
    if file.endswith(".log"):
        with open(file) as f:
            f = f.readlines()
        f1.write("---------------------------------------"+"\n"+str(file)+"\n"+"---------------------------------------"+"\n")
        for line in f:
            for phrase in keep_phrases:
                if phrase in line:
                    f1.write(line)
                    break

#-------------------------------------------------------------
#Kijken welke .log files er in je working directory staan met location = working dorectory

# import os #os module imported here
# location = os.getcwd() # get present working directory location here
# counter = 0 #keep a count of all files found
# csvfiles = [] #list to store all csv files found at location
# filebeginwithhello = [] # list to keep all files that begin with 'hello'
# otherfiles = [] #list to keep any other file that do not match the criteria
#
# for file in os.listdir(location):
#     try:
#         if file.endswith(".log"):
#             print("log file found:\t", file)
#             csvfiles.append(str(file))
#             counter = counter+1
#
#         elif file.startswith("hello") and file.endswith(".csv"): #because some files may start with hello and also be a csv file
#             print("csv file found:\t", file)
#             csvfiles.append(str(file))
#             counter = counter+1
#
#         elif file.startswith("hello"):
#             print("hello files found: \t", file)
#             filebeginwithhello.append(file)
#             counter = counter+1
#
#         else:
#             otherfiles.append(file)
#             counter = counter+1
#     except Exception as e:
#         raise e
#         print ("No files found here!")
#
# print ("Total files found:\t", counter)