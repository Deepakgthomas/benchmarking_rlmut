import sys
import os

from collections import defaultdict
operator_dict = defaultdict(lambda: defaultdict(dict)) #todo Not sure of this. Check it.

folder_path = '/home/thoma/Downloads/results_mutation_benchmark'
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
        else:
            test_generator_type = "weak"
        operator_dict[str(algorithm)][str(environment)][str(test_generator_type)] = defaultdict(list)

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
                            operator_dict[str(algorithm)][str(environment)][str(test_generator_type)][str(operator_value)].append(0)

                        elif "Inconclusive" in mutation_result:
                            print("Something is wrong. Exit system")
                            sys.exit()
                        else:
                            operator_dict[str(algorithm)][str(environment)][str(test_generator_type)][str(operator_value)].append(1) #todo Come up with a better way to represent killed

                        ready_to_append = False

print(operator_dict)



