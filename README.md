# benchmarking_rlmut
Prerequisite - 
1. The authors of the RLMut used `Python 3.8`
2. We used `Ubuntu 22.04.3 LTS` with PyCharm Community for the benchmarking process


Steps for execution - 

1. Go [here](https://zenodo.org/records/7233122) and download "agents.zip".

2. Unzip the folders "Healthy_Agents" and "Mutated_Agents" in the directory "experiments".

3. Go to `custom_env/custom_cartpole/cartpole_folder` and do `pip install -e .`

4. Go to `RLMutation` and do `pip install -r requirements.txt`
5. 
```commandline
   
    cd RLMutation/RLMT/
```
6. To run RLMut with our own version of environments, we need to rename a few folders. Therefore, please run - 
```commandline
    bash rename_folders.sh
```

7. To evaluate the trained agents on our test environments run - 
```commandline
    bash run_test_agent.sh
```

8. To get the results of the mutation testing process, do - 
```commandline
    bash mutation_results.sh
```