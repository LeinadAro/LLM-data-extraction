#!/bin/bash
model=$1
promptDir=$2
answerDir=$3
if [ ! -d "$answerDir" ]; then
	mkdir $answerDir
fi
start_time=$(date +%s.%N)
for filename in $promptDir/*.txt
do
	newFile=$(basename "$filename")
	echo "elaborating $newFile"
	ollama run $model < $filename > $answerDir/$newFile
done
end_time=$(date +%s.%N)

runtime=$( echo "$end_time - $start_time" | bc )
echo "The script took $runtime seconds to execute." > $answerDir/time.txt
echo "END"
