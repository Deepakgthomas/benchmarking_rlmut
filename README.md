# Benchmarking RLMutation [1]


Prerequisite - 
1. Similar to [1], we use `Python 3.8`
2. The tool was written using `Ubuntu 22.04.3 LTS` with PyCharm Community as the IDE


Steps for execution - 


1. Clone the official [RLMutation](https://github.com/FlowSs/RLMutation.git) repository

2. Go [here](https://zenodo.org/records/7233122) and download "agents.zip".

3. Unzip the folders "Healthy_Agents" and "Mutated_Agents" in the directory "experiments". The folder structure should look like this - `RLMutation/experiments`

4. Install the custom gym environment -
```
cd custom_env/custom_cartpole/cartpole_folder 
pip install -e .
```

5. Install the packages for RLMutation
```commandline
cd RLMutation
pip install -r requirements.txt
```

6. We want to run the trained agents downloaded in step 3. on our own environments, without significantly modifying the programs written by [1]. Their RL testing program searches for a trained agent using a path that contains the name of the current environment. Therefore, we need to rename the folders in the `experiments` directory using the names of our environments.
```commandline
bash rename_folders.sh environment_name algorithm_name [incomplete]
```

7. To evaluate the trained agents on our test environments run - 
```commandline
bash run_test_agent.sh
```

8. To get the results of the mutation testing process run - 
```commandline
bash mutation_results.sh
```
The results should be stored in the file - `output.txt`

[1]. Tambon, Florian, et al. "Mutation Testing of Deep Reinforcement Learning Based on Real Faults." 2023 IEEE Conference on Software Testing, Verification and Validation (ICST). IEEE, 2023.