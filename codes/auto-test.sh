#!/bin/bash
model = $1
promptDir= $2
anwserDir= $3
for filename in promptDir/*.txt
do
	newFile=$(basename "$filename")
	echo "elaborating $newFile"
	bash stopwatch.sh $model $filename > $anwserDir/$newFile
done
echo "END"
