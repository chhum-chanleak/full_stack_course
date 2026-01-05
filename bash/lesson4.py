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

# 2. Basic argument variables
# Inside a script or function, Bash provides these:

# Variable	Meaning
# $1	First argument
# $2	Second argument
# $3	Third argument
# $#	Number of arguments
# $0	Script name

# Example 1: Reading arguments in a script

# Script: args.sh
# echo "First argument: $1"
# echo "Second argument: $2"

# Run:
# ./args.sh apple banana

# Output:
# First argument: apple
# Second argument: banana

# Example 2: Counting arguments
# Script:
# echo "You passed $# arguments"

# Run:
# ./args.sh one two three

# Output:
# You passed 3 arguments

# Example 3: Arguments with spaces (quotes matter)
# Script:
# echo "First argument: $1"
# echo "Second argument: $2"

# Run:
# ./args.sh "hello world" bash

# Output:
# First argument: hello world
# Second argument: bash


# Quotes keep words together as one argument.

# Example 4: Arguments in a function
# say_hi() {
#   echo "Hi $1"
# }

# say_hi Alice
# say_hi Bob

# Output:
# Hi Alice
# Hi Bob

# Inside a function, $1 refers to the function’s argument, not the script’s.

# Key takeaways

# Arguments are positional: order matters

# $1, $2, $3 access them

# $# tells how many

# Scripts and functions use arguments the same way

# Tiny self-check

# If you run:

# ./test.sh "one two" three

# What is $1?

# What is $2?

# (Answer it mentally — that’s how you lock it in.)