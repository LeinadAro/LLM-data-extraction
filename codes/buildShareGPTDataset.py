import os
import sys
import pyarrow.parquet as pq
import numpy as np

import pandas as pd

import pyarrow as pa

#{"from": "system", "value": "You are an assistant"}
#{"from": "human", "value": "What is 2+2?"}
#{"from": "gpt", "value": "It's 4."}


def build(system, promptDir, assistantDir):
    conversationList=[]
    for subdir, dirs, files in os.walk(promptDir):
        for file in files:
            print(file)
            
            instruction=open(system, 'r', encoding='UTF-8')
            userInput=open(subdir+'/'+file, 'r', encoding='UTF-8')
            output=open(assistantDir+'/'+os.path.basename(file).split('.')[0]+'.xml', 'r', encoding='UTF-8')
            convo=[]
            convo.append(dict([('from','system'),('value', instruction.read())]))
            convo.append(dict([('from','human'),('value', userInput.read())]))
            convo.append(dict([('from', 'gpt'),('value', output.read())]))
            conversationList.append(convo)
    df = pd.DataFrame({'conversations': conversationList}, index=list(range(0, len(conversationList))))
    print(df)
    table = pa.Table.from_pandas(df)
    pq.write_table(table, 'dataset.parquet')



if __name__ == "__main__":
    a = sys.argv[1]
    b = sys.argv[2]
    c = sys.argv[3]
    build(a, b, c)
print('end')