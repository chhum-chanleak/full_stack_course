# 1. Variables
# i. Variables in Bash store data (strings, numbers, paths, etc.) that you can use later in scripts or commands.

# Key points:

# No spaces around = when assigning:

# NAME=Alice  # ✅ correct
# NAME = Alice  # ❌ wrong

# Reference variables with $:

# echo $NAME

# By default, all variables are strings.

# Use export to make a variable available to child processes.

# Example 1: Basic variable

# NAME="Alice"
# echo "Hello, $NAME!"

# Output:

# Hello, Alice!

# Explanation:

# Assign a string to NAME

# Use $NAME to print its value

# Example 2: Numeric variable

# AGE=25

# echo "I am $AGE years old."

# Output:

# I am 25 years old.

# Explanation:

# Numbers are treated as strings unless used in arithmetic

# Bash doesn’t require explicit typing

# Example 3: Variables with command output

# DATE=$(date)

# echo "Today is $DATE"

# Output: (example)

# Today is Sat Jan 3 12:34:56 UTC 2026

# Explanation:

# $(command) captures the output of a command

# Assign it to a variable for later use

# Example 4: Add two variables

# A=5
# B=3

# SUM=$((A + B))
# echo $SUM

# Output: 8

# Key point:

# $(( ... )) tells Bash: this is arithmetic

# 2. set
#. We use "set" to view declared variables.

# Declare a variable
# my_name="Alice"

# Check all declared variables

# set

# output:

# BASH=/bin/bash
# HOME=/home/alice
# my_name=Alice
# ...
