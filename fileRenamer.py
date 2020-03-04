#!/usr/bin/env python3

import os, glob

def main():

    rootDir = input('Enter parent directory to run script: ') + '/'

    keywords = input('Enter words in filename to be replaced (multiple words separated by space): ').split(" ")

    replaceInFileName = input('Enter string to take its place (Enter to remove keywords): ')
    print('replacing with ', replaceInFileName)

    for keyword in keywords:
        print('changing for keyword ', keyword)
        for filename in os.listdir(rootDir):
            print('scanning ' + filename)
            if "." and keyword in filename:
                newFileName = filename.replace(keyword, replaceInFileName)
                print('new file name: ', newFileName)
                src = rootDir + filename
                dst = rootDir + newFileName
                print("src: " + src)
                print("dst: " + dst)
                os.rename(src, dst)
                print(filename + " changed to " + newFileName)
                print(' ')

if __name__ == '__main__':

    main()
