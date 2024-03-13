export CUDA_VISIBLE_DEVICES=""

set -e

if [ "$2" = dqn ]; then
# https://stackoverflow.com/questions/1494178/how-to-define-hash-tables-in-bash
  declare -A operators=(
    ["incorrect_loss_function"]="None"
    ["mangled"]="1.0"
    ["repeat"]="1.0"
    ["policy_activation_change"]="Sigmoid"
    ["random"]="1.0"
    ["reward_noise"]="1.0"
    ["missing_state_update"]="None"
    ["missing_terminal_state"]="None"
    ["no_discount_factor"]="None"
    ["policy_optimizer_change"]="SGD"
  )

else

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

fi


for arg in "${!operators[@]}"; do
  for val in ${operators[${arg}]}; do
    echo "Running Operator" ${arg} "Value" ${val}
    json_string="{\"$arg\":\"${val}\"}"
    python test_agent.py -a $2 -na 20 -e $1 -m $json_string
  done

done

echo "Running Healthy Agent"
python test_agent.py -a $2 -na 20 -e $1



