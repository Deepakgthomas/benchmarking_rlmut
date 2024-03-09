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


                # Replace the specified substring in the folder name
                if old_substring==new_substring and old_substring not in folder_name and "logs" in old_folder_path:
                    if "CartPole" in old_substring:
                        old_substring="CartPole-v1"
                    else:
                        old_substring="LunarLander-v2"
                new_folder_name = folder_name.replace(old_substring, new_substring)
                print("old_substring = ", old_substring)
                print("new_substring = ", new_substring)

                print("new_folder_name = ", new_folder_name)

                # Construct the full paths for the old and new folders
                old_folder_path = os.path.join(directory_path, folder_name)
                new_folder_path = os.path.join(directory_path, new_folder_name)

                try:
                    # Rename the folder
                    os.rename(old_folder_path, new_folder_path)
                    # print(f"Folder '{folder_name}' successfully renamed to '{new_folder_name}'.")
                except FileExistsError:
                    print(f"Error: Folder '{new_folder_name}' already exists.")

    else:
        print("Path ",  directory_path, " doesn't exist")


parser = argparse.ArgumentParser()
parser.add_argument('agent_type', help = 'Enter whether the agent is healthy or mutated')
parser.add_argument('old_environment_name', help='Enter the name of the environment name you want to replace')
parser.add_argument('new_environment_name', help='Enter the name of the environment name you want to replace your old name with')
parser.add_argument('-operator', required=False,help = 'Enter the name of the operator')
parser.add_argument('-algorithm', required=False,help='Enter the name of the algorithm')
parser.add_argument('-op', required=False ,help = 'Enter the operator parameter')
parser.add_argument('-operator_repeat', required=False,help='En')
args = parser.parse_args()

if args.agent_type=='healthy':
    if args.old_environment_name in {"CartPole-V1", "LunarLander-V2"}:
        print("The capital V in -V will pose a problem. Manually changing it to v")
        dir_path = str(parent_directory) + '/experiments/Healthy_Agents'
        old_substring = args.old_environment_name
        new_substring = args.old_environment_name[:-2] + args.old_environment_name[-2:].lower()
        rename_folders(dir_path, old_substring, new_substring)
        args.old_environment_name = args.old_environment_name[:-2] + args.old_environment_name[-2:].lower()



    first_dir_path = str(parent_directory) + '/experiments/Healthy_Agents/'+str(args.old_environment_name)+'/'+str(args.algorithm)+'/logs'
    second_dir_path = str(parent_directory) + '/experiments/Healthy_Agents'


elif args.agent_type=='mutated':



    if args.op!="None":
        first_dir_path = str(parent_directory) + '/experiments/Mutated_Agents/SingleOrderMutation/' + str(args.operator) + '/'+str(args.old_environment_name)+'/'+str(args.algorithm)+'/' + str(args.op) + '/logs'
        second_dir_path = str(parent_directory) + '/experiments/Mutated_Agents/SingleOrderMutation/' + str(args.operator)

    else:
        first_dir_path = str(parent_directory) + '/experiments/Mutated_Agents/SingleOrderMutation/' + str(args.operator) + '/'+str(args.old_environment_name)+'/'+str(args.algorithm)+'/logs'
        second_dir_path = str(parent_directory) + '/experiments/Mutated_Agents/SingleOrderMutation/' + str(args.operator)




else:
    print("There's an error")
    sys.exit()


old_substring = str(args.old_environment_name)
print("old_substring = ", old_substring)

new_substring = str(args.new_environment_name)

print("new_substring = ", new_substring)

if args.operator == "policy_activation_change" and not os.path.exists(first_dir_path):
    first_dir_path = str(parent_directory) + '/experiments/Mutated_Agents/SingleOrderMutation/' + str(args.operator) + '/' + str(args.new_environment_name) + '/' + str(args.algorithm) + '/' + str(args.op) + '/logs'
    second_dir_path = str(parent_directory) + '/experiments/Mutated_Agents/SingleOrderMutation/' + str(args.operator)
    rename_folders(first_dir_path, old_substring, new_substring)
else:
    rename_folders(first_dir_path, old_substring, new_substring)
    rename_folders(second_dir_path, old_substring, new_substring)

