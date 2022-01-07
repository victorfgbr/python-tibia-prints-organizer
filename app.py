from os import listdir
from os.path import isfile, join
from dto import PrintDto

print ("organizing the print folder's by character name...")

# 1. reads the print folder's path
printsFolderPath = "C:\\Users\\Usuário\\AppData\\Local\\Tibia\\packages\\Tibia\\screenshots"
print (">>> printsFolderPath: " + printsFolderPath)

# 2. get list of files
filesNames = [f for f in listdir(printsFolderPath) if isfile(join(printsFolderPath, f))]
for fileName in filesNames:
    printDto = PrintDto(fileName)
    print (printDto)
    
