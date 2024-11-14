import os 

#baseString = '{"messages": [{"role": "system", "content": ""}, {"role": "user", "content": ""}, {"role": "assistant", "content": ""}]}'
firstPiece='"""Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.\n\n### Instrucion:\n{'
secondPiece='}\n\n### Input:\n{'
thirdPiece='}\n\n### Response:\n{'
fourthPiece='}"""\n\n'
#jsonForm='{"Comune":null, "Indirizzo":null, "Vani": null, "Locali": null,  "Mq": null, "Bagni": null, "Piano": null, "Posti auto": null, "N° Procedura": null, "Lotto":null}'
def build(system, promptDir, assistantDir):
    result=open('dataset.txt', 'w', encoding='UTF-8')
    for subdir, dirs, files in os.walk(promptDir):
        for file in files:
            print(file)
            response=assistantDir+'/'+file
            response=open(response, 'r', encoding='UTF-8')
            sys=open(system, 'r', encoding='UTF-8')
            userMsg = open(subdir+'/'+file, 'r', encoding='UTF-8')
            result.write(firstPiece+sys.read()+secondPiece+userMsg.read()+thirdPiece+response.read()+fourthPiece)
    result.close()


system=input('inserire file system: ')
promptDir=input('inserire promptDir: ')
assistantDir=input('inserire assistantDir: ')
build(system, promptDir, assistantDir)
print('end')