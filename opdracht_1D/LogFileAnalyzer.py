__author__ = 'Jacobdb'
from datetime import datetime
LogFilePath = 'D:\logfiledata\epa-http.txt'
import time
OccuranceAantal = int(150)


hosts ={}

LogFile = open(LogFilePath)
for LogRow in LogFile:
    SplitRow = LogRow.split(' ',1)
    host = SplitRow[0]
    if host in hosts:
        hosts[host] = hosts[host]+1
    else:
        hosts[host] = 1
LogFile.close()
for i in hosts:
    CTime = datetime.utcnow().strftime('%H:%M:%S:%f')
    if hosts[i] > OccuranceAantal:
        print(CTime,':','Host,',i,',aantal keer:', hosts[i])

