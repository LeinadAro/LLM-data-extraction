import os
import sys
import json

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
    answer=open(answer, 'r')
    answer=json.load(answer)
    rightAnswer=json.load(open(rightAnswer, 'r'))
    i=0
    if isinstance(answer, list):
        pt=0
        for i in range(0, len(answer)):
            an = answer[i]
            rAn = rightAnswer[i]
            pt=pt+countPoints(an, rAn)
        return '{:.2f}%'.format(pt/len(answer))
    else:
        return '{:.2f}%'.format(countPoints(answer, rightAnswer))
       
if __name__ == "__main__":
    answerDir = sys.argv[1]
    rightDir = sys.argv[2]

for subdir1, dirs1, files1 in os.walk(answerDir):
    for subdir2, dirs2, files2 in os.walk(rightDir):
        for ans in files1:
            for rightAns in files2:
                if ans==rightAns: print(check(subdir1+'/'+ans, subdir2+'/'+rightAns))
    
	