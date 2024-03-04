export CUDA_VISIBLE_DEVICES=""

set -e


#todo Note the capital V in the original environment name
echo "Why should the V be capital in healthy?"
python rename_program.py healthy $1 $2 -algorithm $3
#todo ReLU/Sigmoid doesn't work
#todo Why is LunarLander coming in the output?


