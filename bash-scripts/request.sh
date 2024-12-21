MODEL_DIR=$1
FILE=$2
OUTPUT_FILENAME=$3
TMP=tmp.json
FORMAT='{"type":"array","items":{"type":"object","properties":{"Comune":{"type":"string"},"Indirizzo":{"type":"string"},"Vani":{"type":"number"},"Locali":{"type":"integer"},"Mq":{"type":"number"},"Bagni":{"type":"integer"},"Piano":{"type":"string"},"Posti auto":{"type":"string"},"N° Procedura":{"type":"string"},"Lotto":{"type":"string"}},"required":["Comune","Indirizzo","Vani","Locali","Mq","Bagni","Piano","Posti auto","N° Procedura","Lotto"]}}'
FILE=$( cat $FILE | jq -Rsa . )
DATA='{ "model": "test", "modelfile": "'$MODEL_DIR'", "prompt": '$FILE', "stream":false, "format": '$FORMAT' }'
echo $DATA > $TMP
curl http://localhost:11434/api/generate -d @tmp.json > $OUTPUT_FILENAME
rm $TMP