import shutil
from os import listdir, makedirs
from os.path import isfile, join
from dto import PrintDto
import sys

# Reads the print folder's path argument
if (len(sys.argv) < 2):
    print (f'Argument not found, please informe path of screenshots folder.')
    exit()

printsFolderPath = str(sys.argv[1])
print(f'>>> printsFolderPath: {printsFolderPath}')

# Get list of prints
listPrintDto = [PrintDto(f) for f in listdir(printsFolderPath) if isfile(join(printsFolderPath, f))]

for printDto in listPrintDto:
    # Create new directory folder
    newFolderPath = join(printsFolderPath, printDto.characterName)
    newFolderPath = join(newFolderPath, printDto.type)
    makedirs(newFolderPath, exist_ok=True)

    # Move file to the new folder
    print (f'>>> Moving {printDto.fileName} to {printDto.characterName}/{printDto.type}/')
    olderFilePath = join(printsFolderPath, printDto.fileName)
    newFilePath = join(newFolderPath, printDto.fileName)
    shutil.move(olderFilePath, newFilePath)
    