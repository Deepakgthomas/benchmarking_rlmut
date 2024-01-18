import os
import sys
import argparse
full_path = os.getcwd()
parent_directory = os.path.dirname(full_path)


def rename_folders(directory_path, old_substring, new_substring):
    for folder_name in os.listdir(directory_path):
        old_folder_path = os.path.join(directory_path, folder_name)

        # Check if it's a directory
        if os.path.isdir(old_folder_path):
            # Replace the specified substring in the folder name
            new_folder_name = folder_name.replace(old_substring, new_substring)

            # Construct the full paths for the old and new folders
            old_folder_path = os.path.join(directory_path, folder_name)
            new_folder_path = os.path.join(directory_path, new_folder_name)

            try:
                # Rename the folder
                os.rename(old_folder_path, new_folder_path)
                print(f"Folder '{folder_name}' successfully renamed to '{new_folder_name}'.")
            except FileExistsError:
                print(f"Error: Folder '{new_folder_name}' already exists.")


parser = argparse.ArgumentParser()
parser.add_argument('agent_type', help = 'Enter whether the agent is healthy or mutated')
parser.add_argument('old_environment_name', help='Enter the name of the environment name you want to replace')
parser.add_argument('new_environment_name', help='Enter the name of the environment name you want to replace your old name with')
parser.add_argument('-operator', required=False,help = 'Enter the name of the operator')
parser.add_argument('-algorithm', required=False,help='Enter the name of the algorithm')
parser.add_argument('-op', required=False ,help = 'Enter the operator parameter')
args = parser.parse_args()
if args.agent_type=='healthy':
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
print("first_dir_path = ", first_dir_path)
print("second_dir_path = ", second_dir_path)

rename_folders(first_dir_path, old_substring, new_substring)
rename_folders(second_dir_path, old_substring, new_substring)

