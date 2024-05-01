# Recoder
This repository is used to replicate the experiments of article **"Towards Effective Multi-Hunk Bug Repair: Detecting, Creating, Evaluating, and Understanding Indivisible Bugs"** on Recoder. If you want to learn more about Recoder, please follow the original repository of [Recoder](https://github.com/pkuzqh/Recoder.git).

## 1. Modification
We have made two modifications:

① Due to the high experimental cost in our paper, to maximize GPU load, we have separated the patch generation and patch validation of Recoder. Since Recoder does not have patch ranking, this separation will not negatively impact the experimental results of Recoder.

② We reformat the patches of Recoder according to this [rule](rules.md) for the convenience of result statistics.

## 2. Environment

- Ubuntu 20.04
- JDK 1.8
- Python 3.8
- CUDA 11.3.1
- cudnn 8.2.1
- torch 1.13.1
- [Defects4J 2.0](https://github.com/rjust/defects4j)
- [CatenaD4J](https://github.com/universetraveller/CatenaD4J.git)


## 3. Experiment Setup
- Timeout: 5h


## 4. Excluded Bug
> None.


## 5. Installation
#### 5.1 Create the docker image
Use the `Dockerfile` in `./Docker` to create the docker image.
```shell
docker build -t recoder-env .
```

#### 5.2 Create the docker container
```shell
docker run -it --gpus all --name=recoder --shm-size="1g" recoder-env /bin/bash
 ```

#### 5.3 Clone the Recoder repository
At the root of this container, we clone the Recoder repository.

```shell
cd /
git clone https://github.com/BaiGeiQiShi/RecoderAPI.git
```

#### 5.4 Setup
① Install the additonal dependencies.
```shell
cd ./RecoderAPI
chmod +x *
./setup.sh
source ~/.bashrc
```
② [Download](https://drive.google.com/file/d/1XWyx-uPOnV0tEIMaWTkAd3yaaxYD-sbh/view?usp=drive_link) the pre-trained model in the `RecoderAPI` directory and unzip this model.
```shell
unzip ./checkpointSearch.zip
```


## 6. Quick Test
It takes several minutes to quickly test your installation. (**Note:** In quick test, the `ochiai.ranking.txt` in Chart18b2 only contains one location！)

① Generate the patches
```
./recd_generate.sh
```

The generated patches are located in `./patches/Chart18b2.txt`. Each line of code represents a patch. Each line is divided by `,` into 3 parts. 
- The first part is **buggy file path**.
- The second part is **buggy line in the buggy file**.
- The third part is **patch** ([here](rules.md) is the rule for reading patches).

For example, one line of patch is shown below:
```
/RecoderAPI/105_bugs_with_src/Chart18b2/source/org/jfree/data/DefaultKeyedValues.java,318,insert-before:0$rebuildIndex();
```
- `/RecoderAPI/105_bugs_with_src/Chart18b2/source/org/jfree/data/DefaultKeyedValues.java` is **buggy file path**.
- `318` is **buggy line in the buggy file**.
- `insert-before:0$rebuildIndex();` is **patch**.

<br>

② Recoder records the time of generating patches in `time-info-gen.txt`. Then we use `recd_validate.sh` to validate patches in the remaining time budget (5 hours - $TIME_TO_GENERATE_PATCHES).
```
./recd_validate.sh
```

The results are located in `./final/Chart18b2.txt`. At the end of each line, there are **Fail**, **Pass**, and **Build Error**.
- **Fail**: After applying this patch, the compilation is successful, but the bug is not fixed.
- **Pass**: This patch is plausible.
- **Build Error**: After applying this patch, the compilation is failed.

For example, one line of patch is shown below:
```
/RecoderAPI/105_bugs_with_src/Chart18b2/source/org/jfree/data/DefaultKeyedValues.java:insert-before:0$rebuildIndex();:318:Pass
```
- `/RecoderAPI/105_bugs_with_src/Chart18b2/source/org/jfree/data/DefaultKeyedValues.java` is **buggy file path**.
- `insert-before:0$rebuildIndex();` is **patch**.
- `318` is **buggy line in the buggy file**.
- `Pass` means **This patch is plausible**.

## 7. Experiment Reproduction
It may take about **20 days** to finish the entire experiment. If you want to fully replicate our experiments on Recoder, please first checkout the 105 bugs in Catena4j and then repair these 105 bugs. You can also modify `105_bugs.txt` to determine the bugs to be fixed.
```
# Clean the quick test files
rm -rf 105_bugs_with_src/*
rm -rf 105_bugs_with_src_backup/*

# Checkout 105 bugs
./checkout_105.sh

# Generate the patches
./recd_generate.sh

# Validate the patches
./recd_validate.sh
```

## 8. Structure of the Directories
```
   |——./105_bugs_with_src/             //buggy project directory
   |——./105_bugs_with_src_backup/      //buggy project directory backup
   |——./105BugsFL/                     //FL results
   |——105_bugs.txt                    //bug_id list(only fix bugs within this file)
   |——time-info-gen.txt               //the time it takes to generate patches
   |——time-info.txt                   //the time it takes to generate and validate patches
   |——checkout_105.sh                 //download buggy project in 105_bugs.txt
   |——setup.sh                        //prepare environment
   |——requirements.sh                 //record necessary requirements
   |——recd_generate.sh                //start generate patches
   |——recd_validate.sh                //start validate patches
   |——./final/                         //patch validation results
   |——./patches/                       //patch generation results
```

If you have any questions, you can go to the [Recoder](https://github.com/pkuzqh/Recoder.git) repository or create issues for more information.
