import os
import sys
import json
from json.decoder import JSONDecodeError

#Checks the json answers of an llm by comparison with the 'right' answers.
#The files that have to be compared must have the same name.

def countPoints(an, rAn):
    if len(list(an))==len(list(rAn)):
                points=0
                for k1,v1 in an.items():
                    for k2, v2 in rAn.items():
                        if k1==k2:
                            if v1 == v2 : points=points+1
                            if v1 != v2 : points=points-1
                points=(points/len(list(an)))*100
                return points
    else: return 0.0

def check(answer, rightAnswer):
    if os.path.splitext(answer)[1] == '.json' and os.path.splitext(rightAnswer)[1] == '.json':
        try:
            answer=json.load(open(answer, 'r'))
            rightAnswer=json.load(open(rightAnswer, 'r'))
        except JSONDecodeError: 
            return 'bad-formatted JSON file'
    else: return 'wrong type of file'

    i=0
    pt=0
    if isinstance(answer, list) and isinstance(rightAnswer, list):
        if len(answer) == len(rightAnswer):
            for i in range(0, len(answer)):
                an = answer[i]
                rAn = rightAnswer[i]
                pt=pt+countPoints(an, rAn)
            pt = (pt/len(answer))
        else: 
            pt = 0
    elif not isinstance(answer, list) and not isinstance(rightAnswer, list):
        pt = countPoints(answer, rightAnswer)
    else: 
        pt = 0
    if pt < 0:
        pt = 0
    return '{:.2f}%'.format(pt)
    
    
if __name__ == "__main__":
    try:
        answerDir = sys.argv[1]
        rightDir = sys.argv[2]
        if os.path.isdir(answerDir) and os.path.isdir(rightDir):
            for ansRoot, ansDirs, ansFiles in os.walk(answerDir):
                for rightRoot, rightDirs, rightFiles in os.walk(rightDir):
                    for ans in ansFiles:
                        for rightAns in rightFiles:
                            if ans==rightAns: print(ans+': '+str(check(ansRoot+'/'+ans, rightRoot+'/'+rightAns)))
        else: print('directories not valid')
    except IndexError:
        print('Wrong arguments. There are 2: answers directory and right answers directory')



	