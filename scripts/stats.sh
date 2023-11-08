#!/bin/bash
# helper to get the total prompt counts for each prompt type

count_prompts() {
    local folder_type=$1
    local count=$(find "$folder_type" -name "assessment.json" 2>/dev/null | wc -l)
    echo "$count"
}

count_prompts_per_casestudy() {
    local sub_folder="$1"
    local m1_count=0
    local m2_count=0
    local m3_counts=()

    if [ -d "$sub_folder/m1" ]; then
        m1_count=$(count_prompts "$sub_folder/m1")
    fi

    if [ -d "$sub_folder/m2" ]; then
        m2_count=$(count_prompts "$sub_folder/m2")
    fi

    while IFS= read -r -d $'\0' faker_folder; do
        if [ -d "$faker_folder" ]; then
            count=$(count_prompts "$faker_folder")
            m3_counts+=("$count")
        fi
    done < <(find "$sub_folder" -maxdepth 1 -type d -name '*-faker' -print0)

    local total_local_m3=0
    for count in ${m3_counts[@]}; do
        if [[ $count =~ ^[0-9]+$ ]]; then
            ((total_local_m3 += count))
        fi
    done

    echo "$m1_count $m2_count $total_local_m3"
}

get_total_prompt_count() {
    local root_dir="data"
    local total_m1=0
    local total_m2=0
    local total_m3=0

    for sub_folder in "$root_dir"/*/; do
        if [ -d "$sub_folder" ]; then
            local counts=$(count_prompts_per_casestudy "$sub_folder")
            read m1_count m2_count m3_count <<< "$counts"
            ((total_m1 += m1_count))
            ((total_m2 += m2_count))
            ((total_m3 += m3_count))
            echo "Prompt counts for $(basename "$sub_folder") - m1: $m1_count, m2: $m2_count, m3: $m3_count"
        fi
    done

    echo "Total prompt count - m1: $total_m1, m2: $total_m2, m3: $total_m3"
}

get_total_prompt_count
