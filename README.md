# Replication Package

For Taxonomy results, please go into the Taxonomy folder
# Benchmarking RLMutation [1]


Prerequisite - 
1. Similar to [1], we use `Python 3.8`
2. The tool was written using `Ubuntu 22.04.3 LTS` with PyCharm Community as the IDE


Steps for execution - 


1. Clone the official [RLMutation](https://github.com/FlowSs/RLMutation.git) repository (Note - It's already present for the moment) and create a new conda environment

```commandline
conda create --name benchmark_clean python=3.8
conda activate benchmark_clean
cd benchmarking_rlmut
```
2. Install the two custom gym environments, myCartPole-v1 and myLunarLander-v1. The environments were created based on instructions given [here](https://www.gymlibrary.dev/content/environment_creation/)

a. Installing myCartPole-v1
```
pip install -e custom_env/custom_cartpole 
```
b. Installing myLunarLander-v1
```
pip install -e custom_env/custom_lunarlander 
```

3. Change your directory to experiments. Go [here](https://zenodo.org/records/7233122) and download "agents.zip".
```commandline
cd experiments
wget https://zenodo.org/api/records/7233122/files-archive
unzip files-archive 
unzip agents.zip
rm -rf files-archive 
rm -rf agents.zip 
cd ..
```

4. Install the packages for RLMutation
```commandline
cd RLMutation
pip install -r requirements.txt
cd RLMT
```
5. To benchmark RLMutation against custom environment configurations, store them in a folder called configurations - `RLMutation/RLMT/configurations`
6. Run the python program `benchmark_rlmutation.py` after going into the directory `RLMutation/RLMT`

```commandline
python benchmark_rlmutation.py
```

How does the program work? 

1. RLMutation stores its saved models (that we want to use) using the environment name. Since we are using our own environments on their stored models, we'd like to rename those folders.  This allows RLMutation to still use those models. Therefore, the Python function `rename()` does that.
```commandline
bash rename_folders_mutated.sh old_environment_name new_environment_name algorithm_name
bash rename_folders_healthy.sh old_environment_name new_environment_name algorithm_name

```
For example - 
```commandline
bash rename_folders_mutated.sh CartPole-v1 myCartPole-v1 PPO
bash rename_folders_healthy.sh CartPole-V1 myCartPole-v1 PPO

```

2. To evaluate RLMutation's trained agents on our test environments, we use the function `run_test()`. This inturn calls the functions created by RLMutation to run their saved models on specified environments.
```commandline
bash run_test_agent.sh new_environment_name algorithm_name
```
For example - 
```commandline
bash run_test_agent.sh myCartPole-v1 ppo 
```

3. The final step involves computing the mutation scores.  
```commandline
bash mutation_results.sh new_environment_name algorithm_name test_generator_type mutant_type_from_file
```
For example - 
```commandline
bash mutation_results.sh myCartPole-v1 ppo strong gamma
```
The results should be stored in the file - `output_myCartPole-v1_ppo_strong_gamma_stdout_mutation_result.txt`. It consists of 3 mutation killing definitions for each operator. We are interested in "Distance Distribution Test"

[1]. Tambon, Florian, et al. "Mutation Testing of Deep Reinforcement Learning Based on Real Faults." 2023 IEEE Conference on Software Testing, Verification and Validation (ICST). IEEE, 2023.