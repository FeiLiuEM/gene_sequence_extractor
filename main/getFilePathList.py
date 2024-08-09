
import os

def getFilePathList(path, filetype):
    
    pathList = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(filetype):
                #pathList.append(os.path.join(file)) #不带文件位置的版本
                pathList.append(os.path.join(root,file)) #带文件位置的版本
    return pathList


