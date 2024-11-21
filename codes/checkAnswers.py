import json
import os

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

def check(answers, rightAnswers):
    answers=open(answers, 'r')
    answers=json.load(answers)
    rightAnswers=json.load(open(rightAnswers, 'r'))
    i=0
    if isinstance(answers, list):
        pt=0
        for i in range(0, len(answers)):
            an = answers[i]
            rAn = rightAnswers[i]
            pt=pt+countPoints(an, rAn)
        i=i+1
        return '{:.2f}%'.format(pt/len(answers))
    else:
        return '{:.2f}%'.format(countPoints(answers, rightAnswers))
       
    
answersDir=input('insert answersDir: ')
rightDir=input('insert rightDir: ')
for subdir1, dirs1, files1 in os.walk(answersDir):
    for subdir2, dirs2, files2 in os.walk(rightDir):
        for ans in files1:
            for rightAns in files2:
                if ans==rightAns: print(check(subdir1+'/'+ans, subdir2+'/'+rightAns))
    
	