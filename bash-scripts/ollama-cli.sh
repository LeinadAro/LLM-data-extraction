#!/bin/bash

#scrpit per usare modello ollama da linea di comando con un prompt. In output oltre alla risposta del modello viene stampato anche il tempo di esecuzione del modello in secondi.

model=$1
prompt=$2

if [ $# -eq 2 ]; then
	if [ -f "$prompt" ]; then
		start_time=$(date +%s.%N)

		ollama run $model < $prompt

		end_time=$(date +%s.%N)

		runtime=$( echo "$end_time - $start_time" | bc )
		echo "The script took $runtime seconds to execute."

	else echo "Error: Prompt file does not exist."

	fi
else echo "Error! The arguments are 2: model, prompt path."
fi