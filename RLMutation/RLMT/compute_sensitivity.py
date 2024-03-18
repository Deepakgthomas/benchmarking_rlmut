import sys
import os
import pandas as pd
from collections import defaultdict
operator_dict = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: defaultdict(dict))))#todo Not sure of this. Check it.

folder_path = 'final_result'
files = os.listdir(folder_path)
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

        operator_dict[str(algorithm)][str(environment)][str(test_generator_type)][str(mutation_type)] = defaultdict(int)

        # Open the file for processing
        with open(file_path, 'r') as file:
            for line in file:
                str_val = line.strip() #todo Not sure about line.strip(). Check this.
                if "Operator" in str_val:
                    operator_value = str_val.replace("Operator", "").strip()
                    # print("operator_value = ",operator_value)
                    ready_to_append = True
                if "Distance Distribution Test" in str_val:
                    if ready_to_append:
                        mutation_result = str_val.replace("Distance Distribution Test :","").strip()
                        if "Not Killed" in mutation_result:
                            operator_dict[str(algorithm)][str(environment)][str(test_generator_type)][str(mutation_type)][str(operator_value)]=0

                        elif "Inconclusive" in mutation_result:
                            print("Something is wrong. Exit system")
                            sys.exit()
                        else:
                            operator_dict[str(algorithm)][str(environment)][str(test_generator_type)][str(mutation_type)][str(operator_value)]=1 #todo Come up with a better way to represent killed

                        ready_to_append = False


out = pd.json_normalize(operator_dict)
out.columns = out.columns.str.split('.', expand=True,n=4) #Check this


# Check this carefully
# Group by all levels of the multi-level column
sum_data = out.groupby(level=[0, 1,2,3], axis = 1).sum()
count_data = out.groupby(level=[0, 1,2,3], axis = 1).count()
result_df = pd.concat([sum_data, count_data], axis=0, keys=['Sum', 'Count'])
result_df.index = result_df.index.droplevel(-1) #todo Very dangerous operation! Please check!!!
result_df.loc['mutation_score'] = result_df.loc['Sum']/result_df.loc['Count']
result_df.to_csv("final_result.csv")

# Convert the grouped data into a DataFrame
# result_df = pd.DataFrame(grouped_data).reset_index()