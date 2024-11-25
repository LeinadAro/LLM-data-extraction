import os
import sys
import pyarrow.parquet as pq
import numpy as np

import pandas as pd

import pyarrow as pa




def build(system, promptDir, assistantDir):
    instructionList=[]
    inputList=[]
    outputList=[]
    for subdir, dirs, files in os.walk(promptDir):
        for file in files:
            print(file)
            instruction=open(system, 'r', encoding='UTF-8')
            userInput=open(subdir+'/'+file, 'r', encoding='UTF-8')
            output=open(assistantDir+'/'+os.path.basename(file).split('.')[0]+'.xml', 'r', encoding='UTF-8')
            instructionList.append(instruction.read())
            inputList.append(userInput.read())
            outputList.append(output.read())
    df = pd.DataFrame({'instruction': instructionList,
                   'input': inputList,
                   'output': outputList},
                   index=list(range(0, len(instructionList))))
    print(df)
    table = pa.Table.from_pandas(df)
    pq.write_table(table, 'alpacaDataset.parquet')


if __name__ == "__main__":
    a = sys.argv[1]
    b = sys.argv[2]
    c = sys.argv[3]
    build(a, b, c)
print('end')