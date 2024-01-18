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
#for arg in "${!operators[@]}"; do
#
#  python rename_program.py mutated CartPole-v1 myCartPole-v1 $arg PPO ${operators[$arg]}
#
#done
#todo Healthy PPO has some problems. The title has capital "V"
#python rename_program.py healthy CartPole-v1 myCartPole-v1 -algorithm PPO
#Checking here




