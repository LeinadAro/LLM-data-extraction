#!/bin/bash

#Script per elaborare i prompt contenuti in una cartella con richieste a ollama server.
#Le risposte sono date in file JSON perchè lo script è pensato per testare modelli istruiti a rispondere in JSON. 

model=$1
promptDir=$2
answerDir=$3

if [ $# -eq 3 ]; then
	if [ -d "$promptDir" ]; then
		if [ ! -d "$answerDir" ]; then
			mkdir $answerDir
		fi
		for filename in $promptDir/*.txt
		do
			name=$(basename "$filename")
			echo "elaborating $name"
			bash call-ollama-server.sh $model $filename $answerDir
		done

		echo "END"

	else echo "Error: prompt directory does not exist"

	fi
else echo "Error! The arguments are 3: model, prompt directory and answer directory."
fi
