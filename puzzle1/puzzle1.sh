#!/bin/bash

INPUT=puzzle1.input

counter=0

while read -n1 char; do
    if [[ $char == "(" ]]; then
        let counter=counter+1
    elif [[ $char == ")" ]]; then
        let counter=counter-1
    fi
done < $INPUT

echo $counter



