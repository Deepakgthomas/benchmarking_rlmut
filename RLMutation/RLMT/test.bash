declare -A X=(
  ['s1']="firstname secondname"
  ['s2']="surname"
  ['s3']="other"
)

for arg in "${!X[@]}"; do
    for val in ${X[${arg}]}; do
        echo "${arg}, ${val}"
    done
done