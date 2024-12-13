import textFilter
import pdfToTxt
import sys

try:
    pdf=sys.argv[1]
    dirtyTxt='dirty.txt'
    cleanTxt=sys.argv[2]
    triggerLine=sys.argv[3]
    pdfToTxt.convert(pdf,dirtyTxt)
    print('file convertito')
    textFilter.filter(dirtyTxt, cleanTxt, triggerLine)
    print('file ripulito')
except IndexError: 
    print('Wrong arguments. There are 3: PDF filepath, new filepath, string with trigger line')