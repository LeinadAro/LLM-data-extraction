#!/bin/bash

#Script per inviare a ollama server una richiesta effettuata con JSON schema come format per l'output strutturato.
#La risposta è data in file JSON perchè lo script è pensato per testare modelli istruiti a rispondere in JSON. 


MODEL=$1
FILENAME=$2
ANSWERS_DIR=$3

if [ $# -eq 3 ]; then
	if [ -f "$FILENAME" ]; then

		if [ ! -d "./$ANSWERS_DIR" ]; then
			mkdir ./$ANSWERS_DIR
		fi
		
		TMP=tmp.json
		FORMAT='{"type":"array","items":{"type":"object","properties":{"Comune":{"type":"string"},"Indirizzo":{"type":"string"},"Vani":{"type":"number"},"Locali":{"type":"integer"},"Mq":{"type":"number"},"Bagni":{"type":"integer"},"Piano":{"type":"string"},"Posti auto":{"type":"string"},"N° Procedura":{"type":"string"},"Lotto":{"type":"string"}},"required":["Comune","Indirizzo","Vani","Locali","Mq","Bagni","Piano","Posti auto","N° Procedura","Lotto"]}}'

		FILE=$( cat $FILENAME | jq -Rsa . )
		DATA='{ "model": "'$MODEL'", "prompt": '$FILE', "stream":false, "format": '$FORMAT' }'
		echo $DATA > $TMP
		OUTPUT_FILENAME=$(basename "$FILENAME" '.txt')'.json'
		timeout 300 curl http://localhost:11434/api/generate -d @tmp.json > $OUTPUT_FILENAME	#timeout a 5 min per tagliare risposte troppo lunghe
		
		echo $( (cat $OUTPUT_FILENAME) | jq -r .response ) > ./$ANSWERS_DIR/$OUTPUT_FILENAME	#estrae la risposta del modello dal file creato da ollama server che contiene anche altri dati
		rm $TMP
		rm $OUTPUT_FILENAME		#rimuove risposta grezza di ollama
		
	else echo "Error: Prompt file does not exist."

	fi
else echo "Error! The arguments are 3: model, prompt path, answer directory."
fi