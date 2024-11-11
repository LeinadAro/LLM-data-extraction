#!/bin/bash

model = $1
promptDir = $2

start_time=$(date +%s.%N)

ollama run model < promptDir

end_time=$(date +%s.%N)

runtime=$( echo "$end_time - $start_time" | bc )
echo "The script took $runtime seconds to execute."
