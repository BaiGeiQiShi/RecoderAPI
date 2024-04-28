#!/bin/bash -x

pip3 install -r requirements.txt
cp .bashrc ~/.bashrc
source ~/.bashrc

echo "export PATH=/opt/conda/bin:/usr/local/nvidia/bin:/usr/local/cuda/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin" >> ~/.bashrc

cp -r ~/Repair/checkpointSearch ./

cd /

git clone https://github.com/rjust/defects4j.git
echo "export PATH=\$PATH:/defects4j" >> ~/.bashrc && export PATH=$PATH:/defects4j

git clone https://github.com/universetraveller/CatenaD4J.git
echo "export PATH=\$PATH:/CatenaD4J" >> ~/.bashrc && export PATH=$PATH:/CatenaD4J

source ~/.bashrc
