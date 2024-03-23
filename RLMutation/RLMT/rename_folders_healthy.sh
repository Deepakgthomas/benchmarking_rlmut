export CUDA_VISIBLE_DEVICES=""

set -e



python rename_program.py healthy $1 $2 --algorithm $3



