#!/bin/bash

appList="pip p7zip-full zip unzip"
pipList="langchain langchain-ollama langchain-experimental transformers datasets evaluate accelerate torch huggingface_hub[cli]"
sudo apt update
sudo apt upgrade
sudo apt install linux-headers-amd64
sudo apt install nvidia-driver firmware-misc-nonfree
sudo apt-get -y install $appList
pip install -U  $pipList

curl -fsSL https://ollama.com/install.sh | sh

FILE=~/.bash_aliases
if [ ! -f "$FILE" ]; then
	touch $FILE
	echo "alias python=python3" >> $FILE
	#echo PATH=$PATH:/my/dir >> ~/.bashrc
	source $FILE
	source ~/.bashrc
fi

