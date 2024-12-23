#!/bin/bash
model=$1
promptDir=$2
answerDir=$3
fileExtension=$4
if [ ! -d "$answerDir" ]; then
	mkdir $answerDir
fi
start_time=$(date +%s.%N)
for filename in $promptDir/*.txt
do
	newFile=$(basename "$filename" '.txt')
	echo "elaborating $newFile"
	file_start_time=$(date +%s.%N)
	#timeout 300 ollama run $model < $filename > $answerDir/$newFile'.'$fileExtension
	timeout 300 bash request.sh $model $filename $answerDir/$newFile'.'$fileExtension
	file_end_time=$(date +%s.%N)
	file_runtime=$( echo "$file_end_time - $file_start_time" | bc )
	if [ ! -d "$answerDir/times" ]; then
	        mkdir $answerDir/times
	fi
	echo "The script took $file_runtime seconds to execute." > $answerDir/times/$newFile'.txt'

done

end_time=$(date +%s.%N)

runtime=$( echo "$end_time - $start_time" | bc )
echo "The script took $runtime seconds to execute." > $answerDir/times/total-time.txt
echo "END"
