
# TBar
This repository is used to replicate the experiments of article **"Towards Effective Multi-Hunk Bug Repair: Detecting, Creating, Evaluating, and Understanding Indivisible Bugs"** on TBar. 

If you want to learn more about TBar, please follow the original repository of [TBar](https://github.com/TruX-DTF/TBar).



## 1. Modification

 We change the a field `isTestFixPatterns` in `edu.lu.uni.serval.tbar.AbstractFixer` from **false** to **true**, so that it can generate more plausible patches. This makes it fairer to compare with other tools.




## 2. Environment
 - JDK 1.8
 - Python 3.8
 - [Defects4J 2.0.0](https://github.com/rjust/defects4j)
- [CatenaD4J](https://github.com/universetraveller/CatenaD4J)



### 3. Experiment Setup

- Timeout: 5h



### 4. Excluded Bug

> None



## 5. Installation

#### 5.1 Create the docker image

Use the `Dockerfile` in `./Docker` to create the docker image.

```shell
docker build -t tbar-env .
```

This docker image includes **Defects4J**, **CatenaD4J**, **JDK 1.8**, and **Python 3.8**.

#### 5.2 Create the container with this image

AlphaRepair requires the use of GPU, otherwise generating the patch part would be very slow.

```shell
docker run -it --name tbar tbar-env /bin/bash
```

#### 5.3 Clone the TBar repository

At the root of this container, we clone the TBar repository.

```shell
cd /
git clone https://github.com/give-to/TBarAPI.git
cd TBarAPI/ && chmod +x *
```



## 6. Quick Test

It takes several minutes to quickly test your installation. (**Note:** In quick test, the `ochiai.ranking.txt` in Chart_18_2 only contains one location! )

```shell
cp C4J_location/105SampleBugsResult/Chart_18_2/short.txt C4J_location/105SampleBugsResult/Chart_18_2/ochiai.ranking.txt
# Test your environment
python3 runTBarForCatenaD4J.py 0 0 /TBarAPI test.txt /defects4j
```

After finishing the repair, the results are in folders: `OUTPUT`.

Note: If you do not get any results, you can go to `/tbar_log/TBar.log` for more information.



## 7. Experiment Reproduction

It may take about **22 days** to finish the entire experiment. You can also modify `105_bugs_list.txt` to determine the bugs to be fixed.

```shell
cp C4J_location/105SampleBugsResult/Chart_18_2/backup.txt C4J_location/105SampleBugsResult/Chart_18_2/ochiai.ranking.txt
rm -rf OUTPUT/
# Run the whole experiment
python3 runTBarForCatenaD4J.py 0 104 /TBarAPI 105_bugs_list.txt /defects4j
```

After finishing the repair, the results are in folders: `OUTPUT`.



## 8. Structure of the Directories

 ```powershell
  |--- README.md               :  user guidance
  |--- C4J_location            :  Bug positions localized with GZoltar of CatenaD4J bugs
  |--- C4J_results             :  Generated patches of CatenaD4J bugs
  |--- D4J                     :  Defects4J information
  |--- Docker                  :  Dockerfile
  |--- Results                 :  Generated patches of Defects4J bugs
  |--- src                     :  source code
  |--- target                  :  binary code
 ```
