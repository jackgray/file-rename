#!/usr/bin/python

import os, glob


def main():

    rootInputDir = "/Users/jackgray/Desktop/xCOBREcopy"
    #rootInputDir = input('Enter parent directory (in quotes): ')
    rootDir = rootInputDir + "/"

    findInFirstFolderName = "sub-"
    #input('Enter segment in folder name to be replaced (in quotes): ')
    replaceInFirstFolderName = "x"
    #input('Enter string to take its place (in quotes): ')

    findInSubFolderName = "ses-"
    #input('Enter segment in subfolder to be replaced (in quotes): ')
    replaceInSubFolderName = "x"
    #input('Enter string to take its place (in quotes): ')

    for folderName in os.listdir(rootDir):
        if folderName != '.DS_Store':
            newFolderName = folderName.replace(findInFirstFolderName, replaceInFirstFolderName)
            src = rootDir + folderName
            dst = rootDir + newFolderName
            os.rename(src, dst)
            print(folderName + " changed to " + newFolderName)
            print(' ')
            for subFolderName in os.listdir(rootDir + newFolderName):
                if subFolderName != '.DS_Store':
                    newSubFolderName = subFolderName.replace(findInSubFolderName, replaceInSubFolderName)
                    src =  rootDir + newFolderName + '/' + subFolderName
                    dst = rootDir + newFolderName + '/' + newSubFolderName
                    os.rename(src, dst)
                    print(subFolderName + " changed to " + newSubFolderName)
                    for subSubFolderName in os.listdir(rootDir + newFolderName + '/' + newSubFolderName):

                        if subSubFolderName != '.DS_Store':
                            if subSubFolderName.startswith("sub"):
                                    findFileName = folderName + '_' + subFolderName + '_'
                                    newFileName = subSubFolderName.replace(findFileName, '')
                                    src = rootDir + newFolderName + '/' + newSubFolderName + '/' + subSubFolderName
                                    dst = rootDir + newFolderName + '/' + newSubFolderName + '/' + newFileName
                                    os.rename(src, dst)
                                    continue
                            for fileName in os.listdir(rootDir + newFolderName+ '/' + newSubFolderName + '/' + subSubFolderName):
                                if fileName != '.DS_Store':
                                    findFileName = folderName + '_' + subFolderName + '_'
                                    newFileName = fileName.replace(findFileName, '')
                                    src = rootDir + newFolderName + '/' + newSubFolderName + '/' + subSubFolderName + '/' + fileName
                                    dst = rootDir + newFolderName + '/' + newSubFolderName + '/' + subSubFolderName + '/' + newFileName

                                    os.rename(src, dst)
                                    print(fileName + " changed to " + newFileName)





if __name__ == '__main__':

    main()
