import os
import shutil
import time

def main():
    deletedFoldersCount = 0
    deletedFilesCount = 0

    path = "/PATH_TO_DELETE"

    days = 30
    seconds = time.time() - (days * 24 * 60 * 60)

    if os.path.exists(path):
        for rootFolder, folders, files in os.walk(path):
            if seconds >= getFileOrFolderAge(rootFolder):
                removeFolder(rootFolder)
				deletedFoldersCount += 1
                break

    else:
        for folder in folders:
            folderPath = os.path.join(rootFolder, folder)

            if seconds >= getFileOrFolderAge(folderPath):
                removeFolder(folderPath)
				deletedFoldersCount += 1
        
        
        
        for file in files:
            filePath = os.path.join(rootFolder, file)

            if seconds >= getFileOrFolderAge(filePath):
                removeFile(filePath)
                deletedFilesCount += 1 
        
    else:
        if seconds >= getFileOrFolderAge(path):
                removeFile(path)
				deletedFilesCount += 1
    
    else:
        print(f'"{path}" is not found')
		deletedFilesCount += 1

    print(f"Total folders deleted: {deletedFoldersCount}")
	print(f"Total files deleted: {deletedFilesCount}")

def removeFolder(path):
    if not shutil.rmtree(path):
        print(f"{path} is removed successfully")
    
    else:
        print(f"Unable to delete the " + path)

def getFileOrFolderAge(path):
    ctime = os.stat(path).st_ctime

    return ctime

