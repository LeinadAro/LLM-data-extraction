import os
import textFilter
import pdfToTxt

root_dir = input('Dirty directory: ')
middle_dir = './midlle'
target_dir = input('Clean directory: ')
triggerLines = input('Trigger line: ')

triggerLines = triggerLines.split(',')

if not os.path.exists(target_dir):
    os.makedirs(target_dir)

if not os.path.exists(middle_dir):
    os.makedirs(middle_dir)

for root, dirs, files in os.walk(root_dir):
    for file in files:
        isClean = False
        dirty = root_dir+'/'+file
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
print('fine')