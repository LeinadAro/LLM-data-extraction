import os
import sys
import json
from json.decoder import JSONDecodeError

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
    try:
        answer=json.load(open(answer, 'r'))
        rightAnswer=json.load(open(rightAnswer, 'r'))
    except JSONDecodeError: 
        return 'bad-formatted JSON file'
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
    answerDir = sys.argv[1]
    rightDir = sys.argv[2]

for subdir1, dirs1, files1 in os.walk(answerDir):
    for subdir2, dirs2, files2 in os.walk(rightDir):
        for ans in files1:
            for rightAns in files2:
                if ans==rightAns: print(ans+': '+str(check(subdir1+'/'+ans, subdir2+'/'+rightAns)))
    
	