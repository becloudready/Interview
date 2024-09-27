#!/bin/bash
clear
read -p "Enter a number: " num
result=0
for i in $(seq 1 $num); do 
	result=$((result+i))
done
echo $result