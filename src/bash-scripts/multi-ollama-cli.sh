#!/bin/bash

#Script per testare un modello su una cartella contenente uno o più prompt. Nella cartella delle risposte vengono creata un cartella contenente i tempi di risposta in secondi.
#Le risposte sono date in file JSON perchè lo script è pensato per testare modelli istruiti a rispondere in JSON. 

model=$1
promptDir=$2
answerDir=$3

fileExtension="json"

if [ $# -eq 3 ]; then
	if [ -d "$promptDir" ]; then
		if [ ! -d "$answerDir" ]; then
			mkdir $answerDir
		fi
		start_time=$(date +%s.%N)
		for filename in $promptDir/*.txt
		do
			newFile=$(basename "$filename" '.txt')
			echo "elaborating $newFile"
			file_start_time=$(date +%s.%N)
			timeout 300 ollama run $model < $filename > $answerDir/$newFile'.'$fileExtension	#timeout a 5 min per tagliare risposte troppo lunghe
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
		
	else echo "Error: Prompt directory does not exist"

	fi
else echo "Error! The arguments are 3: model, prompt directory, answer directory."
fi
