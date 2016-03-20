__author__ = 'Alexis'

import zipfile

myWorkingDir = "C:\\Users\\Alexis\\Documents\\ComicDisplayWD"
myFile = zipfile.ZipFile("C:\\Users\\Alexis\\Dropbox\\Robyn_H_11774_4d5.zip", "r")

for name in myFile.namelist():
    print(name)

myFile.extractall(myWorkingDir)

