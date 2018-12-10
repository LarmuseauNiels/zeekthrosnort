from datetime import *

class TimeStamp:
    month =  0
    day = 0
    hour = 0
    minit = 0
    sec = 0
    #def compare(timestamp, margininsec):
        
    def setFromUnix(self, unix):
        dt = datetime.fromtimestamp(int(round(float(unix)))) 
        self.month = dt.month
        self.day = dt.day
        self.hour = dt.hour
        self.minit =  dt.minute
        self.sec = dt.second

    def setFromSnort(self, snort):
        firstsplit = snort.split("-")
        date = firstsplit[0].split("/")
        time = firstsplit[1].split(":")
        self.month = int(date[0])
        self.day = int(date[1])
        self.hour = int(time[0])
        self.minit = int(time[1])
        self.sec = int(round(float(time[2])))
        
    def calcseconds(self ):
        return ((self.month * 2629800) + (self.day*86400 )+ (self.hour*3600)+(self.minit*60)+self.sec)

    def getSecDistance(self, otherTimeStamp):
        return abs(self.calcseconds() - otherTimeStamp.calcseconds())

    def compareTimeStamp(self, otherTimeStamp, margininseconds):
        return (self.getSecDistance(otherTimeStamp) < margininseconds )

    def toString(self):
        return (str(self.month) + " / " + str(self.day) + "-" + str(self.hour) + ":" + str(self.minit) +":"+ str(self.sec))