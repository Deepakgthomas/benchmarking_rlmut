export CUDA_VISIBLE_DEVICES=""

set -e

# https://stackoverflow.com/questions/1494178/how-to-define-hash-tables-in-bash
declare -A operators=(
  ["incorrect_loss_function"]="None"
  ["mangled"]="1.0"
  ["repeat"]="1.0"
  ["policy_activation_change"]="ReLU Sigmoid"
  ["random"]="1.0"
  ["reward_noise"]="1.0"
  ["missing_state_update"]="None"
  ["missing_terminal_state"]="None"
  ["no_discount_factor"]="None"
  ["no_reverse"]="None"
  ["policy_optimizer_change"]="SGD"
)


for arg in "${!operators[@]}"; do
  for val in ${operators[${arg}]}; do
    echo "Running Operator" ${arg} "Value" ${val}
    json_string="{\"$arg\":\"${val}\"}"
    echo $json_string
#    python train.py -a ppo -na 20 -e LunarLander-v2 -t 200000 -s 0 -m $json_string
  done

done




