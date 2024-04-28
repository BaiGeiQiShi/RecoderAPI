#!/bin/bash -i
echo "======================================="
echo "@: Please input y yes ENTER if the installations request"
echo "================Set up================="
echo "@: Detecting conda installation"
if test -z "$(conda -V)"; then
	echo "@: Trying to install conda with python3.9"
	echo "@: Updating apt-get"
	echo "=================="
	apt-get update
	echo "@: Trying to install wget"
	echo "=================="
	apt-get install wget
	echo "@: Download conda with wget now"
	wget https://repo.anaconda.com/archive/Anaconda3-2022.05-Linux-x86_64.sh -O ~/anaconda.sh
	bash ~/anaconda.sh -p $HOME/anaconda
	rm ~/anaconda.sh
	source ~/.bashrc
fi
echo "@: You have installed $(conda -V)"
echo "@: Please ensure your python version is advanced than 3.7 to use the tool"
echo "@: Trying to install cudatoolkit, ignore it if you have installed"
conda install cudatoolkit==11.3.1
echo "@: Trying to install cudnn"
conda install cudnn==8.2.1
echo "@: Trying to install torch"
pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu113
echo "@: Installing requirements"
pip3 install -r requirements.txt

mkdir 105_bugs_with_src
mkdir 105_bugs_with_src_backup
echo "END OF SCRIPT"
