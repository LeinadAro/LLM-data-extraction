#!/bin/bash

appList="pip p7zip-full zip unzip huggingface_hub[cli]"
pipList="langchain langchain-ollama langchain-experimental"
sudo apt update
sudo apt upgrade
sudo apt install linux-headers-amd64
sudo apt install nvidia-driver firmware-misc-nonfree
sudo apt-get -y install $appList
pip install $pipList

curl -fsSL https://ollama.com/install.sh | sh

touch ~/.bash_aliases
echo "alias python=python3" >> ~/.bash_aliases
#echo PATH=$PATH:/my/dir >> ~/.bashrc
source ~/.bash_aliases
source ~/.bashrc

