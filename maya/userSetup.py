import os
import pymel.core as pm
import maya.cmds as mc
from datetime import datetime

### Date ###
now = datetime.now()
date = now.strftime('%Y-%m-%d')


def sceneLoad():

   ### Date and Time ###
   now = datetime.now()
   date = now.strftime('%Y-%m-%d')
   time = now.strftime('%H:%M:%S')

   ### Path Variables ###
   user = os.getlogin()
   scriptPath = mc.file(q=True, sn=True)
   scriptName = os.path.basename(scriptPath)
   scriptFolder = os.path.dirname(scriptPath)
   shotFolder = os.path.dirname(scriptFolder)
   logFolder = shotFolder + '/.log/' + date + '/'
   logProjectFolder = logFolder + '/' + scriptName + '/'
   logFile = logProjectFolder + user + '.txt'

   ### Create Log Project Folder ###
   try:
      os.makedirs(logProjectFolder)
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

def sceneSaved():

   ### Date and Time ###
   now = datetime.now()
   date = now.strftime('%Y-%m-%d')
   time = now.strftime('%H:%M:%S')
   
   ### Path Variables ###
   user = os.getlogin()
   scriptPath = mc.file(q=True, sn=True)
   scriptName = os.path.basename(scriptPath)
   scriptFolder = os.path.dirname(scriptPath)
   shotFolder = os.path.dirname(scriptFolder)
   logFolder = shotFolder + '/.log/' + date + '/'
   logProjectFolder = logFolder + '/' + scriptName + '/'
   logFile = logProjectFolder + user + '.txt'

   ### Create Log Project Folder ###
   try:
      os.makedirs(logProjectFolder)
   except FileExistsError:
      pass

   ### Create Log File ###
   scriptLog = open(logFile, 'a')
   scriptLog.close()

   ### Write File ###
   scriptLog = open(logFile, 'r')
   if(scriptLog.read() == ''):
      scriptLog = open(logFile, 'a')
      scriptLog.write("Script loaded at: " + time + "\nScript saved at: " + time)
      scriptLog.close()
   else:
      scriptLog = open(logFile, 'a')
      scriptLog.write("\nScript saved at: " + time)
      scriptLog.close()

   ### Calculate User Total Time ###
   runtimeZero = datetime.strptime("00:00:00", "%H:%M:%S")
   userRuntime = runtimeZero

   with open(logFile, 'r') as log:
      loadedTime = datetime.strptime(log.readline().split(': ', 1)[1].strip(), "%H:%M:%S")
      lastSavedTime = datetime.strptime(log.readline().split(': ', 1)[1].strip(), "%H:%M:%S")
      for line in log:
         if(line.find('loaded') == -1):
            lastSavedTime = datetime.strptime(line.split(': ', 1)[1].strip(), "%H:%M:%S")
         else:
            userRuntime += (lastSavedTime - loadedTime)
            loadedTime = datetime.strptime(line.split(': ', 1)[1].strip(), "%H:%M:%S")
            lastSavedTime = datetime.strptime(line.split(': ', 1)[1].strip(), "%H:%M:%S")
      userRuntime += (lastSavedTime - loadedTime)

   ### Write Summary Log ###
   summaryFile = logProjectFolder + '.log-summary.txt'
   summaryLog = open(summaryFile, 'a')
   summaryLog = open(summaryFile, 'r')
   
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

pm.scriptJob(e=('SceneOpened', sceneLoad))
pm.scriptJob(e=('SceneSaved', sceneSaved))