# Recoder

We reformat the patches of Recoder according to this [rule](rules.md) for the convenience of result statistics.

## 1. Environment

- Ubuntu 20.04
- JDK 1.8
- Python 3.8
- CUDA 11.3.1
- cudnn 8.2.1
- torch 1.13.1
- [Defects4J 2.0](https://github.com/rjust/defects4j)
- [CatenaD4J](https://github.com/universetraveller/CatenaD4J.git)


## 2. Experiment Setup
- Timeout: 5h


## 3. Excluded Bug
> None.


## 4. Installation
#### 4.1 Create the docker image
Use the `Dockerfile` in `./Docker` to create the docker image.
```shell
docker build -t recoder-env .
```

#### 4.2 Create the docker container
```
docker run -it --gpus all --name=recoder --shm-size="1g" recoder-env /bin/bash
 ```

#### 4.3 Clone the Recoder repository
At the root of this container, we clone the Recoder repository.

```shell
cd /
git clone https://github.com/BaiGeiQiShi/RecoderAPI.git
```

#### 4.4 Setup
① Install the additonal dependencies.
```shell
cd ./RecoderAPI
./setup.sh
source ~/.bashrc
```
② [Download](https://drive.google.com/file/d/1XWyx-uPOnV0tEIMaWTkAd3yaaxYD-sbh/view?usp=drive_link) the pre-trained model in the `RecoderAPI` directory and unzip this model.
```
unzip ./checkpointSearch.zip
```


## 5. Quick Test
```
# Generate the patches
cd 105_bugs_with_src_backup
catena4j checkout -p Chart -v 18b2 -w ./Chart18b2
cd ..
cp 105BugsFL/Chart_18_2/* 105_bugs_with_src_backup/Chart18b2/
cp -r 105_bugs_with_src_backup/* 105_bugs_with_src
./recd_generate.sh
```

The generated patches are located in `./patches/Chart18b2.txt`. Each line of code represents a patch. Each line is divided by `,` into 3 parts. The first part is **buggy file path**. The second part is **buggy line in the buggy file**. The third part is **patch** ([here](rules.md) is the rule for reading patches).
<br>
<br>

Recoder records the time of generating patches in `time-info-gen.txt`. Then we use `recd_validate.sh` to validate patches in the remaining time budget (5 hours - $TIME_TO_GENERATE_PATCHES).
```
# Validate the patches
./recd_validate.sh
```

The results are located in `./final/Chart18b2.txt`. At the end of each line, there are **Fail**, **Pass**, and **Build Error**.
- **Fail**: After applying this patch, the compilation is successful, but the bug is not fixed.
- **Pass**: This patch is plausible.
- **Build Error**: After applying this patch, the compilation is failed.


## 6. Experiment Reproduction
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
