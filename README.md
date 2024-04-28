# Recoder

## 1. Environment

- Ubuntu 20.04
- docker
- nvidia-docker
- Python 3.7
- PyTorch 1.3
- JDK 1.8
- [Defects4J 2.0](https://github.com/rjust/defects4j)
- [CatenaD4J](https://github.com/universetraveller/CatenaD4J.git)


## 2. Installation

#### 2.1 Pull the docker image
We directly use the image provided by [Recoder](https://github.com/pkuzqh/Recoder.git).

```sudo docker pull zqh111/recoder:interface ```

#### 2.2 Create the docker container
```
docker run -it --gpus all --name=recoder --shm-size="1g" zqh111/recoder:interface /bin/bash
 ```

#### 2.3 Install dependencies
To prepare the environment, you need to install some additional dependencies

```
pip install -r requirements.txt
git clone https://github.com/universetraveller/CatenaD4J.git
export PATH=\$PATH:/CatenaD4J" >> ~/.bashrc && export PATH=$PATH:/CatenaD4J
git clone https://github.com/BaiGeiQiShi/RecoderAPI.git
```


## 3. Quick Test
```
# Generating the patches
cd ./RecoderAPI

cd 105_bugs_with_src_backup
catena4j checkout -p Chart -v 18b2 -w ./Chat18b2
cd ..
cp -r 105_bugs_with_src_backup/* 105_bugs_with_src
./recd_generate.sh
```

```
# Validate the patches
./recd_validate.sh
```


## 4. Usage
You should first checkout the bug in Catena4j
```
# Generate the patches

# Validate the patches

```

If you have any questions, you can go to the [Recoder](https://github.com/pkuzqh/Recoder.git) repository or create issues for more information.
