import os
import sys
from xml.parsers.expat import ExpatError
import xmltodict

def countPoints(an, rAn):
    points = 0 
    for k1,v1 in an.items():
        for k2, v2 in rAn.items():
            if isinstance(v1, dict) and isinstance(v2, dict):
                points = points + countPoints(v1, v2)
            elif isinstance(v1, list) and isinstance(v2, list):
                if len(v1)==len(v2):
                    for i in range(0, len(v1)):
                        points = points + countPoints(v1[i], v2[i])
                else: return 0
            else:
                if k1==k2:
                    if v1==v2: points += 1
                    if v1!=v2: points -= 1
    return points

def maxPoints(rAn):
    points = 0 
    for k,v in rAn.items():
        if isinstance(v, dict):
            points = points + maxPoints(v)
        elif isinstance(v, list):
            for i in range(0, len(v)):
                points = points + maxPoints(v[i])
        else:
                points = points + 1
    return points

def check(answer, rightAnswer):
    if os.path.splitext(answer)[1] == '.xml' and os.path.splitext(rightAnswer)[1] == '.xml':
        try: 
            with open(answer, 'r') as answer:
                answer = xmltodict.parse(answer.read())
            with open(rightAnswer, 'r') as rightAnswer:
                rightAnswer = xmltodict.parse(rightAnswer.read())
        except ExpatError:
            return 'bad-formatted xml file'
    else: return 'wrong type of file'
    if answer.keys() == rightAnswer.keys():
        #print(countPoints(answer, rightAnswer))
        #print(maxPoints(rightAnswer))
        pt=(countPoints(answer, rightAnswer)/maxPoints(rightAnswer))*100
        if pt < 0: pt = 0
        return '{:.2f}%'.format(pt)
    else: return 'Keys of files do not match'
       
if __name__ == "__main__":
    answersDir = sys.argv[1]
    rightDir = sys.argv[2]

for subdir1, dirs1, files1 in os.walk(answersDir):
    for subdir2, dirs2, files2 in os.walk(rightDir):
        for ans in files1:
            for rightAns in files2:
                if ans==rightAns: 
                    print(ans+': '+check(subdir1+'/'+ans, subdir2+'/'+rightAns))
    
	