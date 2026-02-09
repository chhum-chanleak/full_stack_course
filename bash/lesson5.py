# Quoting

# && / ||

# Exit codes (conceptual)

# Tiny scripts

# 1. Quoting
# i. In Bash, quoting controls how the shell interprets text.

# Example 1: No quotes (default behavior)

# name=Hello World
# echo $name

# What happens

# ❌ Error: World: command not found

# Why

# Bash splits on spaces

# It thinks:

# name=Hello

# then tries to run World as a command

# ✅ Correct version:

# name=Hello\ World

# Rule:
# Without quotes, spaces, globbing, and expansions all happen.

# Example 2: Double quotes " " (most commonly used)

# name="Hello World"
# echo "$name"

# Output

# Hello World

# What double quotes do

# Preserve spaces

# Still allow:

# Variable expansion ($name)

# Command substitution ($(...))

# Escape sequences (\n, \")

# Example:

# echo "Today is $(date)"

# Rule:
# Use double quotes when you want variables expanded but text kept together.

# Example 3: Single quotes ' ' (literal text)

# name="Alice"
# echo '$name is here'

# Output

# $name is here

# Why

# Single quotes disable everything

# No variables

# No commands

# No escapes

# Rule:

# Single quotes mean: “Take this text exactly as-is.”

# Best for:

# Regex

# Passwords

# SQL

# JSON

# Literal strings

# Example 4: Quotes vs globbing (*)

# echo *.txt

# Output (example)

# a.txt b.txt notes.txt

# Now with quotes:

# echo "*.txt"

# Output

# *.txt

# Why

# Without quotes: * expands (globbing)

# With quotes: treated as literal text

# Rule:
# Quotes prevent wildcard expansion.

# 2. Logical operators (&& / ||)

# Example 1: && (AND)

# mkdir new_folder && echo "Folder created successfully"

# If mkdir new_folder succeeds → prints message

# If folder already exists → no message

# Example 2: || (OR)

# mkdir new_folder || echo "Folder already exists"

# If mkdir fails (folder exists) → prints message

# If mkdir succeeds → does not print

# Example 3: Combining && and ||

# mkdir project && echo "Created" || echo "Failed"

# If mkdir project succeeds → prints Created

# If mkdir project fails → prints Failed

# Warning: Be careful: this behaves differently in complex cases because echo "Created" can succeed, preventing || from running. Sometimes parentheses are needed.

# Example 4: Using with commands that might fail

# grep "hello" file.txt && echo "Found" || echo "Not found"

# If file.txt exists and contains "hello" → prints Found

# If not found → prints Not found

# 3. Exit codes or return value

# i. What are exit codes?

# Every command in Bash returns a number when it finishes — this is called the exit code.

# Convention:

# 0 → success

# Non-zero → failure (different numbers can indicate different types of errors)

# $? → special variable that holds the exit code of the last command

# ii. Why exit codes matter?

# They tell Bash whether a command succeeded or failed.

# && and || rely on exit codes.

# Scripts use exit codes for conditional execution and error handling.

# Example 1: Checking success

# mkdir my_folder
# echo $?   # prints 0 if folder created, non-zero if it failed

# Example 2: Using &&

# mkdir new_dir && echo "Created successfully"

# echo runs only if mkdir succeeded (exit code 0)

# Example 3: Using ||

# mkdir existing_dir || echo "Directory already exists"

# echo runs only if mkdir failed (exit code ≠ 0)

# Example 4: In scripts with conditional checks

# grep "hello" file.txt
# if [ $? -eq 0 ]; then
#     echo "Found 'hello'"
# else
#     echo "Did not find 'hello'"
# fi

# $? captures the exit code of grep

# 0 → string found, non-zero → string not found

# 4. Basic scripts

# i. A basic Bash script is:

# A file containing Bash commands

# Executed top-to-bottom

# Driven by exit codes, not magic

# Minimum structure:

# #!/bin/bash
# commands...

# ii. Why we use basic Bash scripts?

# a. Automation

# Turn repeated manual commands into a single action

# Save time and reduce effort

# b. Preventing mistakes

# Enforce correct order of operations

# Stop execution when a critical step fails

# Reduce risk of running commands in the wrong place

# c. Encoding logic

# Store decisions and conditions in code instead of memory

# Let exit codes drive behavior

# d. Reproducibility

# Same script → same behavior every time

# Acts as automation + documentation

# e. Glue between tools

# Combine small Unix tools into a workflow

# Pipe and chain commands together

# f. Scalability

# Basic scripts naturally grow into:

# build scripts

# backup scripts

# deployment scripts

# monitoring scripts

# Example 1: Minimal script (structure)

# #!/bin/bash
# echo "Hello from Bash"

# What this teaches:

# Script structure

# echo prints output

# Script exits with 0 if nothing fails

# How to run:

# chmod +x hello.sh
# ./hello.sh

# Example 2: Basic automation

# #!/bin/bash
# mkdir logs
# echo "Logs directory ready"

# What this teaches:

# Scripts remove repeated typing

# Commands run sequentially

# Example 3: Using exit codes for logic

# #!/bin/bash
# mkdir backup && echo "Backup created" || echo "Backup already exists"

# What this teaches:

# Commands return exit codes

# && and || act like simple if / else

# Logic is driven by success or failure

# Example 4: Guarding against failure (very important)

# #!/bin/bash
# cd project || exit 1
# echo "Now inside project directory"

# What this teaches:

# Guard pattern

# Script stops if a critical step fails

# Prevents dangerous mistakes