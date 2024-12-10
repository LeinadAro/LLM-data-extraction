import os
import sys
import textFilter
import pdfToTxt

#This method takes pdf and txt files in input. The pdfs are converted in txt files. 
#Then it filters the txt based on the triggerLines using the textFilter.filter method.
#The original files are untouched because the processed files are put in a new directory.

def dataCleaner(dirty_dir, target_dir, triggerLines):
    triggerLines = triggerLines.split(',')
    middle_dir = './midlle'
        
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    if not os.path.exists(middle_dir):
        os.makedirs(middle_dir)
    for root, dirs, files in os.walk(dirty_dir):
        for file in files:
            isClean = False
            dirty = dirty_dir+'/'+file
            base, extension = os.path.splitext(file)
            clean = target_dir+'/'+base+'.txt'
            if extension == '.pdf' or extension == '.txt':
                if extension == '.pdf':
                    semi_clean = middle_dir+'/'+base+'.txt'
                    pdfToTxt.convert(dirty, semi_clean)
                    dirty = semi_clean
                
                for triggerLine in triggerLines:  
                    if not isClean:
                       isClean = textFilter.filter(dirty, clean, triggerLine)
                os.remove(dirty)
    os.rmdir(middle_dir)        
    
if __name__ == "__main__":   
    dirty_dir = sys.argv[1]
    target_dir = sys.argv[2]
    triggerLines = sys.argv[3]
    if os.path.isdir(dirty_dir):
        dataCleaner(dirty_dir, target_dir, triggerLines)
    else:
        print('Dirty dir does not exist')
    print('fine')