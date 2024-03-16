export CUDA_VISIBLE_DEVICES=""

set -e
# Look at the rules for [] and equality checking in Bash for future reference.

if [ "$3" = "DQN" ]; then
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
    ["policy_activation_change"]="Sigmoid"
    ["policy_optimizer_change"]="SGD"
  )

else
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

fi

for arg in "${!operators[@]}"; do

  for val in ${operators[${arg}]}; do

    python rename_program.py mutated $1 $2 --operator ${arg} --algorithm $3 -op_val ${val}

  done

done

#todo ReLU/Sigmoid doesn't work
#todo Why is LunarLander coming in the output?


