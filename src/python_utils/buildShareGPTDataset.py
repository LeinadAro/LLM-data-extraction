import os
import sys
import pyarrow.parquet as pq
import numpy as np

import pandas as pd

import pyarrow as pa

#Builds a dataset with the ShareGPT format by taking in input one system prompt for all conversations.
#The prompt file and assistant file that have to go in the same conversation must have the same basename, the extension is ignored.

def build(name, system, promptDir, assistantDir):
    if os.path.isdir(promptDir) and os.path.isdir(assistantDir):
        conversationList=[]
        for promptRoot, promptDirs, promptFiles in os.walk(promptDir, OSError()):
            for assistantRoot, assistantDirs, assistantFiles in os.walk(assistantDir, OSError()):
                if (len(promptFiles) != len(assistantFiles)) or (len(promptFiles) == 0 or len(assistantFiles) == 0): 
                    return 'promptDir and assistantDir are incompatible'
                for i in range(0, len(promptFiles)):              
                    instruction=open(system, 'r', encoding='UTF-8')
                    userInput=open(promptRoot+'/'+promptFiles[i], 'r', encoding='UTF-8')
                    output=open(assistantRoot+'/'+assistantFiles[i], 'r', encoding='UTF-8')
                    convo=[]
                    convo.append(dict([('from','system'),('value', instruction.read())]))
                    convo.append(dict([('from','human'),('value', userInput.read())]))
                    convo.append(dict([('from', 'gpt'),('value', output.read())]))
                    conversationList.append(convo)
        df = pd.DataFrame({'conversations': conversationList}, index=list(range(0, len(conversationList))))
        table = pa.Table.from_pandas(df)
        if os.path.splitext(name)[1] == '': name=name+'.parquet'
        pq.write_table(table, name)
        return f'file {name} successufully built'
    else: return 'directories not valid'



if __name__ == "__main__":
    try: 
        newFilename = sys.argv[1]
        systemMessage = sys.argv[2]
        promptDir = sys.argv[3]
        assistantDir = sys.argv[4]
        if os.path.splitext(newFilename)[1] == '.parquet' or os.path.splitext(newFilename)[1] == '':
            print(build(newFilename, systemMessage, promptDir, assistantDir))
        else: print('new filename extension not valid')
    except FileNotFoundError: 
        print('file not found')
    except IndexError: 
        print('Wrong arguments. There are 4 arguments: new filename, system file, prompts directory and assitant messages directory')
print('end')