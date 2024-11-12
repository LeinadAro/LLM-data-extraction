import os 

#baseString = '{"messages": [{"role": "system", "content": ""}, {"role": "user", "content": ""}, {"role": "assistant", "content": ""}]}'
firstPiece='{"messages": [{"role": "system", "content": "'
secondPiece='}, {"role": "user", "content": "'
thirdPiece='"}, {"role": "assistant", "content": "'
fourthPiece='"}]}'
jsonForm='{"Comune":null, "Indirizzo":null, "Vani": null, "Locali": null,  "Mq": null, "Bagni": null, "Piano": null, "Posti auto": null, "N° Procedura": null, "Lotto":null}'
def build(system, promptDir, assistantDir):
    result=open('result.txt', 'w', encoding='UTF-8')
    for subdir, dirs, files in os.walk(promptDir):
        for file in files:
            print(file)
            userMsg = open(subdir+'/'+file, 'r', encoding='UTF-8')
            result.write(firstPiece+system+secondPiece+userMsg.read()+thirdPiece+jsonForm+fourthPiece)
    result.close()


system=input('inserire file system: ')
promptDir=input('inserire promptDir: ')
build(system, promptDir, jsonForm)
print('end')