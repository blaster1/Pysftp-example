#!/usr/bin/env python
import pysftp
import datetime
import fnmatch
import time
import sys
import os
import logging
logname = os.path.basename(__file__)
logger = logging.getLogger(logname)
logger.setLevel(logging.INFO)
handler = logging.FileHandler(logname +'.log')
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s' , datefmt='%m/%d/%Y %I:%M:%S %p')
handler.setFormatter(formatter)
logger.addHandler(handler)
handler = logging.StreamHandler()
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s' , datefmt='%m/%d/%Y %I:%M:%S %p')
handler.setFormatter(formatter)
logger.addHandler(handler)

os.chdir('/home/MYLOCALHOME/DOWNLOADDIR')
now = datetime.datetime.now()
DTG = (datetime.date.today()).strftime('%m%d%Y')
FILESET = [line.strip() for line in open('/home/MYLOCALHOME/scripts/FILESET', 'r')]
def intersect(FILESET, FILESET_AVAILABLE):
 return list(set(FILESET) & set(FILESET_AVAILABLE))
def union(FILESET, FILESET_AVAILABLE):
 return list(set(FILESET) | set(FILESET_AVAILABLE))
def SOMEPATTERNGET():
 try:
  sftp = pysftp.Connection(host='sftp.someplace.com', username='someuser', password='somepassword')
  sftp.cwd('/ftphome/someuser/fromsomeplace')
  NUMFILES = 0
  FILESET_AVAILABLE = []
  for FILENAME in sftp.listdir('/ftphome/someuser/fromsomeplace'):
   if fnmatch.fnmatch(FILENAME, 'SOMEPATTERN*' + DTG + '*'):
    FILESET_AVAILABLE.append(FILENAME[0:8])
    NUMFILES += 1
  if NUMFILES == 14:
   logger.info('Found %s' % NUMFILES)
   logger.info('Downloading all SOMEPATTERN Files now')
   logger.info(intersect(FILESET, FILESET_AVAILABLE))
   for FILENAME in sftp.listdir('/ftphome/someuser/fromsomeplace'):
    if fnmatch.fnmatch(FILENAME, 'SOMEPATTERN*' + DTG + '*'):
     sftp.get(FILENAME)
   sftp.close()
  elif len(sys.argv) > 1:
   logger.info('Command line arg to download immediately')
   logger.info('Downloading %s SOMEPATTERN Files Now' % NUMFILES)
   logger.info(intersect(FILESET, FILESET_AVAILABLE))
   for FILENAME in sftp.listdir('/ftphome/someuser/fromsomeplace'):
    if fnmatch.fnmatch(FILENAME, 'SOMEPATTERN*' + DTG + '*'):
     sftp.get(FILENAME)
   sftp.close()
  elif now.hour == 11:
   logger.info('It is 11:00')
   logger.info('Downloading %s SOMEPATTERN Files Now' % NUMFILES)
   logger.info(intersect(FILESET, FILESET_AVAILABLE))
   for FILENAME in sftp.listdir('/ftphome/someuser/fromsomeplace'):
    if fnmatch.fnmatch(FILENAME, 'SOMEPATTERN*' + DTG + '*'):
     sftp.get(FILENAME)
   sftp.close()
  else:
   sftp.close()
   logger.info('Looking for 14 SOMEPATTERN Files with the Datestring: %s' % DTG)
   logger.info('Found %s' % NUMFILES)
   logger.info(intersect(FILESET, FILESET_AVAILABLE))
   logger.info('sleeping for 10 minutes')
   time.sleep(600)
   SOMEPATTERNGET()
 except Exception,e:
  print str(e)
  os._exit(1)
  logger.info('Download was NOT successful')
SOMEPATTERNGET()






