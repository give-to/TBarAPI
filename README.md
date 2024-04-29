
# TBar
Template-based automated program repair. The source code are modified from official [TBar](https://github.com/TruX-DTF/TBar).


## 1. Environment
 - JDK 1.8
 - Python 3.8
 - [Defects4J 2.0.0](https://github.com/rjust/defects4j)
- [CatenaD4J](https://github.com/universetraveller/CatenaD4J)



## 2. Installation

#### 2.1 Create the docker image

Use the `Dockerfile` in `./Docker` to create the docker image.

```shell
docker build -t tbar-env .
```

This docker image includes **Defects4J**, **CatenaD4J**, **JDK 1.8**, and **Python 3.8**.

#### 2.2 Create the container with this image

AlphaRepair requires the use of GPU, otherwise generating the patch part would be very slow.

```shell
docker run -it --name tbar tbar-env /bin/bash
```

#### 2.3 Clone the TBar repository

At the root of this container, we clone the TBar repository.

```shell
cd /
git clone https://github.com/give-to/TBarAPI.git
```



## 3. Quick Test

Run the test experiment to ensure your environment is correct. This command takes a maximum of 5 hours.

```shell
# Test your environment
python3 runTBarForCatenaD4J.py 0 0 /TBarAPI test.txt /defects4j
```



## 4. Repeat whole experiments

```shell
# Run the whole experiment
python3 runTBarForCatenaD4J.py 0 104 /TBarAPI 105_bugs_list.txt /defects4j
```



 ## 5. Usage
Fixing CatenaD4J bugs with normal fault localization configuration. The following command reads the list of bugs in the `bug_list_file` and fixes them sequentially. The results will be stored in `OUTPUT` directory.

 - `python3 runTBarForCatenaD4J.py <start_index> <end_index> <tbar_Home> <bug_list_file> <defects4j_Home>`
   
   Where:
   
   - `start_index`: bug start index in `bug_list_file` file.
   - `end_index`: bug end index in `bug_list_file` file.
   - `tbar_Home`: the root directory of TBar.
   - `bug_list_file`: a file contains all the bugs to be fixed.
   - `defects4j_Home`: the root directory of Defects4J.
   



## 6. Structure of the Directories

 ```powershell
  |--- README.md               :  user guidance
  |--- D4J                     :  Defects4J information
  |--- FailedTestCases         :  Failed test cases of each Defects4J bug
  |--- lib                     :  GZoltar jar files
  |--- Results                 :  Generated patches
  |------ FixPatterns          :  Bugs fixed by each fix pattern
  |------ PerfectFL            :  Bugs fixed with perfect fault localization configuration
  |------ NormalFL             :  Bugs fixed with normal fault localization configuration
  |--- C4J_results             :  Generated patches of CatenaD4J bugs
  |--- src                     :  source code
  |--- SuspiciousCodePositions :  Bug positions localized with GZoltar
  |--- target                  :  binary code
 ```
