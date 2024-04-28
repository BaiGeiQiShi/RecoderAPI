# Recoder

## 1. Environment

- Ubuntu 20.04
- docker
- nvidia-docker
- GPUs should support CUDA and the version should be advanced than 11.0
- Python >=3.7
- JDK 1.8
- [Defects4J 2.0](https://github.com/rjust/defects4j)
- [CatenaD4J](https://github.com/universetraveller/CatenaD4J.git)


## 2. Installation

#### 2.1 Create the docker image
Use the `Dockerfile` in `./Docker` to create the docker image.
```shell
docker build -t recoder-env .
```


#### 2.2 Create the docker container
```
docker run -it --gpus all --name=recoder --shm-size="1g" recoder-env /bin/bash
 ```

#### 2.3 Clone the Recoder repository
At the root of this container, we clone the Recoder repository.

```shell
cd /
git clone https://github.com/BaiGeiQiShi/RecoderAPI.git
```

#### 2.4 Setup
Install the additonal dependencies.
```shell
cd ./RecoderAPI
./setup.sh
```

## 3. Quick Test
```
# Generating the patches

cd 105_bugs_with_src_backup
catena4j checkout -p Chart -v 18b2 -w ./Chart18b2
cd ..
cp -r 105_bugs_with_src_backup/* 105_bugs_with_src
./recd_generate.sh
```

The generated patches are located in `./patches/$BUG_ID.txt`. Each line of code represents a patch. Each line is divided by `,` into 3 parts. The first part is **buggy file path**. The second part is **buggy line in the buggy file**. The third part is **patch** ([here](rules.md) is the rule for reading patches).
<br>
<br>

Recoder records the time of generating patches in `time-info-gen.txt`. Then we use `recd_validate.sh` to validate patches in the remaining time budget (5 hours - $TIME_TO_GENERATE_PATCHES).
```
# Validate the patches
./recd_validate.sh
```



## 4. Usage
You should first checkout the 105 bugs in Catena4j and then repair these 105 bugs
```
# Checkout 105 bugs
./checkout_105.sh

# Generate the patches
./recd_generate.sh

# Validate the patches
./recd_validate.sh
```

If you have any questions, you can go to the [Recoder](https://github.com/pkuzqh/Recoder.git) repository or create issues for more information.
