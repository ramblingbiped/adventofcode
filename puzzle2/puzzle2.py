#!/usr/bin/env python3

total = []

with open('puzzle2.input') as f:
    for line in f:
        # Create an empty array, split the string into three parts, convert
        # each part into an integer and add it to the array.
        int_array = []
        int_array.append(int(line.split('x')[0]))
        int_array.append(int(line.split('x')[1]))
        int_array.append(int(line.split('x')[2]))
    
        
        length = int_array[0]
        width = int_array[1]
        height = int_array[2]

        package_area = ( 2 * length * width ) + ( 2 * width * height ) + ( 2 * height * length )

        slack_array = int_array
        slack_array.remove(max(slack_array))
        
        slack = slack_array[0] * slack_array[1]

        total_paper = package_area + slack

        total.append(total_paper)

print(sum(total))
