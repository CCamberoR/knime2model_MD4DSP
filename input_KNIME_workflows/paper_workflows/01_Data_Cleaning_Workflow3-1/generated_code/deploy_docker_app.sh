#!/bin/bash
set -e

if [ ! -d "data" ]; then
    mkdir -p data
fi

if [ ! -d "data/output" ]; then
    mkdir -p data/output
fi
if [ ! -d "data/output" ]; then
    mkdir -p data/output
fi
if [ ! -d "data/output" ]; then
    mkdir -p data/output
fi
if [ ! -d "data/output" ]; then
    mkdir -p data/output
fi
if [ ! -d "data/output" ]; then
    mkdir -p data/output
fi
if [ ! -d "data/output" ]; then
    mkdir -p data/output
fi
#sudo apt-get update --yes
#sudo apt-get install ca-certificates curl
#sudo install -m 0755 -d /etc/apt/keyrings
#sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
#sudo chmod a+r /etc/apt/keyrings/docker.asc

#echo \
#  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
#  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
#  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
#sudo apt-get update --yes

#sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin --yes

docker build --no-cache -t ubuntu_22_04:latest -f Dockerfile .

clear

cp /home/carlos/Escritorio/datasets/binner_input_dataDictionary.csv "$(pwd)/data/"output
cp /home/carlos/Escritorio/datasets/binner_output_dataDictionary.csv "$(pwd)/data/"output
cp /home/carlos/Escritorio/datasets/binner_output_dataDictionary.csv "$(pwd)/data/"output
cp /home/carlos/Escritorio/datasets/rowFilterPrimitive_output_dataDictionary.csv "$(pwd)/data/"output
cp /home/carlos/Escritorio/datasets/rowFilterPrimitive_output_dataDictionary.csv "$(pwd)/data/"output
cp /home/carlos/Escritorio/datasets/columnFilter_output_dataDictionary.csv "$(pwd)/data/"output




docker run -it --rm --name docker_python --network host --mount type=bind,source="$(pwd)/data",target=/wf_validation_python/data ubuntu_22_04:latest

docker rmi ubuntu_22_04:latest

clear

echo -e "Exiting the application...\n"
