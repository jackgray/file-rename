#!/usr/bin/python

import os, time


def main():

    print("This script will change the names of files and folders to remove unecessary prefixes and replace them with 'x'")
    #time.sleep(5)
    print("It is designed to work on SchizConnect openneuro file structure format where subject folder names start with 'sub-' and child session folder names start with 'ses-'.")
    #time.sleep(5)
    print("Make sure you run it on the immediate parent directory of the subject folders.")
    #time.sleep(5)

    #rootInputDir = "/Users/jackgray/Desktop/xCOBREcopy"
    rootInputDir = input('Enter parent directory (in quotes): ')
    rootDir = rootInputDir + "/"

    print(' ')
    print("Changing names...")
    print('')
    time.sleep(1)
    
    findInFirstFolderName = "sub-"
    #input('Enter segment in folder name to be replaced (in quotes): ')
    replaceInFirstFolderName = "x"
    #input('Enter string to take its place (in quotes): ')
    
    findInSubFolderName = "ses-"
    #input('Enter segment in subfolder to be replaced (in quotes): ')
    replaceInSubFolderName = "x"
    #input('Enter string to take its place (in quotes): ')

    for folderName in os.listdir(rootDir):
            newFolderName = folderName.replace(findInFirstFolderName, replaceInFirstFolderName)
            src = rootDir + folderName 
            dst = rootDir + newFolderName
            os.rename(src, dst)
            print(folderName + " -> " + newFolderName)
            print(' ')
            for subFolderName in os.listdir(rootDir + newFolderName):
                newSubFolderName = subFolderName.replace(findInSubFolderName, replaceInSubFolderName)    
                src =  rootDir + newFolderName + '/' + subFolderName
                dst = rootDir + newFolderName + '/' + newSubFolderName
                os.rename(src, dst) 
                print(subFolderName + " -> " + newSubFolderName)
                print(' ')
                for subSubFolderName in os.listdir(rootDir + newFolderName + '/' + newSubFolderName): 
                    findFileName = folderName + '_' + subFolderName + '_'
                    newFileName = subSubFolderName.replace(findFileName, '')
                    src = rootDir + newFolderName + '/' + newSubFolderName + '/' + subSubFolderName
                    dst = rootDir + newFolderName + '/' + newSubFolderName + '/' + newFileName
                    os.rename(src, dst)
                    print(subSubFolderName + " -> " + newFileName)
                    print(' ')
                    continue
                    for fileName in os.listdir(rootDir + newFolderName+ '/' + newSubFolderName + '/' + subSubFolderName):
                        findFileName = folderName + '_' + subFolderName + '_'
                        newFileName = fileName.replace(findFileName, '')
                        src = rootDir + newFolderName + '/' + newSubFolderName + '/' + subSubFolderName + '/' + fileName
                        dst = rootDir + newFolderName + '/' + newSubFolderName + '/' + subSubFolderName + '/' + newFileName  
                        os.rename(src, dst)
                        print(fileName + " -> " + newFileName) 
                                    
                    
                



if __name__ == '__main__':
    try:
        main()
    except:
        pass
    

