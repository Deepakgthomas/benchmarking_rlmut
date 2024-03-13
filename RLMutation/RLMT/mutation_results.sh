export CUDA_VISIBLE_DEVICES=""

set -e


##todo WARN: The obs returned by the `reset()` method is not within the observation space.
##todo WARN: Why did the commented call in the second for loop fail?
#todo Had to delete PAC_ReLu and NR
#todo Extract all todos
if [ "$2" = "dqn" ]; then
  my_array=("ILF" "M_1.0" "R_1.0" "Ra_1.0" "RN_1.0" "NDF" "MSU" "MTS" "PAC_Sigmoid" "POC_SGD")
else
  my_array=("ILF" "M_1.0" "R_1.0" "Ra_1.0" "RN_1.0" "NDF" "NR" "MSU" "MTS" "PAC_Sigmoid" "POC_SGD" "PAC_ReLU")
fi

for arg in "${my_array[@]}"; do
  echo "Operator $arg"
  python eval_mut.py -a $2 -e $1 -m $arg
done > "output_$1_$2_$3_$4.txt"




