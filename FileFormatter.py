#this strips leading spaces from files that aren't compatible from different OS
import os

def formatter(filepath):
    #lists the folder contents
    foldercontents = os.listdir(filepath)
    #bad characters for files
    bad_chars = [' ', '_', '-', '!','.', ',']
    #iterates through files in folder
    for filenames in foldercontents:
        #replaces and removes bad_chars with no space
        newfile = ''.join(i for i in filenames if not i in bad_chars)
        #creates sourcepath for the old files
        sourcepath = filepath +'\\'+ filenames
        #
        destinationpath = filepath +'\\'+ newfile
        os.rename(sourcepath, destinationpath)

        
filepath = 'C:\\Users\\mfaber\\Documents\\test folder'

formatter(filepath)