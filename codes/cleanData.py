import os
import textFilter
import pdfToTxt

#This method takes pdf and txt files in input. The pdfs are converted in txt files. Then it filters the txt based on the triggerLines using the textFilter.filter method. The files original files are untouched because the processed files are put in a new directory.
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
    
    
dirty_dir = input('Dirty directory: ')
if os.path.isdir(dirty_dir):
    target_dir = input('Clean directory: ')
    triggerLines = input('Trigger line: ')
    dataCleaner(dirty_dir, target_dir, triggerLines)
else:
    print('Dirty dir does not exist')
print('fine')