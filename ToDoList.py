#new ideas, to do list maker


class DaySchedule:
    timeTable = {}
    def __init__(self):
        timeTable = {i: '' for i in range(900, 2100, 10)}
        self.timeTable = timeTable
    def addEvent(self ,timeBegins, timeEnds, eventName):
        for i in range(900, 2110, 10):
            if (i >= timeBegins and i <= timeEnds):
                if self.timeTable[i] is '':
                    self.timeTable[i] = eventName
                else:
                    while i >= timeBegins:
                        self.timeTable[i] = ''
                        i-=10
                    print('Error: Time Conflict')
                    break
    def getTimeTable(self):
        return self.timeTable


table = DaySchedule()
table.__init__()
#debug print(str(table.getTimeTable()))
table.addEvent(1000, 1200, 'Class')
table.addEvent(900, 1300, 'Conflct')
print(table.getTimeTable())
    
             
