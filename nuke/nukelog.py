from datetime import datetime
import os
import nuke

### Date ###
now = datetime.now()
date = now.strftime('%Y-%m-%d')

### Path Variables ###
scriptPath = nuke.root().name()
user = os.getlogin()
scriptName = os.path.basename(scriptPath)
scriptFolder = os.path.dirname(scriptPath)
shotFolder = os.path.dirname(scriptFolder)
logFolder = shotFolder + '/.log/' + date + '/'

### Create Log And Date Folder ###
try:
   os.makedirs(logFolder)
except FileExistsError:
   pass

### Create Log ###
def scriptLoad():

    ### Date and Time ###
    now = datetime.now()
    date = now.strftime('%Y-%m-%d')
    time = now.strftime('%H:%M:%S')

    ### Path Variables ###
    scriptPath = nuke.root().name()
    scriptName = os.path.basename(scriptPath)
    scriptFolder = os.path.dirname(scriptPath)
    shotFolder = os.path.dirname(scriptFolder)
    logFolder = shotFolder + '/.log/' + date
    logProjectFolder = logFolder + '/' + scriptName + '/'
    logFile = logProjectFolder + user + '.txt'

    ### Create Log Project Folder ###
    try:
        os.makedirs(logFolder + '/' + scriptName + '/')
    except FileExistsError:
        pass
    
    ### Create Log File ###
    scriptLog = open(logFile, 'a')
    scriptLog.close()

    ### Write File ###
    scriptLog = open(logFile, 'r')
    if(scriptLog.read() == ''):
        scriptLog = open(logFile, 'a')
        scriptLog.write("Script loaded at: " + time)
        scriptLog.close()
    else:
        scriptLog = open(logFile, 'a')
        scriptLog.write("\nScript loaded at: " + time)
        scriptLog.close()

def scriptSave():

    ### Time ###
    now = datetime.now()
    time = now.strftime('%H:%M:%S')

    ### Path Variables ###
    scriptPath = nuke.root().name()
    scriptName = os.path.basename(scriptPath)
    scriptFolder = os.path.dirname(scriptPath)
    shotFolder = os.path.dirname(scriptFolder)
    logFolder = shotFolder + '/.log/' + date
    logProjectFolder = logFolder + '/' + scriptName + '/'
    logFile = logProjectFolder + user + '.txt'

    ### Create Log Project Folder ###
    try:
        os.makedirs(logFolder + '/' + scriptName + '/')
    except FileExistsError:
        pass

    ### Write File ###
    scriptLog = open(logFile, 'a')
    scriptLog = open(logFile, 'r')
    if(scriptLog.read() == ''):
        scriptLog = open(logFile, 'a')
        scriptLog.write("Script loaded at: " + time)
        scriptLog.close()
    else:
        scriptLog = open(logFile, 'a')
        scriptLog.write("\nScript saved at: " + time)       

def scriptClose():

    ### Time ###
    now = datetime.now()
    time = now.strftime('%H:%M:%S')

    ### Path Variables ###
    scriptPath = nuke.root().name()
    scriptName = os.path.basename(scriptPath)
    scriptFolder = os.path.dirname(scriptPath)
    shotFolder = os.path.dirname(scriptFolder)
    logFolder = shotFolder + '/.log/' + date
    logProjectFolder = logFolder + '/' + scriptName + '/'
    logFile = logProjectFolder + user + '.txt'

    ### Write File ###
    scriptLog = open(logFile, 'a')
    scriptLog.write("\nScript closed at: " + time)
    scriptLog.close()

    ### Calculate User Total Time ###
    openInstances = 0
    userRuntime = datetime.strptime("00:00:00", "%H:%M:%S")
    with open(logFile, 'r') as log:
        for lines in log:
            if(lines.find('loaded')!=-1):
                openInstances += 1
                if(openInstances == 1):
                    loadedTimeStr = str(lines.split(': ', 1)[1]).strip()
                    loadedTime = datetime.strptime(loadedTimeStr, "%H:%M:%S")
            if(lines.find('closed')!=-1):
                openInstances -= 1
                if (openInstances == 0):
                    closedTimeStr = str(lines.split(': ', 1)[1]).strip()
                    closedTime = datetime.strptime(closedTimeStr, "%H:%M:%S")

            if(openInstances == 0):
                userRuntime += closedTime - loadedTime
    
    ### Write Summary Log ###
    summaryFile = logProjectFolder + '.log-summary.txt'
    summaryLog = open(summaryFile, 'a')
    summaryLog = open(summaryFile, 'r')

    runtimeZero = datetime.strptime("00:00:00", "%H:%M:%S")
    totalRuntime = runtimeZero
    userRuntimeStr = str(userRuntime.time())

    if(summaryLog.read() == ''):
        summaryLog = open(summaryFile, 'a')
        summaryLog.write("Total time: " + userRuntimeStr + "\n" + user + ": " + userRuntimeStr + "\n")
    else:
        summaryLog = open(summaryFile, 'r')
        otherUsersLines = ''
        userLines = user + ": " + userRuntimeStr + "\n"

        for lines in summaryLog:
            if(lines.find(user) == -1 and lines.find('Total time: ') == -1):
                otherUsersLines += lines
                linesTime = datetime.strptime(lines.split(': ', 1)[1].strip(), "%H:%M:%S")
                totalRuntime = totalRuntime + (linesTime - runtimeZero)
        
        totalRuntime = totalRuntime + (userRuntime - runtimeZero)
        summaryRead = "Total time: " + str(totalRuntime.time()) + "\n" + userLines + otherUsersLines

        summaryLog = open(summaryFile, 'w')
        summaryLog.write(summaryRead)

nuke.addOnScriptLoad(scriptLoad)
nuke.addOnScriptSave(scriptSave)
nuke.addOnScriptClose(scriptClose)