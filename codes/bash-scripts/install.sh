#!/bin/bash

appList="pip p7zip-full zip unzip"
pipList="langchain langchain-ollama langchain-experimental"
sudo apt update
sudo apt-get -y install $appList
pip install $pipList

#curl -fsSL https://ollama.com/install.sh | sh


#echo PATH=$PATH:/my/dir >> ~/.bashrc
#source ~/.bashrc

