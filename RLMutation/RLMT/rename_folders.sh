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
  ["policy_activation_change"]="ReLU Sigmoid"
  ["policy_optimizer_change"]="SGD"
)




for arg in "${!operators[@]}"; do

  for val in ${operators[${arg}]}; do

    python rename_program.py mutated LunarLander-v2 $1 -operator ${arg} -algorithm $2 -op ${val}

  done

done
#todo Note the capital V in the original environment name
python rename_program.py healthy LunarLander-V2 $1 -algorithm $2
#todo ReLU/Sigmoid doesn't work
#todo Why is LunarLander coming in the output?


