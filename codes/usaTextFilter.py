import textFilter
import pdfToTxt

pdf=input("Inserire file da ripulire: ")
dirtyTxt='dirty.txt'
cleanTxt=input("Inserire nome file ripulito: ")
triggerLine=input("Inserire frase trigger: ")
pdfToTxt.pdf_to_text(pdf,dirtyTxt)
print('file convertito')
textFilter.filter(dirtyTxt, cleanTxt, triggerLine)
print('file ripulito')