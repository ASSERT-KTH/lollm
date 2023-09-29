#!/bin/bash
# helper to populate the data folder
# usage: scripts/populate.sh data/french-comedy/ruby-faker/03

DIR=$1

mkdir -p $DIR

touch $DIR/prompt.txt
touch $DIR/output.txt
touch $DIR/execution-result.txt
touch $DIR/assessment.json

cat > $DIR/assessment.json << EOF
{
 "model":"",
 "data_constraints_can_be_checked": "",
 "number_of_options_in_the_generators": "",
 "cultural_alignment": "",
 "cultural_alignment_quantitative": "",
 "executes": "",
 "execute_error": "",
 "contains_true_generator":"",
 "comments":""
}
EOF

