# benchmarking_rlmut

Steps for execution - 

1. Go [here](https://zenodo.org/records/7233122) and download "agents.zip".

2. Unzip the folders "Healthy_Agents" and "Mutated_Agents" in the directory "experiments".

3. Go to `custom_env/custom_cartpole/cartpole_folder` and do `pip install -e .`

4. Go to `RLMutation` and do `pip install -r requirements.txt`

5. To run RLMut with our own version of environments, we need to rename a few folders. Therefore, please run - 
```commandline
    bash /RLMutation/RLMT/rename_folders.sh
```

6. To evaluate the trained agents on our test environments run - 
```commandline
    bash /RLMutation/RLMT/run_test_agent.sh
```

7. To get the results of the mutation testing process, do - 
```commandline
    bash /RLMutation/RLMT/mutation_results.sh
```