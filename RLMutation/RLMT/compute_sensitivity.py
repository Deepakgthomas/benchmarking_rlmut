import sys
import shutil

import os
import pandas as pd
from collections import defaultdict
operator_dict = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: defaultdict(dict))))#todo Not sure of this. Check it.

rq2_folder="rq2_folder"
if os.path.exists(rq2_folder):
    # Delete the folder
    shutil.rmtree(rq2_folder)
os.makedirs(rq2_folder)

folder_path = 'final_result'
files = os.listdir(folder_path)
data_list = []
for file_name in files:
    # Construct the full path to the file
    file_path = os.path.join(folder_path, file_name)

    # Check if the path is a file (not a directory)
    if os.path.isfile(file_path):
        if "dqn" in file_name:
            algorithm = "dqn"
        else:
            algorithm = "ppo"
        if "CartPole-v1" in file_name:
            environment = "CartPole-v1"
        else:
            environment = "LunarLander-v2"
        if "_strong_" in file_name:
            test_generator_type = "strong"
            start_index=file_name.find("_strong_")
            end_index=file_name.find("_stdout_")
            mutation_type = file_name[start_index + len("_strong_"):end_index]
        else:
            test_generator_type = "weak"
            start_index=file_name.find("_weak_")
            end_index=file_name.find("_stdout_")
            mutation_type = file_name[start_index + len("_weak_"):end_index]

        operator_dict[str(environment)][str(algorithm)][str(test_generator_type)][str(mutation_type)] = defaultdict(int)
        data_list.append((str(environment),str(algorithm), str(test_generator_type), str(mutation_type)))
        # Open the file for processing
        with open(file_path, 'r') as file:
            for line in file:
                str_val = line.strip() #todo Not sure about line.strip(). Check this.
                if "Operator" in str_val:
                    operator_value = str_val.replace("Operator", "").strip()
                    ready_to_append = True
                if "Distance Distribution Test" in str_val:
                    if ready_to_append:
                        mutation_result = str_val.replace("Distance Distribution Test :","").strip()
                        if "Not Killed" in mutation_result:
                            operator_dict[str(environment)][str(algorithm)][str(test_generator_type)][str(mutation_type)][str(operator_value)]=0

                        elif "Inconclusive" in mutation_result:
                            operator_dict[str(environment)][str(algorithm)][str(test_generator_type)][str(mutation_type)][str(operator_value)]=0
                        else:
                            operator_dict[str(environment)][str(algorithm)][str(test_generator_type)][str(mutation_type)][str(operator_value)]=1

                        ready_to_append = False


out = pd.json_normalize(operator_dict)
out.columns = out.columns.str.split('.', expand=True,n=4) #Check this
out.to_csv(str(rq2_folder)+"/final_result.csv")

# Check this carefully
# Group by all levels of the multi-level column
sum_data = out.groupby(level=[0, 1,2,3], axis = 1).sum() #todo Check groupby
count_data = out.groupby(level=[0, 1,2,3], axis = 1).count()
result_df = pd.concat([sum_data, count_data], axis=0, keys=['Sum', 'Count'])
result_df.index = result_df.index.droplevel(-1) #todo Very dangerous operation! Please check!!!
result_df.loc['mutation_score'] = result_df.loc['Sum']/result_df.loc['Count']
result_df.to_csv(str(rq2_folder)+"/mutation_score.csv")


# print(result_df.at['mutation_score', ('dqn', 'CartPole-v1', 'strong', 'constant')])
sensitivity_dict = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: defaultdict(dict))))#todo Not sure of this. Check it.

for i in data_list:
    if i[2]=='weak':
        continue

    weak_tuple=(str(i[0]),str(i[1]),str("weak"),str("constant"))
    sensitivity_dict[str(i[0])][str(i[1])][str(i[3])]=(result_df.at['mutation_score', i]-result_df.at['mutation_score', weak_tuple])/result_df.at['mutation_score', i]
sensitivity_df = pd.json_normalize(sensitivity_dict)
sensitivity_df.columns = sensitivity_df.columns.str.split('.', expand=True) #Check this
sensitivity_df.to_csv(str(rq2_folder)+"/sensitivity_df_.csv")