import fileinput
import chardet

def filter(inputFile, outputFile, triggerLine):
    dirtyTxt=fileinput.input(inputFile, encoding='utf-8', errors='ignore')
    ok=True
    clean=False
    newFile=open(outputFile,mode='w', encoding='utf-8',  errors='ignore')
    for line in dirtyTxt:
        if triggerLine in line:
            ok = False
            clean = True
        if ok:
            newFile.write(line)
    newFile.close
    return clean

