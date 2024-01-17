export CUDA_VISIBLE_DEVICES=""

set -e

# https://stackoverflow.com/questions/1494178/how-to-define-hash-tables-in-bash
declare -A operators=(
  ["incorrect_loss_function"]="None"
  ["mangled"]="1.0"
  ["repeat"]="1.0"
  ["random"]="1.0"
  ["reward_noise"]="1.0"
  ["missing_state_update"]="None"
  ["missing_terminal_state"]="None"
  ["no_discount_factor"]="None"
  ["no_reverse"]="None"
  ["policy_activation_change"]="ReLU"
  ["policy_activation_change"]="Sigmoid"
  ["policy_optimizer_change"]="SGD"
)
for arg in "${!operators[@]}"; do
  json_string="{\"$arg\":\"${operators[$arg]}\"}"

  python rename_program.py mutated myCartPole-v1 $arg PPO ${operators[$arg]}
  if [ $? -ne 0 ]; then
    echo "Error: Python renaming failed"
  fi
  python test_agent.py -a ppo -na 20 -e myCartPole-v1 -m $json_string
  if [ $? -ne 0 ]; then
    echo "Error: Python test agent failed"
  fi
done
#todo WARN: The obs returned by the `reset()` method is not within the observation space.
#todo WARN: Why did the commented call in the second for loop fail?

my_array=("ILF" "M_1.0" "R_1.0" "Ra_1.0" "RN_1.0" "NDF" "NR" "MSU" "MTS" "PAC_ReLU" "PAC_Sigmoid" "POC_SGD")
for arg in "${my_array[@]}"; do
  python eval_mut.py -a ppo -e myCartPole-v1 -m $arg
done > output.txt



