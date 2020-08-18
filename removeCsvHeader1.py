#! python3
# removecsvheader.py - Removes the header from all CSV files in the current working directory
  
import csv, os
import shutil
  
os.makedirs('headerRemoved', exist_ok=True)
  
# loop through every file in the current working directory.
for csvFilename in os.listdir('.'):
    if not csvFilename.endswith('.csv'):
        continue # skip non-csv files
    print('Removing header from ' + csvFilename + '...')
    targetFilename = os.path.join('headerRemoved', csvFilename)
    print(targetFilename)
    with open(csvFilename) as ifo, open(targetFilename, "w") as ofo:
        print(ifo)
        print(ofo)
        ifo.readline()
        shutil.copyfileobj(ifo, ofo)
