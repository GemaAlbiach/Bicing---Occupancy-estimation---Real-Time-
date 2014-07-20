#!/usr/bin/env python

import re, urllib
import datetime
import time
import os

getUrl= 'http://wservice.viabicing.cat/getstations.php?v=1'
outputPath='./output/Raw/'
prefixFile = 'bicingSnapshotRaw'
format = '.txt'
suffixFormatDate = '%Y%m%d%H%M%S'
MAX_SNAPSHOTS = 5500
FREQ_SNAPSHOT = 60

if not os.path.exists(outputPath):
    os.makedirs(outputPath)

timestamp = datetime.datetime.now().strftime(suffixFormatDate)
fileName = file(outputPath + prefixFile + timestamp + format,'wt')

i = 0
while True:
  try:
    jsonBicing = urllib.urlopen(getUrl).read()
  
    fileName.write(jsonBicing+'\n')
    i += 1
    if(i == MAX_SNAPSHOTS):
      fileName.close()
      timestamp = datetime.datetime.now().strftime(suffixFormatDate)
      fileName = file(outputPath + prefixFile + timestamp+format,'wt')
      i = 0
  
    time.sleep(FREQ_SNAPSHOT)
  except:
    print 'Error at:' + datetime.datetime.now().strftime(suffixFormatDate)+ ':BicingRawCrawler'
