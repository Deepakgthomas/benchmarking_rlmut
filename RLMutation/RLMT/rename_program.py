import os
import sys
import argparse
full_path = os.path.abspath(os.path.dirname(__file__))

parent_directory = os.path.dirname(full_path)

def rename_folders(directory_path, old_substring, new_substring):
    if os.path.exists(directory_path):

        for folder_name in os.listdir(directory_path):
            old_folder_path = os.path.join(directory_path, folder_name)

            # Check if it's a directory
            if os.path.isdir(old_folder_path):

                '''
                This is needed when benchmark_rlmutation.py detects that the parent directory has already been renamed. 
                However, the child directory within the logs folder is yet to be renamed. 
                This is because the parent directory, for instance, 
                RLMutation/experiments/Mutated_Agents/SingleOrderMutation/incorrect_loss_function/CartPole-v1,
                has multiple algorithms, namely DQN, PPO and A2C associated with it. 
                '''
                # Replace the specified substring in the folder name
                if old_substring==new_substring and old_substring not in folder_name and "logs" in old_folder_path:
                    if "CartPole" in old_substring:
                        old_substring="CartPole-v1"
                    else:
                        old_substring="LunarLander-v2"
                new_folder_name = folder_name.replace(old_substring, new_substring)


                # Construct the full paths for the old and new folders
                older_folder_path = os.path.join(directory_path, folder_name)
                new_folder_path = os.path.join(directory_path, new_folder_name)

                try:
                    # Rename the folder
                    os.rename(older_folder_path, new_folder_path)
                    # print(f"Folder '{folder_name}' successfully renamed to '{new_folder_name}'.")
                except FileExistsError:
                    print(f"Error: Folder '{new_folder_name}' already exists.")

    else:
        '''
        This error might occur if you are directly using the Bash programs developed to 
        rename environments for multiple algorithms
        '''

        print("Path ",  directory_path, " doesn't exist")


parser = argparse.ArgumentParser()
parser.add_argument('agent_type', help = 'Enter whether the agent is healthy or mutated')
parser.add_argument('old_environment_name', help='Enter the name of the environment name you want to replace')
parser.add_argument('new_environment_name', help='Enter the name of the environment name you want to replace your old name with')
parser.add_argument('-op', '--operator', required=False,help = 'Enter the name of the mutation operator')
parser.add_argument('-algo', '--algorithm', required=False,help='Enter the name of the algorithm')
parser.add_argument('-op_val', '--operator_value', required=False ,help = 'Enter the value of the operator parameter')
args = parser.parse_args()

'''
first_dir_path addresses the immediate child folders corresponding to the folders inside the logs directory. For instance: 
/benchmarking_rlmut/RLMutation/experiments/Mutated_Agents/SingleOrderMutation/incorrect_loss_function/mymyCartPole-v1/PPO/logs/ILF_ppo_myCartPole-v1_0

second_dir_path addresses the immediate child folders corresponding either to the Healthy_Agents or Mutated_Agents directory
'''

if args.agent_type=='healthy':
    if args.old_environment_name in {"CartPole-V1", "LunarLander-V2"}:
        '''
        The capital V in -V will pose a problem. Manually changing it to v
        '''
        dir_path = str(parent_directory) + '/experiments/Healthy_Agents'
        old_substring = args.old_environment_name
        new_substring = args.old_environment_name[:-2] + args.old_environment_name[-2:].lower()
        rename_folders(dir_path, old_substring, new_substring)
        args.old_environment_name = args.old_environment_name[:-2] + args.old_environment_name[-2:].lower()



    first_dir_path = str(parent_directory) + '/experiments/Healthy_Agents/'+str(args.old_environment_name)+'/'+str(args.algorithm)+'/logs'
    second_dir_path = str(parent_directory) + '/experiments/Healthy_Agents'


elif args.agent_type=='mutated':



    if args.operator_value!="None":
        first_dir_path = str(parent_directory) + '/experiments/Mutated_Agents/SingleOrderMutation/' + str(args.operator) + '/'+str(args.old_environment_name)+'/'+str(args.algorithm)+'/' + str(args.operator_value) + '/logs'
        second_dir_path = str(parent_directory) + '/experiments/Mutated_Agents/SingleOrderMutation/' + str(args.operator)

    else:
        first_dir_path = str(parent_directory) + '/experiments/Mutated_Agents/SingleOrderMutation/' + str(args.operator) + '/'+str(args.old_environment_name)+'/'+str(args.algorithm)+'/logs'
        second_dir_path = str(parent_directory) + '/experiments/Mutated_Agents/SingleOrderMutation/' + str(args.operator)




else:
    print("There's an error")
    sys.exit()


old_substring = str(args.old_environment_name)

new_substring = str(args.new_environment_name)

'''
"policy_activation_change" operator is a special case as it has two corresponding values - ReLU and Sigmoid
Therefore, the program has to traverse through some paths multiple times. However, the second time a path is traversed, the names of
some folders in the path would have changed and would need to be updated. 
'''
if args.operator == "policy_activation_change" and not os.path.exists(first_dir_path):
    first_dir_path = str(parent_directory) + '/experiments/Mutated_Agents/SingleOrderMutation/' + str(args.operator) + '/' + str(args.new_environment_name) + '/' + str(args.algorithm) + '/' + str(args.operator_value) + '/logs'
    second_dir_path = str(parent_directory) + '/experiments/Mutated_Agents/SingleOrderMutation/' + str(args.operator)
    rename_folders(first_dir_path, old_substring, new_substring)
else:
    rename_folders(first_dir_path, old_substring, new_substring)
    rename_folders(second_dir_path, old_substring, new_substring)

