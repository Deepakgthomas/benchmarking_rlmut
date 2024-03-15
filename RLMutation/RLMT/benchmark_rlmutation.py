
import os
import subprocess
import sys
import shutil


def run_test(new_environment_name, algorithm):
    stdout_file_name = str(misc_stdout_err)+ "/" + str(new_environment_name)+"_"+str(algorithm)+"_"+"stdout_test.txt"
    stderr_file_name = str(misc_stdout_err)+ "/" + str(new_environment_name)+"_"+str(algorithm)+"_"+"stderr_test.txt"

    test_agent_script = "run_test_agent.sh"

    command = ["bash", test_agent_script, new_environment_name, algorithm]

    with open(stdout_file_name, "w") as stdout, open(stderr_file_name, "w") as stderr:
        result = subprocess.run(command, stdout=stdout, stderr=stderr, check=True)



def compute_mutation_results(new_environment_name, algorithm, test_generator_type, mutant_type_from_file):
    stdout_file_name = str(results_dir)+ "/"+ str(new_environment_name)+"_"+str(algorithm)+"_"+str(test_generator_type)+"_"+str(mutant_type_from_file)+"_"+"stdout_mutation_result.txt"
    stderr_file_name = str(misc_stdout_err)+ "/"+ str(new_environment_name)+"_"+str(algorithm)+"_"+str(test_generator_type)+"_"+str(mutant_type_from_file)+"_"+"stderr_mutation_result.txt"
    test_agent_script = "mutation_results.sh"
    command = ["bash", test_agent_script, new_environment_name, algorithm, test_generator_type, mutant_type_from_file]
    with open(stdout_file_name, "w") as stdout, open(stderr_file_name, "w") as stderr:
        result = subprocess.run(command, stdout=stdout, stderr=stderr, check=True)

#todo Check if os.walk uses dfs to traverse trees

def rename():
    old_environment_name=""
    '''
    These are the environment, RL agent and algorithm combinations we have
    '''
    environments = ["CartPole-v1", "LunarLander-v2"]
    agent_type=["Healthy", "Mutated"]
    algorithms=["PPO", "DQN"]
    for algos in algorithms:
        for env in environments:
            for agent in agent_type:
                if env=="CartPole-v1" and agent=="Healthy":
                    new_environment_name = "myCartPole-v1"
                    target_directory = os.path.join(os.path.dirname(os.getcwd()),
                                                    "experiments/Healthy_Agents")
                    items = os.listdir(target_directory)
                    # Identifying the original name of the environment, in order to modify it
                    folders = [item for item in items if os.path.isdir(os.path.join(target_directory, item))]
                    folders_with_substring = [folder for folder in folders if new_environment_name in folder]
                    if len(folders_with_substring)==0:
                        old_environment_name="CartPole-V1"
                    else:
                        old_environment_name=new_environment_name
                    rename_program_script="rename_folders_healthy.sh"

                elif env=="CartPole-v1" and agent=="Mutated":
                    new_environment_name="myCartPole-v1"
                    target_directory = os.path.join(os.path.dirname(os.getcwd()),
                                                    "experiments/Mutated_Agents/SingleOrderMutation/incorrect_loss_function")
                    items = os.listdir(target_directory)
                    folders = [item for item in items if os.path.isdir(os.path.join(target_directory, item))]
                    folders_with_substring = [folder for folder in folders if new_environment_name in folder]
                    if len(folders_with_substring)==0:
                        old_environment_name="CartPole-v1"
                    else:
                        old_environment_name=new_environment_name
                    rename_program_script="rename_folders_mutated.sh"
                elif env=="LunarLander-v2" and agent=="Healthy":
                    new_environment_name="myLunarLander-v1"
                    target_directory = os.path.join(os.path.dirname(os.getcwd()),
                                                    "experiments/Healthy_Agents")
                    items = os.listdir(target_directory)
                    folders = [item for item in items if os.path.isdir(os.path.join(target_directory, item))]
                    folders_with_substring = [folder for folder in folders if new_environment_name in folder]
                    if len(folders_with_substring)==0:
                        old_environment_name="LunarLander-V2"
                    else:
                        old_environment_name=new_environment_name
                    rename_program_script="rename_folders_healthy.sh"
                elif env=="LunarLander-v2" and agent=="Mutated":
                    new_environment_name="myLunarLander-v1"
                    target_directory = os.path.join(os.path.dirname(os.getcwd()),
                                                    "experiments/Mutated_Agents/SingleOrderMutation/incorrect_loss_function")
                    items = os.listdir(target_directory)
                    folders = [item for item in items if os.path.isdir(os.path.join(target_directory, item))]
                    folders_with_substring = [folder for folder in folders if new_environment_name in folder]
                    if len(folders_with_substring)==0:
                        old_environment_name="LunarLander-v2"
                    else:
                        old_environment_name=new_environment_name
                    rename_program_script="rename_folders_mutated.sh"

                # Calling the bash operations here
                stdout_file_name = str(misc_stdout_err)+ "/" + str(new_environment_name) + "_" + str(algos) + "_" + "stdout_rename.txt"
                stderr_file_name = str(misc_stdout_err)+ "/" + str(new_environment_name) + "_" + str(algos) + "_" + "stderr_rename.txt"
                command = ["bash", rename_program_script, old_environment_name, new_environment_name, algos]
                with open(stdout_file_name, "w") as stdout, open(stderr_file_name, "w") as stderr:
                    result = subprocess.run(command, stdout=stdout, stderr=stderr, check=True)


def run_tool(directory):


    '''
    The first step involves calling the rename function. It renames the stored
    RL model folders with our environment names
    '''

    rename()

    for root, _, files in os.walk(directory):
        root_substring = root.rsplit("/",1)[-1]
        if root_substring == "CartPole-v1" or root_substring == "LunarLander-v2":
            environment = root_substring
        elif root_substring == "ppo" or root_substring == "dqn":
            algorithm = root_substring
        elif root_substring == "strong" or root_substring == "weak":
            test_generator_type = root_substring
        for file in files:
            print("file = ", file)
            if file.endswith('.txt'):
                parts = file.split("-")
                mutant_type_from_file = parts[-2]
                file_path = os.path.join(root, file)

                # Create a temporary folder (destination_folder) folder from where the custom environments will take
                # the environment configuration files.
                destination_folder = 'testing'
                if os.path.exists(destination_folder):
                    # Delete the folder
                    shutil.rmtree(destination_folder)
                os.makedirs(destination_folder)
                shutil.copy(file_path, destination_folder)
                new_environment_name=""
                if environment=="CartPole-v1":
                    new_environment_name="myCartPole-v1"
                elif environment=="LunarLander-v2":
                    new_environment_name="myLunarLander-v1"

                '''
                The run_test() runs the stored models on our custom environment
                '''
                run_test(new_environment_name, algorithm)
                shutil.rmtree(destination_folder)
                '''
                The compute_mutation_results() computes the mutation score for each operator 
                corresponding to that environment and algorithm and outputs the result
                '''
                compute_mutation_results(new_environment_name, algorithm, test_generator_type, mutant_type_from_file)

results_dir = 'results_mutation_benchmark'
if os.path.exists(results_dir):
    print("Deleting old results")
    shutil.rmtree(results_dir)
os.makedirs(results_dir)
misc_stdout_err = 'stdout_err'
if os.path.exists(misc_stdout_err):
    shutil.rmtree(misc_stdout_err)
os.makedirs(misc_stdout_err)
def main():
    # # Provide the top-level directory where your files are located
    top_directory = 'configurations'
    run_tool(top_directory)

if __name__ == "__main__":
    main()