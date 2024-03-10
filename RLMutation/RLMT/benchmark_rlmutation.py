
import os

import subprocess
import sys
import shutil


# directory ="/home/thoma/benchmarking_rlmut/RLMutation"
# os.chdir(directory)
# def rename_files(environment, algorithm, test_generator_type, agent_type):
#     current_directory = os.getcwd()
#     parent_directory = os.path.dirname(current_directory)
#     if agent_type=="mutated":
#         target_directory = os.path.join(parent_directory,
#                                         "experiments/Mutated_Agents/SingleOrderMutation/incorrect_loss_function")
#     else:
#         target_directory = os.path.join(parent_directory,
#                                         "experiments/Healthy_Agents")
#     print("target_directory = ", target_directory)
#
#     # Identifying old environment name
#     items = os.listdir(target_directory)
#     # Filter out the folders
#     folders = [item for item in items if os.path.isdir(os.path.join(target_directory, item))]
#
#     # look for folder with environment name in it. There should be 2 folders, one for cartpole and one for lunarlander
#     environment_with_cap_V = environment[:-2] + environment[-2].upper() + environment[-1]
#
#     folders_with_substring = [folder for folder in folders if environment in folder or environment_with_cap_V in folder]
#     # Exactly one folder should be selected. Anything other than one implies a bug.
#     print("folders_with_substring = ", folders_with_substring)
#     if (len(folders_with_substring)) != 1:
#         print("There's a serious bug")
#         print("Exiting")
#         sys.exit()
#
#     old_environment_name = folders_with_substring[0]
#     # new_environment_name = test_generator_type + "_" + algorithm + "_" + environment
#     if "CartPole" in old_environment_name:
#         new_environment_name="myCartPole-v1"
#     elif "LunarLander" in old_environment_name:
#         new_environment_name="myLunarLander-v1"
#     else:
#         print("There's going to be an error")
#
#     print("old_environment_name = ", old_environment_name)
#     print("new_environment_name = ", new_environment_name)
#     algorithm_name = algorithm.upper()
#     if agent_type=="mutated":
#         rename_program_script = "/home/thoma/benchmarking_rlmut/RLMutation/RLMT/rename_folders_mutated.sh"
#     else:
#         rename_program_script = "/home/thoma/benchmarking_rlmut/RLMutation/RLMT/rename_folders_healthy.sh"
#     command = ["bash", rename_program_script, old_environment_name, new_environment_name, algorithm_name]
#     process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     stdout, stderr = process.communicate()
#
#     print("Standard Output:")
#     print(stdout.decode())
#     print("Standard Error:")
#     print(stderr.decode())
#
#     # Get the return code
#     return_code = process.returncode
#     print("Return Code:", return_code)
#     return new_environment_name

def run_test(new_environment_name, algorithm):
    print("Running test")
    test_agent_script = "/home/thoma/benchmarking_rlmut/RLMutation/RLMT/run_test_agent.sh"
    print("new_environment_name = ", new_environment_name)
    print("algorithm = ", algorithm)
    command = ["bash", test_agent_script, new_environment_name, algorithm]
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    print("Standard Output:")
    print(stdout.decode())
    print("Standard Error:")
    print(stderr.decode())

    # Get the return code
    return_code = process.returncode
    print("Return Code:", return_code)


def compute_mutation_results(new_environment_name, algorithm, test_generator_type, mutant_type_from_file):
    print("Mutation Results")
    test_agent_script = "/home/thoma/benchmarking_rlmut/RLMutation/RLMT/mutation_results.sh"
    command = ["bash", test_agent_script, new_environment_name, algorithm, test_generator_type, mutant_type_from_file]
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    print("Standard Output:")
    print(stdout.decode())
    print("Standard Error:")
    print(stderr.decode())

    # Get the return code
    return_code = process.returncode
    print("Return Code:", return_code)
#todo Check if os.walk uses dfs to traverse trees

def rename():
    old_environment_name=""
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
                    folders = [item for item in items if os.path.isdir(os.path.join(target_directory, item))]
                    folders_with_substring = [folder for folder in folders if new_environment_name in folder]
                    print("folders_with_substring = ", folders_with_substring)
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
                command = ["bash", rename_program_script, old_environment_name, new_environment_name, algos]
                process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = process.communicate()
                print("Standard Output:")
                print(stdout.decode())
                print("Standard Error:")
                print(stderr.decode())

                # Get the return code
                return_code = process.returncode
                print("Return Code:", return_code)

def print_txt_files(directory):
    # # new_environment_name = ""
    # # old_environment_name = ""
    # print("Renaming Mutants")
    # new_environment_name = rename_files(environment, algorithm, test_generator_type, "mutated")
    # print("Renaming Healthy Agents")
    # new_environment_name = rename_files(environment, algorithm, test_generator_type, "healthy")
    # rename()
    for root, _, files in os.walk(directory):
        print("root")
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
                env_path = test_generator_type + "_" + algorithm + "_" + environment
                destination_folder = '/home/thoma/benchmarking_rlmut/RLMutation/RLMT/'+'testing'
                os.makedirs(destination_folder)

                shutil.copy(file_path, destination_folder)
                new_environment_name=""
                if environment=="CartPole-v1":
                    new_environment_name="myCartPole-v1"
                elif environment=="LunarLander-v2":
                    new_environment_name="myLunarLander-v1"
                run_test(new_environment_name, algorithm)
                shutil.rmtree(destination_folder)
                compute_mutation_results(new_environment_name, algorithm, test_generator_type, mutant_type_from_file)



# # Provide the top-level directory where your files are located
top_directory = 'configurations'
print_txt_files(top_directory)

# rename()