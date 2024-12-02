import os
import sys
import pyarrow.parquet as pq
import numpy as np

import pandas as pd

import pyarrow as pa


def build(name, system, promptDir, assistantDir):
    conversationList=[]
    for promptRoot, promptDirs, promptFiles in os.walk(promptDir):
        for assistantRoot, assistantDirs, assistantFiles in os.walk(promptDir):
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
    print(df)
    table = pa.Table.from_pandas(df)
    pq.write_table(table, name)



if __name__ == "__main__":
    a = sys.argv[1]
    b = sys.argv[2]
    c = sys.argv[3]
    d = sys.argv[4]
    build(a, b, c, d)
print('end')